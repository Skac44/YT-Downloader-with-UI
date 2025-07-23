import tkinter as tk
import os
import sys
from tkinter import *
import yt_dlp
from tkinter import messagebox,filedialog

#   

import ctypes #icon
myapp = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myapp)

#GUI
root = tk.Tk()
root.geometry('800x350')
root.resizable(False, False)
root.title('Youtube Downloader')
root.config(background='#B2EF9B')

def resource_path(relative_path):
    """Get the absolute path to a resource, accounting for PyInstaller."""
    try:
        # PyInstaller creates a temp folder and stores files in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def get_ffmpeg_path():
    """Get the path to ffmpeg binaries"""
    try:
        # PyInstaller creates a temp folder and stores files in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, "ffmpeg", "bin")

# Load the icon
img = PhotoImage(file=resource_path('YTIcon.png'))
root.iconphoto(False, img)

#links/paths to string
video_link = StringVar()
download_path = StringVar()
default_download_path = os.path.join(os.path.expanduser("~"), "Downloads")
download_path.set(default_download_path)

#default dropdown
selected_format = StringVar(value="MP3 (Audio Only)")


def Functionality():
    title_label = Label(root, text='Youtube Video/Audio Downloader', padx=15, pady=15, font='Arial 14', fg='black')
    title_label.grid(row=1,column=1, padx=15,pady=15, columnspan=3)

    link_label = Label(root, text='Youtube URL')
    link_label.grid(row=2,column=0, padx=15,pady=15)

    root.linktext = Entry(root, width = 40, textvariable = video_link, font = 'Arial 14')
    root.linktext.grid(row=2, column=1, padx=15,pady=15, columnspan=3)


def BrowseToLocation():
    download_directory = filedialog.askdirectory(initialdir="default_download_path", title="Save Video")
    download_path.set(download_directory) if download_directory else download_path.set(default_download_path)

def DownloadYT():
    YT_link = video_link.get()
    download_folder = download_path.get()
    selected = selected_format.get()
    ffmpeg_path = get_ffmpeg_path()

    try:
        if selected == "MP3 (Audio Only)":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
                'ffmpeg_location': ffmpeg_path,
                'postprocessor_args': ['-map_metadata', '-1', '-metadata', 'creation_time=now'],
            }

        elif selected == "MP4 (Video and Audio)":
                        ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio/best[ext=m4a]',
                'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
                'merge_output_format': 'mp4',
                'ffmpeg_location': ffmpeg_path,
                'postprocessor_args': ['-map_metadata', '-1', '-metadata', 'creation_time=now'],
            }
        
        else:
              messagebox.showerror("Error", "Invalid format!")
              return
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([YT_link])

        messagebox.showinfo("Success", f"The content has been downloaded to:\n{download_folder}")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

destination_label = Label(root, text="Selected Path: ")
destination_label.grid(row=3, column=0, padx=15,pady=15)

root.destinationtext = Entry(root, width=40, textvariable=download_path, font='Arial 14', state='readonly')
root.destinationtext.grid(row=3,column=1,padx=15,pady=15,columnspan=3)

browse_btn = Button(root, text="Browse Location", command=BrowseToLocation, width=20, bg='white', relief=GROOVE)
browse_btn.grid(row=5,column=2,padx=15,pady=15)

browse_btn = Button(root, text="Download", command=DownloadYT, width=50, bg='white', relief=GROOVE)
browse_btn.grid(row=5,column=1,padx=15,pady=15)

format_label = Label(root, text="Select Format:")
format_label.grid(row=4, column=0, padx=15, pady=15)

format_options = ["MP3 (Audio Only)", "MP4 (Video and Audio)"]
format_dropdown = OptionMenu(root, selected_format, *format_options)
format_dropdown.config(width=25, bg='white', relief=GROOVE)
format_dropdown.grid(row=4, column=1, padx=15, pady=15, columnspan=3)

Functionality()
root.mainloop()