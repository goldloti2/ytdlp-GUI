import Config
from DL import DL_Thread
import json
import logging
import os
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from UI import Ui_MainWindow

class MainWindow_controller(QtWidgets.QMainWindow):
    def __init__(self, logger: str = "logger"):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.logger = logging.getLogger(logger)
        self.config = Config.Config("./config/basic.cfg", logger)
        self.init_fillin()
        self.setup_control()
        self.f_tbl_name = []
        for i in range(self.ui.format_table.columnCount()):
            self.f_tbl_name.append(self.ui.format_table.horizontalHeaderItem(i).text())
    
    def init_fillin(self):
        self.ui.vid_custom_line.clear()
        self.ui.aud_custom_line.clear()
        self.config.load_config()
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
        self.ui.ck_check.setChecked(False)
        self.ui.ck_file_line.setEnabled(False)
        self.ui.ck_file_line.clear()
        self.ui.ck_file_btn.setEnabled(False)
        self.ui.dl_btn.setEnabled(False)

    def setup_control(self):
        self.ui.url_line.returnPressed.connect(self.ui.search_btn.click)
        self.ui.search_btn.clicked.connect(self.search_clicked)
        self.ui.res_list.itemSelectionChanged.connect(self.res_list_changed)
        self.ui.save_dir_btn.clicked.connect(self.save_dir_clicked)
        self.ui.vid_btn_grp.buttonToggled.connect(self.vid_grp_toggled)
        self.ui.aud_btn_grp.buttonToggled.connect(self.aud_grp_toggled)
        self.ui.vid_custom_rad.toggled.connect(self.vid_custom_toggled)
        self.ui.aud_custom_rad.toggled.connect(self.aud_custom_toggled)
        self.ui.vid_custom_line.textChanged.connect(self.config.set_vid_fmt)
        self.ui.aud_custom_line.textChanged.connect(self.config.set_aud_fmt)
        self.ui.ck_check.clicked.connect(self.ck_check_clicked)
        self.ui.ck_file_btn.clicked.connect(self.ck_file_clicked)
        self.ui.ret_def_btn.clicked.connect(self.init_fillin)
        self.ui.save_def_btn.clicked.connect(self.config.save_config)
        self.ui.dl_btn.clicked.connect(self.dl_clicked)
    
    def search_clicked(self):
        self.url = self.ui.url_line.text()
        self.logger.info("search %s", self.url)
        self.search_thread = DL_Thread(self.url, self.config.get_ytdl())
        self.search_thread.started.connect(self.reverse_button_stat)
        self.search_thread.finished.connect(self.reverse_button_stat)
        self.search_thread.result_sig.connect(self.update_res_list)
        self.search_thread.error_sig.connect(self.error_msgbox)
        self.search_thread.start()
    
    def res_list_changed(self):
        res_format = self.res_formats[self.ui.res_list.currentRow()]
        self.ui.format_table.setRowCount(len(res_format))
        for i, res in enumerate(res_format):
            for j, name in enumerate(self.f_tbl_name):
                new_item = QtWidgets.QTableWidgetItem(res[name])
                self.ui.format_table.setItem(i, j, new_item)
                if name == "note":
                    new_item.setToolTip(res[name])
        self.ui.format_table.resizeColumnsToContents()
        self.logger.info(
            "format table change, video id: (%d), availabe formats: (%d)",
            self.ui.res_list.currentRow(), len(res_format))
        self.logger.debug("\n%s", json.dumps(res_format, indent = 4))
    
    def save_dir_clicked(self):
        self.logger.info("save folder button clicked")
        dir_path = QFileDialog.getExistingDirectory(
            self, "Open folder", self.config.get_save_dir())
        if dir_path != "":
            self.config.set_save_dir(dir_path)
            self.ui.save_dir_line.setText(dir_path)
    
    def vid_grp_toggled(self, btn: QtWidgets.QRadioButton):
        if not btn.isChecked():
            return
        self.logger.info("video format radio clicked: %s", btn.objectName())
        if btn.objectName() == "vid_none_rad" and self.ui.aud_none_rad.isChecked():
            self.ui.aud_best_rad.setChecked(True)
        if btn.objectName() == "vid_custom_rad":
            self.config.set_vid_fmt(self.ui.vid_custom_line.text())
        else:
            self.config.set_vid_fmt(btn.objectName())
    
    def aud_grp_toggled(self, btn: QtWidgets.QRadioButton):
        if not btn.isChecked():
            return
        self.logger.info("audio format radio clicked: %s", btn.objectName())
        if btn.objectName() == "aud_none_rad" and self.ui.vid_none_rad.isChecked():
            self.ui.vid_best_rad.setChecked(True)
        if btn.objectName() == "aud_custom_rad":
            self.config.set_aud_fmt(self.ui.aud_custom_line.text())
        else:
            self.config.set_aud_fmt(btn.objectName())
    
    def vid_custom_toggled(self):
        self.ui.vid_custom_line.setEnabled(self.ui.vid_custom_rad.isChecked())
    
    def aud_custom_toggled(self):
        self.ui.aud_custom_line.setEnabled(self.ui.aud_custom_rad.isChecked())
    
    def ck_check_clicked(self):
        if self.ui.ck_check.isChecked():
            self.logger.info("check cookie checkbox")
            self.ui.ck_file_line.setEnabled(True)
            self.ui.ck_file_btn.setEnabled(True)
            self.config.set_cookie(self.ui.ck_file_line.text())
        else:
            self.logger.info("uncheck cookie checkbox")
            self.ui.ck_file_line.setEnabled(False)
            self.ui.ck_file_btn.setEnabled(False)
            self.config.set_cookie("")
    
    def ck_file_clicked(self):
        self.logger.info("cookie file button clicked")
        file_path, file_type = QFileDialog.getOpenFileName(
            self, "Open cookie file", ".")
        if file_path != "":
            self.config.set_cookie(file_path)
            self.ui.ck_file_line.setText(file_path)
    
    def dl_clicked(self):
        self.logger.info("download %s", self.url)
        self.ui.dl_bar.setValue(0)
        self.ui.ela_lbl.clear()
        self.ui.eta_lbl.clear()
        self.dl_thread = DL_Thread(self.url, self.config.get_ytdl(), True)
        self.dl_thread.started.connect(self.reverse_button_stat)
        self.dl_thread.finished.connect(self.reverse_button_stat)
        self.dl_thread.prog_sig.connect(self.change_bar_stat)
        self.search_thread.error_sig.connect(self.error_msgbox)
        self.dl_thread.start()
    
    def change_bar_stat(self, info: dict):
        if info["status"] == "downloading":
            self.ui.dl_bar.setValue(info["pct"])
            self.ui.dl_name_lbl.setText(info["name"])
            self.ui.ela_lbl.setText(info["ela"])
            self.ui.eta_lbl.setText("ETA: " + info["eta"])
        elif info["status"] == "finished":
            self.ui.dl_bar.setValue(info["pct"])
            self.ui.ela_lbl.setText(info["ela"])
            self.ui.eta_lbl.setText("finished")

    def reverse_button_stat(self):
        reverse_stat = not self.ui.search_btn.isEnabled()
        self.ui.search_btn.setEnabled(reverse_stat)
        if self.ui.res_list.count() != 0:
            self.ui.dl_btn.setEnabled(reverse_stat)
    
    def update_res_list(self, result: list):
        self.logger.info("found video: (%d)", len(result[0]))
        self.logger.debug("\n%s", json.dumps(result[0], indent = 4))
        self.res_formats = result[1]
        self.ui.res_list_box.setTitle(f"Found Video - {len(result[0])} total")
        self.ui.res_list.clear()
        self.ui.res_list.addItems(result[0])
        self.ui.res_list.setCurrentRow(0)
    
    def error_msgbox(self, msg: str):
        mbox = QMessageBox.critical(self.ui.centralwidget, "Error when downloading", msg)