from DL import Search_Thread
import json
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        with open("./config/basic.cfg", "r") as cfg:
            self.config = json.load(cfg)
        self.config["ytdl"]["outtmpl"] = os.path.join(self.config["save_dir"],
                                                      self.config["outtmpl"])
        self.ui.save_dir_display.setText(self.config["save_dir"])
        self.ui.download_bar.setValue(0)
        self.setup_control()

    def setup_control(self):
        self.ui.search_button.clicked.connect(self.search_clicked)
        self.ui.save_dir_button.clicked.connect(self.open_dir)
    
    def reverse_button_stat(self):
        reverse_stat = not self.ui.search_button.isEnabled()
        self.ui.search_button.setEnabled(reverse_stat)
        self.ui.download_button.setEnabled(reverse_stat)
        self.ui.save_dir_button.setEnabled(reverse_stat)
    
    def search_clicked(self):
        self.url = self.ui.input_url.text()
        self.search_thread = Search_Thread(self.url, self.config["ytdl"])
        self.search_thread.started.connect(self.reverse_button_stat)
        self.search_thread.result_sig.connect(self.update_result_list)
        self.search_thread.finished.connect(self.reverse_button_stat)
        self.search_thread.start()
    
    def update_result_list(self, result: list):
        self.ui.result_list_box.setTitle(f"Found Video - {len(result)} total")
        self.ui.result_list.clear()
        self.ui.result_list.addItems(result)
    
    def open_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "Open folder",
                                                    self.config["save_dir"])
        if dir_path != "":
            self.config["save_dir"] = dir_path
            self.config["ytdl"]["outtmpl"] = os.path.join(self.config["save_dir"],
                                                          self.config["outtmpl"])
            self.ui.save_dir_display.setText(dir_path)