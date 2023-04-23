import json
import os



class Config():
    def __init__(self, config_path: str):
        self.__config_path = config_path
        self.load_config()
    
    def load_config(self):
        with open(self.__config_path, "r") as f:
            self.__json = json.load(f)

    def save_config(self):
        with open(self.__config_path, "w") as f:
            json.dump(self.__json, f)
    
    def get_ytdl(self) -> dict:
        ytdl = self.__json["ytdl"]
        ytdl["outtmpl"] = os.path.join(self.__json["save_dir"],
                                       self.__json["outtmpl"])
        # if self.__json["vid_f"] == "":
        #     ytdl["format"] = self.__json["vid_f"] + "+" + self.__json["aud_f"]
        # vid = self.__json["vid_f"]
        # aud = self.__json["aud_f"]
        # if vid != "" and aud != "":
        #     ytdl["format"] = 1
        return ytdl
    
    def set_save_dir(self, save_dir: str):
        self.__json["save_dir"] = save_dir
    
    def get_save_dir(self) -> str:
        return self.__json["save_dir"]