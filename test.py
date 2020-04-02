# from VideoInfo import Mp4Url

# mp4 = Mp4Url('http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4')
# mp4.getAll()
# print(mp4)

from temp.jpeg import Jpeg

j = Jpeg.from_file(
    r"C:\\Users\\kentxxq\Desktop\\a01de1df06bbc2563316d5e579cb9b79_1200x500.jpg"
)

print(j.segments)
