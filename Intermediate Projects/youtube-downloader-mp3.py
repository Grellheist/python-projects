from pytube import YouTube
from sys import argv
import os

link = argv[1]  # Gets the link which is the second position on the command 
yt = YouTube(link) 
print("Title: ", yt.title)
yt_download = yt.streams.filter(only_audio=True).first()  # Downloads best resolution by default
out_file = yt_download.download()
base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file, new_file)
# Command should follow: python3 youtube_downloader "[video link]"
