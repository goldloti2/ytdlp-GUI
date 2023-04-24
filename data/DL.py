from PyQt5.QtCore import QThread, pyqtSignal
import yt_dlp
from yt_dlp import YoutubeDL



class DL_Thread(QThread):
    result_sig = pyqtSignal(list)
    error_sig = pyqtSignal(str)

    def __init__(self, url: str, ytdl_opt: dict, download: bool = False, parent = None):
        super().__init__(parent)
        self.url = url
        self.ytdl_opt = ytdl_opt
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