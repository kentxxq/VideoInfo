# coding:utf-8

import requests
import struct
from .parse import Box
from construct.lib.container import Container
from .VideoBase import VideoBase


class Mp4Url(VideoBase):
    def __init__(self, url: str):
        super(Mp4Url, self).__init__(url)

    def getAll(self):
        """
        一次性获得所有元数据。
        优点是请求次数少，缺点是请求数据量变大。
        但是现在网速越来越快了，如果真的很慢，那么说明资源不好，获取资源的信息也变得没意义。
        亦或者你的网络有问题，你应该先解决这个问题，来确保程序可以高效运行。
        """
        while True:
            size, flag = self._findMoov()
            if flag == 'moov':
                break
            else:
                self.seek += size

        data = self._getMoov(size)
        for child in data.children:
            if child.type == b'mvhd':
                self.duration = int(child.duration / child.timescale)
            if child.type == b'trak':
                results = child.search_all('type')
                if b'smhd' in results:
                    self.balance = child.search_all('balance')[0]
                if b'vmhd' in results:
                    width = child.search_all('width')[0]
                    height = child.search_all('height')[0]

                    self.width = int(bytes(bin(width).replace('0b', '').zfill(32)[:16], encoding='ascii'),
                                     base=2)
                    self.height = int(bytes(bin(height).replace('0b', '').zfill(32)[:16], encoding='ascii'),
                                      base=2)
                    self.sample_count = child.search_all('sample_count')[0]

    @property
    def framerate(self) -> int:
        return int(self.sample_count / self.duration)

    def _getMoov(self, size: int) -> Container:
        self._setHeaders(self.seek, size)
        data = self._sendRequest()
        boxdata = Box.parse(data)
        return boxdata

    def _setHeaders(self, seek: int, size: int):
        self.sender.headers['Range'] = f'bytes={seek}-{seek + size - 1}'

    def _sendRequest(self) -> bytes:
        try:
            data = self.sender.get(url=self.url, stream=True,
                                   timeout=6).raw.read()
        except requests.Timeout:
            raise self.url + '连接超时:超过6秒(默认)服务器没有响应任何数据！'
        return data

    def _findMoov(self) -> (int, str):
        self._setHeaders(self.seek, 8)
        data = self._sendRequest()
        size = int(struct.unpack('>I', data[:4])[0])
        flag = data[-4:].decode('ascii')
        return size, flag
