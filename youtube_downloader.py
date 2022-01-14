"""
First: create and activate the virtual environment
Second: install the required package using: pip install pytube
Note: By default, the download path will be in the project directory.
    you can leave it that way or you can change it by using the os module
    and save the video wherever you want to.
"""
from pytube import YouTube
import os

# change the path to where you want to save the video
os.chdir("/home/omer358/Downloads/youtube_videos")

# go to the youtube video page and copy the URL
link = input("Enter your Youtube URL: ")
yt = YouTube(link)
queries = yt.streams
download_opts = list(enumerate(queries))
for opt in download_opts:
    print(opt)

print("Enter the desired option: ")
choice = int(input("enter the option: "))
dn_video = queries[choice]
video_size = dn_video.filesize / (1024 * 1024)
print("the total video size is:{:.2f}MB".format(video_size))
print("Downloading...")
dn_video.download()
print("Download has been successfully completed in: {}".format(os.getcwd()))
