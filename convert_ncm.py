from ncmdump import NeteaseCloudMusicFile

ncmfile = NeteaseCloudMusicFile("filename.ncm")
ncmfile.decrypt()

print(ncmfile.music_metadata)  # show music metadata

ncmfile.dump_music("filename.mp3")  # auto detect correct suffix

# Maybe you also need dump metadata or cover image
# ncmfile.dump_metadata("filename.json")
# ncmfile.dump_cover("filename.jpeg")


import os
from ncmdump import NeteaseCloudMusicFile

# 获取所有需要转换音乐的文件名
directory = "./input_music/"
out_path = "./output_music/"
files_name = os.listdir(directory)
input_music = ""
out_music = ""

# 输出转换后的文件
first_name = []
for name in files_name:
    input_music = directory + name
    ncmfile = NeteaseCloudMusicFile(str(input_music))
    ncmfile.decrypt()
    print(ncmfile.music_metadata)  # show music metadata
    out_music = out_path + name.split(".")[0]
    ncmfile.dump_music(str(out_music))  # auto detect correct suffix
