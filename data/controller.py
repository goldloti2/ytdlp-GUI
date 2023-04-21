import json
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        with open("./config/basic.cfg", "r") as cfg:
            self.config = json.load(cfg)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.ui.search_button.clicked.connect(self.search_clicked)
        
        self.ui.save_dir_display.setText(self.config["last_save_dir"])
        self.ui.save_dir_button.clicked.connect(self.open_dir)
    
    def search_clicked(self):
        msg = self.ui.input_url.text()
        self.ui.result_list.insertPlainText(msg + "\n")
    
    def open_dir(self):
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "Open folder",
                                                    self.config["last_save_dir"])
        if dir_path != "":
            self.config["last_save_dir"] = dir_path
            self.ui.save_dir_display.setText(dir_path)