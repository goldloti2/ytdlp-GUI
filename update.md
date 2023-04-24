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
