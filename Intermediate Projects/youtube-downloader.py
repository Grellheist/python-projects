import customtkinter as tk
from pytube import YouTube, Playlist
import os

tk.set_appearance_mode("dark")
tk.set_default_color_theme("dark-blue")

# Functions


def video_downloader():
    get_link = entry1.get()
    yt = YouTube(get_link).streams.filter(only_audio=True).first()
    out_file = yt.download()
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3"
    os.rename(out_file, new_file)


def playlist_downloader():
    get_link = entry2.get()
    yt = Playlist(get_link)
    for video in yt.videos:
        out_file = video.streams.filter(only_audio=True).first().download()
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)


root = tk.CTk()
root.geometry("500x350")

root.title("Youtube video/playlist to mp3 by Grellheist")

frame = tk.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

entry1 = tk.CTkEntry(master=frame, placeholder_text="Video Link")
entry1.pack(pady=12, padx=10)

button1 = tk.CTkButton(master=frame, text="Download video as mp3", command=video_downloader)
button1.pack(pady=12, padx=10)

entry2 = tk.CTkEntry(master=frame, placeholder_text="Playlist Link")
entry2.pack(pady=12, padx=10)

button2 = tk.CTkButton(master=frame, text="Download playlist as mp3", command=playlist_downloader)
button2.pack(pady=12, padx=10)


root.mainloop()
