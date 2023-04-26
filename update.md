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
  - progress hooks don't work when downloading niconico video
  - long video name may stretch window

2023/04/25 - 3

- download button is disabled until the first search done
- option buttons won't be disabled during searching and downloading

2023/04/25 - 4

- add universal logger and ytdl logger

2023/04/25 - 5

- minus change to time to string

2023/04/26

- tab sequence change
- buttons can be pressed with enter key
