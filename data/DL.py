import json
import logging
import os
from PyQt5.QtCore import QThread, pyqtSignal
from typing import Union
import yt_dlp
from yt_dlp import YoutubeDL



def time_to_str(time: Union[int, float]):
    if not (isinstance(time, int) or isinstance(time, float)):
        return "???"
    time = int(round(time, 0))
    second = time % 60
    minute = time // 60 % 60
    hour = time // 3600
    return f"{hour:02d}:{minute:02d}:{second:02d}"

def valid(d: dict, k: str):
    return k in d.keys() and d[k] != None


class DL_Thread(QThread):
    result_sig = pyqtSignal(list)
    error_sig = pyqtSignal(str)
    prog_sig = pyqtSignal(dict)

    def __init__(
            self, url: str, ytdl_opt: dict,
            download: bool = False, logger: str = "logger", parent = None):
        super().__init__(parent)
        self.url = url
        self.ytdl_opt = ytdl_opt
        self.ytdl_opt["logger"] = logging.getLogger("ytdl")
        self.ytdl_opt["progress_hooks"] = [self.hook_signal]
        self.download = download
        self.logger = logging.getLogger(logger)
        # self.ytdl_opt["listformats"] = True

    def run(self):
        self.logger.info("stard download: %s", self.url)
        try:
            with YoutubeDL(self.ytdl_opt) as ytdl:
                info = ytdl.extract_info(self.url, download = self.download)
            res_list = [[], []]
            if "entries" in info.keys():
                for entry in info["entries"]:
                    res_list[0].append(entry["title"])
                    res_list[1].append(self.format_parse(entry["formats"]))
            else:
                res_list[0].append(info["title"])
                res_list[1].append(self.format_parse(info["formats"]))
            self.result_sig.emit(res_list)
        except yt_dlp.utils.DownloadError as e:
            self.error_sig.emit(e.args[0])
            self.logger.exception("ytdl download error")
        except Exception as e:
            self.error_sig.emit(e.args[0])
            self.logger.exception("error during download")
        self.logger.debug("download end")
    
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
    
    def format_parse(self, formats: list):
        parse = []
        for f in formats:
            p = {
                "id": f["format_id"],
                "ext": f["ext"],
                "res": f["resolution"],
                "note": "",
                "fps": "",
                "ch": "",
                "size": "",
                "vbr": "",
                "abr": "",
                "asr": ""
                }
            if valid(f, "fps"):
                p["fps"] = f"{f['fps']:.0f}"
            if valid(f, "audio_channels"):
                p["ch"] = str(f["audio_channels"])
            if valid(f, "vbr"):
                p["vbr"] = f"{f['vbr']:.0f}K"
            if valid(f, "abr"):
                p["abr"] = f"{f['abr']:.0f}K"
            if valid(f, "asr"):
                p["asr"] = f"{f['asr'] / 1000:.1f}K"
            if valid(f, "format_note"):
                p["note"] = f["format_note"]
            if valid(f, "filesize"):
                filesize = f["filesize"]
                if filesize < 1024:
                    size_str = f"{filesize}B"
                elif filesize < 1048576:
                    size_str = f"{filesize / 1024:.2f}KiB"
                elif filesize < 1073741824:
                    size_str = f"{filesize / 1048576:.2f}MiB"
                else:
                    size_str = f"{filesize / 1073741824:.2f}GiB"
                p["size"] = size_str
            parse.append(p)
        return parse