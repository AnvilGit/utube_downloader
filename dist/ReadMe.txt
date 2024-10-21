
# This is the old one
1. This is the executable version of youtube video downloader.
created with pyintaller program. 
- youtube.exe, ofcourse now doesn't work as the code has changed.
only one file, so NSIS wasn't needed in this case.
- I did use NSIS to create Password Program.
- NSIS will be great for condensing Games programs.

# This is the new one - 19 July 2024 and it works
1. youtube1.exe created using pyinstaller
Steps:
1. pip install pyinstaller  # on pycharm
2. pyinstaller youtube1.py --onefile --noconsole # choose the .py file that you want to convert..--onefile flag will avoid creating multiples unnecessary folders
3. than on result we will see, build and dist folder and inside dist we have .exe file
4. if there is more than one file, e.g: main.py that have graphics, sounds folder as in game, put all folder and main.py together and zipped it and send it to yr fren or use NSIS to condensed.



The End