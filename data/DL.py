import os
from PyQt5.QtCore import QThread, pyqtSignal
from typing import Union
import yt_dlp
from yt_dlp import YoutubeDL



def time_to_str(time: Union[int, float]):
    time = int(round(time, 0))
    second = time % 60
    minute = int(time / 60 % 60)
    hour = int(time / 3600)
    return f"{hour:02d}:{minute:02d}:{second:02d}"


class DL_Thread(QThread):
    result_sig = pyqtSignal(list)
    error_sig = pyqtSignal(str)
    prog_sig = pyqtSignal(dict)

    def __init__(self, url: str, ytdl_opt: dict, download: bool = False, parent = None):
        super().__init__(parent)
        self.url = url
        self.ytdl_opt = ytdl_opt
        self.ytdl_opt["progress_hooks"] = [self.hook_signal]
        self.download = download
        # self.ytdl_opt["listformats"] = True

    def run(self):
        try:
            with YoutubeDL(self.ytdl_opt) as ytdl:
                info = ytdl.extract_info(self.url, download = self.download)
        except yt_dlp.utils.DownloadError as e:
            self.error_sig.emit(e.args[0])
        except:
            print("bbbbbbbbbbbbbb")
        else:
            res_list = []
            if "entries" in info.keys():
                for entry in info["entries"]:
                    res_list.append(entry["title"])
            else:
                res_list.append(info["title"])
            self.result_sig.emit(res_list)
    
    def hook_signal(self, d: dict):
        pct = float(d["_percent_str"].split("%")[0][-5:].split(" ")[-1])
        name = os.path.split(d["filename"])[-1]
        name = os.path.splitext(name)[0]
        info = {
                "status": d["status"],
                "name": name,
                "pct": pct,
                "ela": time_to_str(d["elapsed"])
               }
        if "eta" in d.keys():
            info["eta"] = time_to_str(d["eta"])
        self.prog_sig.emit(info)