cd ..
env\Scripts\activate &^
pyinstaller -F -n VDlr -i .\data\icon.ico -w .\data\main.py &^
env\Scripts\deactivate &^
mkdir .\dist\config &^
mkdir .\dist\data &^
copy .\config\basic.cfg .\dist\config\ &^
copy .\data\icon.ico .\dist\data\ &^
copy .\data\ffmpeg.exe .\dist\data\ &^
cd dist &^
zip -r -u .\VDlr_v1_0_2023_7_6_win_x86_64.zip .\config .\data .\VDlr.exe &^
pause &^
exit /b 0