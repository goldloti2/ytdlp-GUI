from PyQt5.QtCore import QThread, pyqtSignal
import yt_dlp
from yt_dlp import YoutubeDL



class Search_Thread(QThread):
    result_sig = pyqtSignal(list)
    error_sig = pyqtSignal(str)

    def __init__(self, url: str, ytdl_opt: dict, parent = None):
        super().__init__(parent)
        self.url = url
        self.ytdl_opt = ytdl_opt
        # self.ytdl_opt["listformats"] = True

    def run(self):
        try:
            with YoutubeDL(self.ytdl_opt) as ytdl:
                info = ytdl.extract_info(self.url, download = False)
        except yt_dlp.utils.DownloadError as e:
            self.error_sig.emit(e.args[0])
        except:
            print("bbbbbbbbbbbbbb")
        else:
            res_list = []
            if "entries" in info.keys():
                for entry in info["entries"]:
                    res_list.append(f"{entry['title']}.{entry['ext']}")
            else:
                res_list.append(f"{info['title']}.{info['ext']}")
            self.result_sig.emit(res_list)