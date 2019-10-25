# coding:utf-8

import requests


class VideoBase:
    def __init__(self, url: str):
        self.sender = requests.session()
        self.sender.headers = {
            'Connection': 'keep-alive',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/66.0.3359.139 Safari/537.36 '
        }
        self.url = url
        self.seek = 0

        self.duration = 0
        self.balance = 0
        self.width = 0
        self.height = 0
        self.sample_count = 0

    @property
    def framerate(self) -> int:
        pass

    def __str__(self):
        return '时长(秒):' + str(self.duration) + '\n' + \
               '宽(像素):' + str(self.width) + '\n' + \
               '高(像素):' + str(self.height) + '\n' + \
               '帧率(每秒):' + str(self.framerate) + '\n' + \
               '声道(0立体声，-1左声道，1右声道):' + str(self.balance)
