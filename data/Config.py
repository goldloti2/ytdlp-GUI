import json
import os



class Config():
    def __init__(self, config_path: str):
        self.__config_path = config_path
        self.load_config()
    
    def load_config(self):
        with open(self.__config_path, "r") as f:
            self.__json_file = json.load(f)

    def save_config(self):
        with open(self.__config_path, "w") as f:
            json.dump(self.__json_file, f)
    
    def get_ytdl(self) -> dict:
        ytdl = self.__json_file["ytdl"]
        ytdl["outtmpl"] = os.path.join(self.__json_file["save_dir"],
                                       self.__json_file["outtmpl"])
        return ytdl
    
    def set_save_dir(self, save_dir: str):
        self.__json_file["save_dir"] = save_dir
    
    def get_save_dir(self) -> str:
        return self.__json_file["save_dir"]