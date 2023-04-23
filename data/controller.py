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
        vid_fmt = self.config.get_vid_fmt()
        if vid_fmt == "vid_best_rad":
            self.ui.vid_best_rad.setChecked(True)
        elif vid_fmt == "vid_none_rad":
            self.ui.vid_none_rad.setChecked(True)
        else:
            self.ui.vid_custom_rad.setChecked(True)
            self.ui.vid_custom_line.setText(vid_fmt)
        aud_fmt = self.config.get_aud_fmt()
        if aud_fmt == "aud_best_rad":
            self.ui.aud_best_rad.setChecked(True)
        elif aud_fmt == "aud_none_rad":
            self.ui.aud_none_rad.setChecked(True)
        else:
            self.ui.aud_custom_rad.setChecked(True)
            self.ui.aud_custom_line.setText(aud_fmt)
        self.vid_custom_toggled()
        self.aud_custom_toggled()

    def setup_control(self):
        self.ui.search_btn.clicked.connect(self.search_clicked)
        self.ui.save_dir_btn.clicked.connect(self.save_dir_clicked)
        self.ui.vid_btn_grp.buttonToggled.connect(self.vid_grp_toggled)
        self.ui.aud_btn_grp.buttonToggled.connect(self.aud_grp_toggled)
        self.ui.vid_custom_rad.toggled.connect(self.vid_custom_toggled)
        self.ui.aud_custom_rad.toggled.connect(self.aud_custom_toggled)
    
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
        self.config.set_vid_fmt(btn.objectName())
    
    def aud_grp_toggled(self, btn: QtWidgets.QRadioButton):
        if not btn.isChecked():
            return
        if btn.objectName() == "aud_none_rad" and self.ui.vid_none_rad.isChecked():
            self.ui.vid_best_rad.setChecked(True)
        self.config.set_aud_fmt(btn.objectName())
    
    def vid_custom_toggled(self):
        self.ui.vid_custom_line.setEnabled(self.ui.vid_custom_rad.isChecked())
    
    def aud_custom_toggled(self):
        self.ui.aud_custom_line.setEnabled(self.ui.aud_custom_rad.isChecked())
    
    def reverse_button_stat(self):
        reverse_stat = not self.ui.search_btn.isEnabled()
        self.ui.search_btn.setEnabled(reverse_stat)
        self.ui.dl_btn.setEnabled(reverse_stat)
        self.ui.save_dir_btn.setEnabled(reverse_stat)
    
    def update_res_list(self, result: list):
        self.ui.res_list_box.setTitle(f"Found Video - {len(result)} total")
        self.ui.res_list.clear()
        self.ui.res_list.addItems(result)