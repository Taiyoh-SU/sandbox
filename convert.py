import ffmpeg
import os

# ファイルmediaにある音声のない動画ファイルと音声のみのファイルを結合して保存
in_directory = "media"
media = os.listdir(in_directory)
num = 0
for i in media:
    print(f"{num}: {i}")
    num += 1
videopath = in_directory + "/" + media[int(input("Please select Video File Number: "))]
audiopath = in_directory + "/" + media[int(input("Please select Audio File Number: "))]
outputpath = "out.mp4"

vstream = ffmpeg.input(videopath)
astream = ffmpeg.input(audiopath)

stream = ffmpeg.output(vstream, astream, outputpath, vcodec="copy", acodec="aac")
ffmpeg.run(stream)
input("Done! Please hit any key...")
