
# How to start:
#method 1:
# python utube_downloader.py
#method 2:
# double click the youtube1.exe on dist folder and the GUI program should open.

import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL  # python -m pip install yt-dlp if not installed

# Define GUI Elements
def createWidgets():
    link_label = Label(root, text="Youtube URL: ", bg="#E8D579")
    link_label.grid(row=1, column=0, pady=5, padx=5)

    root.link_text = Entry(root, width=60, textvariable=video_link)
    root.link_text.grid(row=1, column=1, pady=5, padx=5)

    destination_label = Label(root, text="Destination ", bg="#E8D579")
    destination_label.grid(row=2, column=0, pady=5, padx=5)

    root.destination_text = Entry(root, width=55, textvariable=download_path)
    root.destination_text.grid(row=2, column=1, pady=3, padx=3)

    browse_but = Button(root, text="Browse", command=browse, width=10, bg="#05E8E0")
    browse_but.grid(row=2, column=2, pady=1, padx=1)

    download_but = Button(root, text="Download Videos", command=download_video, width=25, bg="#05E8E0")
    download_but.grid(row=3, column=1, pady=2, padx=2)

    download_but1 = Button(root, text="Download Audio", command=download_audio, width=20,
                           bg="#05E8E0")
    download_but1.grid(row=3, column=2, pady=3, padx=3)


def browse():
    download_dir = filedialog.askdirectory(initialdir="Your Directory Path")
    download_path.set(download_dir)


def download_video():
    url = video_link.get()
    folder = download_path.get()

    ydl_opts = {
        'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'outtmpl': f'{folder}/%(title)s.%(ext)s',
        'merge_output_format': 'mp4' , # Ensures the output file is in MP4 format
        'ffmpeg_location': 'C:/ffmpeg'  # Path to your ffmpeg installation
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Video downloaded to: {folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")


def download_audio():
    url = video_link.get()
    folder = download_path.get()

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{folder}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': 'C:/ffmpeg'  # Path to your ffmpeg installation
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", f"Audio downloaded to: {folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download audio: {e}")


# Main Application Setup
root = tk.Tk()

root.geometry("650x120")
root.resizable(False, False)
root.title("Youtube Video and Audio Downloader")
root.config(background="#D4BDAC")

video_link = StringVar()
download_path = StringVar()

createWidgets()

root.mainloop()
