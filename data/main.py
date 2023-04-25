from controller import MainWindow_controller
import logging
import os
from PyQt5 import QtWidgets
import sys
import time



def init_logger():
    timestamp = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    fmt = logging.Formatter('[%(asctime)s]:[%(levelname)s]:%(name)s: %(message)s')
    
    if not os.path.isdir("log"):
        os.mkdir("log")
    
    uni_logger = logging.getLogger("logger")
    uni_logger.setLevel(logging.DEBUG)
    filename = os.path.join("log", timestamp + ".log")
    fh = logging.FileHandler(filename = filename, encoding = "utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    uni_logger.addHandler(fh)

    ytdl_logger = logging.getLogger("ytdl")
    ytdl_logger.setLevel(logging.DEBUG)
    filename = os.path.join("log", timestamp + "_ytdl.log")
    fh = logging.FileHandler(filename = filename, encoding = "utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(fmt)
    ytdl_logger.addHandler(fh)

if __name__ == '__main__':
    init_logger()
    logger = logging.getLogger("logger")
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow_controller()
        window.show()
        sys.exit(app.exec_())
    except SystemExit:
        pass
    except:
        logger.exception("error")