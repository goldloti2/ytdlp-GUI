# Update

2023/04/21

- initial commit
- basic GUI layout

2023/04/22

- new: search url and list all video name

2023/04/23 - 1

- renew UI layout
  - add format table and more download options
- shortening object names (button -> btn, etc.)

2023/04/23 - 2

- pack config into `Config` class

2023/04/23 - 3

- connect video/audio option signals to slots, not implemented
- remove worst video/audio option

2023/04/23 - 4

- video/audio options now workable, and can preselect by default config

2023/04/23 - 5

- add video/audio format specific options, and `line edit` objects enable when options are checked

2023/04/24 - 1

- Return To Default and Save As Default buttons now work
- fix custom formats not passed correctly

2023/04/24 - 2

- Download button now works

2023/04/24 - 3

- cookies checkbox enables/disables cookies file input
- cookies file browser fills in path automatically
- Return To Default clears all texts in option

2023/04/24 - 4

- cookie path can be passed to yt-dlp
- save folder and cookie line change to read only

2023/04/24 - 5

- download progress links to progress bar, file name, elapsed time and ETA

2023/04/25 - 1

- format table shows available formats of the chosen video

2023/04/25 - 2

- fix Facebook video download error (missing keys in progress hooks)
- known bug:
  - progress hooks don't work when downloading niconico video *(2023/04/25 note: package-site bug)*
  - long video name may stretch window *(fixed in 2023/04/26-5)*

2023/04/25 - 3

- download button is disabled until the first search done
- option buttons won't be disabled during searching and downloading

2023/04/25 - 4

- add universal logger and ytdl logger

2023/04/25 - 5

- minus change to time to string

2023/04/26 - 1

- tab sequence change
- buttons can be pressed with enter key

2023/04/26 - 2

- add logger
- code style improve
- known bug:
  - clicking Return To Default when custom video/audio button is checked, none video/audio button is checked rather than the default setting *(fixed in 2023/04/26-3)*

2023/04/26 - 3

- fix bug: unexpected behavior of Return To Default button *(bug in 2023/04/26-2)*

2023/04/26 - 4

- add download error message box
- remove ANSI Escape Code in messages from yt-dlp to UI

2023/04/26 - 5

- add icon
- change title to "Video Downloader"
- fix bug: long video name may stretch window horizontally, though it may take space above it *(bug in 2023/04/25-2)*

2023/04/26 - 6 v1.0

- v1.0 release (only for Windows x86-64)
- add build command

2023/04/26 - 7

- update README.md
- set more options in build.cmd

2023/04/26 - 8 v1.0.1

- fix bug: Download button should only be enabled after a successful search
- update How to Use Cookies in README.md

2023/08/20 v1.0.2023.7.6

- update yt-dlp to v2023.7.6
- add indep_script for running build script outside

2023/12/12 v1.0.2023.11.16

- update yt-dlp to v2023.11.16

2024/03/05 v1.0.2023.12.30

- update yt-dlp to v2023.12.30

2025/02/05 v1.0.2024.10.22

- update yt-dlp to v2024.10.22
