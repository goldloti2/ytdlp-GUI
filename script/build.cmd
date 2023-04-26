pyinstaller -F -n VDlr -i .\data\icon.ico .\data\main.py
mkdir .\dist\config
mkdir .\dist\data
copy .\config\basic.cfg .\dist\config\
copy .\data\icon.ico .\dist\data\
copy .\data\ffmpeg.exe .\dist\data\
cd dist
zip -r .\VDlr_v1_0_win_x86_64.zip .\config .\data .\VDlr.exe