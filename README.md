简介
===

这个包是用来获取在线视频文件元数据的。

USAGE
==

```python
from VideoInfo import Mp4Url

mp4=Mp4Url('http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4')

mp4.getAll()

print(mp4)
```


TODO
===

后续没事的时候，把一些avi，rmvb，mkv什么的都弄好。

如果是本地文件
===

推荐安装一个ffmpeg，通过调用命令行获取数据