import json
import logging
import os



class Config():
    def __init__(self, config_path: str, logger: str = "logger"):
        self.__config_path = config_path
        self.logger = logging.getLogger(logger)
    
    def load_config(self):
        with open(self.__config_path, "r") as f:
            self.__json = json.load(f)
        self.__cookiefile = ""
        self.logger.info("load config")
        self.logger.debug(
            "\npath:%s\nconfig:\n%s",
            self.__config_path,
            json.dumps(self.__json, indent = 4))


    def save_config(self):
        with open(self.__config_path, "w") as f:
            json.dump(self.__json, f, indent = 4)
        self.logger.info("save config")
        self.logger.debug("\n%s", json.dumps(self.__json, indent = 4))
    
    def get_ytdl(self) -> dict:
        ytdl = self.__json["ytdl"].copy()
        ytdl["outtmpl"] = os.path.join(self.__json["save_dir"],
                                       self.__json["outtmpl"])
        if self.__json["vid_fmt"] == "":
            ytdl["format"] = self.__json["aud_fmt"]
        elif self.__json["aud_fmt"] == "":
            ytdl["format"] = self.__json["vid_fmt"]
        else:
            ytdl["format"] = f"{self.__json['vid_fmt']}+{self.__json['aud_fmt']}"
        ytdl["format"] += self.__json["def_fmt"]
        if self.__cookiefile != "":
            ytdl["cookiefile"] = self.__cookiefile
        self.logger.debug("ytdl option:\n%s", json.dumps(ytdl, indent = 4))
        return ytdl
    
    def set_save_dir(self, save_dir: str):
        self.__json["save_dir"] = save_dir
        self.logger.info("set save fodler: %s", save_dir)
    
    def get_save_dir(self) -> str:
        return self.__json["save_dir"]
    
    def set_vid_fmt(self, vid_fmt: str):
        if vid_fmt == "vid_best_rad":
            self.__json["vid_fmt"] = "bv"
        elif vid_fmt == "vid_none_rad":
            self.__json["vid_fmt"] = ""
        else:
            self.__json["vid_fmt"] = vid_fmt
        self.logger.info("set video format: %s", vid_fmt)
    
    def get_vid_fmt(self) -> str:
        if self.__json["vid_fmt"] == "bv":
            return "vid_best_rad"
        elif self.__json["vid_fmt"] == "":
            return "vid_none_rad"
        else:
            return self.__json["vid_fmt"]
    
    def set_aud_fmt(self, aud_fmt: str):
        if aud_fmt == "aud_best_rad":
            self.__json["aud_fmt"] = "ba"
        elif aud_fmt == "aud_none_rad":
            self.__json["aud_fmt"] = ""
        else:
            self.__json["aud_fmt"] = aud_fmt
        self.logger.info("set audio format: %s", aud_fmt)
    
    def get_aud_fmt(self) -> str:
        if self.__json["aud_fmt"] == "ba":
            return "aud_best_rad"
        elif self.__json["aud_fmt"] == "":
            return "aud_none_rad"
        else:
            return self.__json["aud_fmt"]
    
    def set_cookie(self, cookie: str):
        self.__cookiefile = cookie
        self.logger.info("set cookie file: %s", cookie)