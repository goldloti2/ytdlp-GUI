import Config
from DL import Search_Thread
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.config = Config.Config("./config/basic.cfg")
        self.init_fillin()
        self.setup_control()
    
    def init_fillin(self):
        self.ui.save_dir_line.setText(self.config.get_save_dir())

    def setup_control(self):
        self.ui.search_btn.clicked.connect(self.search_clicked)
        self.ui.save_dir_btn.clicked.connect(self.save_dir_clicked)
        self.ui.vid_btn_grp.buttonToggled.connect(self.vid_grp_toggled)
        self.ui.aud_btn_grp.buttonToggled.connect(self.aud_grp_toggled)
    
    def search_clicked(self):
        self.url = self.ui.url_line.text()
        self.search_thread = Search_Thread(self.url, self.config.get_ytdl())
        self.search_thread.started.connect(self.reverse_button_stat)
        self.search_thread.result_sig.connect(self.update_res_list)
        self.search_thread.finished.connect(self.reverse_button_stat)
        self.search_thread.start()
    
    def save_dir_clicked(self):
        dir_path = QFileDialog.getExistingDirectory(self,
                                                    "Open folder",
                                                    self.config.get_save_dir())
        if dir_path != "":
            self.config.set_save_dir(dir_path)
            self.ui.save_dir_line.setText(dir_path)
    
    def vid_grp_toggled(self, btn: QtWidgets.QRadioButton):
        if not btn.isChecked():
            return
        if btn.objectName() == "vid_none_rad" and self.ui.aud_none_rad.isChecked():
            self.ui.aud_best_rad.setChecked(True)
        print(btn.objectName())
    
    def aud_grp_toggled(self, btn: QtWidgets.QRadioButton):
        if not btn.isChecked():
            return
        if btn.objectName() == "aud_none_rad" and self.ui.vid_none_rad.isChecked():
            self.ui.vid_best_rad.setChecked(True)
        print(btn.objectName())
    
    def reverse_button_stat(self):
        reverse_stat = not self.ui.search_btn.isEnabled()
        self.ui.search_btn.setEnabled(reverse_stat)
        self.ui.dl_btn.setEnabled(reverse_stat)
        self.ui.save_dir_btn.setEnabled(reverse_stat)
    
    def update_res_list(self, result: list):
        self.ui.res_list_box.setTitle(f"Found Video - {len(result)} total")
        self.ui.res_list.clear()
        self.ui.res_list.addItems(result)