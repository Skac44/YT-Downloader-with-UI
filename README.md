# YouTube Downloader with GUI
This is a simple and user-friendly Youtube Video/Audio downloader with a GUI to download YouTube videos as MP4 or extract audio as MP3 files with the help of yt-dlp command line interface

## Features
- Download audio only (MP3 format)
- Download video + audio (MP4 format)
- Choose custom download directory
- Clean graphical interface
- Built-in FFmpeg support for format conversion

## System Requirements
- OS (if you want to download directly, any version can be created by compiling the code on your machine to an executable): Windows (tested on Windows 10/11)
- Python: 3.8+
- FFmpeg: Required for audio conversion (must be in system PATH)

## Dependencies: 
- See requirements.txt

## Usage
1. Paste YouTube URL in the input field

2. Select output format (MP3 or MP4)

3. Choose download location (default: Downloads folder)

4. Click the "Download" button

## Technical Details
- Backend: Uses yt-dlp (YouTube-DL fork) for downloading

- Audio Conversion: FFmpeg for MP3 conversion

- GUI Framework: Tkinter (Python standard library)

- Packaging: Supports PyInstaller for executable creation

## Limitations and Future upgrades
- Downloading from a playlist may result in the download of the full playlist
- No Loading Bar to inform user of the download state
- Videos may be downloaded with metadata date from the original video (ex. If a video is uploaded in 2007 it will download the file with the upload date)


# Legal Notice
**Important**: This software is intended for:
- Downloading content you have rights to
- Personal archival of publicly available videos
- Educational purposes only
By using this software, you agree to comply with YouTube's Terms of Service and all applicable copyright laws. I am not responsible for misuse of this tool.
