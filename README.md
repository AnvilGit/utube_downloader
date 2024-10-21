# YouTube Video and Audio Downloader

- This is a simple Python application that allows you to download YouTube videos and audio using `yt-dlp` and `Tkinter` for the GUI. 
- You can download either videos (in MP4 format) or audio (in MP3 format) from YouTube by providing a URL and selecting a destination folder for the download.

## Features
- Download YouTube videos in up to 720p resolution.
- Extract audio from YouTube videos and save as MP3.
- Simple graphical user interface (GUI) using Tkinter.
- Choose the download location on your machine.
  
## Requirements
- Python 3.x
- The following Python libraries:
  - `yt-dlp`: You can install it using `pip install yt-dlp`.
  - `Tkinter`: It is usually pre-installed with Python, but if not, you can install it via your package manager.
- [FFmpeg](https://ffmpeg.org/download.html): Required for audio extraction and merging video/audio files.
  - Make sure to download and set the path to FFmpeg correctly (add its bin folder to the environment variables, and update the path in the code as needed).

## How to Use

### Method 1: Running the Python script directly

1. Clone the repository or download the script file.
2. Make sure the required libraries are installed:

   pip install yt-dlp

3 Install FFmpeg and set the path in the script (C:/ffmpeg).
4 Run the Python script:

python youtube1.py


###Method 2: Running the executable
1. If you've already created an executable using tools like PyInstaller, you can run it by double-clicking the youtube1.exe file located in the dist folder.
2. The GUI will open, allowing you to input a YouTube URL and choose whether to download the video or audio.

###How It Works
- 1. Provide a YouTube URL: Enter the YouTube URL you wish to download.
- 2. Choose a destination: Use the "Browse" button to select the folder where you want the downloaded file to be saved.
- 3. Download Video or Audio:
-  Click "Download Videos" to download the video file (in MP4 format).
- Click "Download Audio" to download only the audio (in MP3 format).


- 4. After downloading, a success message will pop up indicating the location of the downloaded file.

###FFmpeg Installation
This script uses FFmpeg to handle audio extraction and video/audio merging. To install FFmpeg:
1. Download FFmpeg from the official website: https://ffmpeg.org/download.html
2. Unzip the file and move it to a folder on your computer, e.g., C:\ffmpeg.
3. Add C:\ffmpeg\bin to your system's environment variables (so it's accessible from anywhere).
4. Update the ffmpeg_location in the script to point to your FFmpeg installation.

###Example
1. Enter the YouTube URL in the text field.
2. Select a destination folder for the download.
3. Click either "Download Videos" or "Download Audio."
4. Your file will be saved in the specified folder.

###Notes
- If there is any error (e.g., invalid URL or issues with downloading), an error message will be displayed.
- The program will only download videos in a maximum of 720p resolution.


###Screenshots
![audio-video-dl](https://github.com/user-attachments/assets/25a3d80b-175e-4af8-b3bf-8ce7b1199901)


