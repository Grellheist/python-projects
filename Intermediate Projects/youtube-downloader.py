from pytube import YouTube
from sys import argv

link = argv[1]  # Gets the link which is the second position on the command 
yt = YouTube(link) 
print("Title: ", yt.title)
yt_download = yt.streams.get_highest_resolution()  # Downloads best resolution by default
yt_download.download()

# Command should follow: python3 youtube_downloader "[video link]"
