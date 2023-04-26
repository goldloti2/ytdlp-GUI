# yt-dlp GUI

只是個yt-dlp的GUI介面，順便當練習PyQt5

## Features (Planned)

- Download video from provided URL (if yt-dlp supported)
- Video and audio can be downloaded seperately
- Customizable download option (different resolution, etc.)
- Download with cookies if needed

## Requirement

Python 3.8 packages: (listed in requirements.txt)

- PyQt5
- yt_dlp

others:

- [ffmpeg](https://ffmpeg.org/)

## How to Run With Python

1. Install python and required packages
2. Download ffmpeg and put ffmpeg.exe into `data` folder
    - or change `ytdl: ffmpeg_location` in `config/basic.cfg` to your ffmpeg.exe
3. Run `data/main.py`

## How to Use Cookies

1. Get coockies in Netscape format. Most browsers have supported plugin such as `GET cookies.txt`
2. Choose cookies file and go
