# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'data\UI\mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalGroupBox.setFlat(True)
        self.horizontalGroupBox.setCheckable(False)
        self.horizontalGroupBox.setObjectName("horizontalGroupBox")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalGroupBox)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.url_line = QtWidgets.QLineEdit(self.horizontalGroupBox)
        self.url_line.setObjectName("url_line")
        self.horizontalLayout_4.addWidget(self.url_line)
        self.search_btn = QtWidgets.QPushButton(self.horizontalGroupBox)
        self.search_btn.setAutoDefault(True)
        self.search_btn.setFlat(False)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_4.addWidget(self.search_btn)
        self.horizontalLayout_4.setStretch(0, 6)
        self.horizontalLayout_4.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox)
        self.res_list_box = QtWidgets.QGroupBox(self.centralwidget)
        self.res_list_box.setFlat(False)
        self.res_list_box.setObjectName("res_list_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.res_list_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.res_list = QtWidgets.QListWidget(self.res_list_box)
        self.res_list.setObjectName("res_list")
        self.verticalLayout_3.addWidget(self.res_list)
        self.format_table = QtWidgets.QTableWidget(self.res_list_box)
        self.format_table.setObjectName("format_table")
        self.format_table.setColumnCount(0)
        self.format_table.setRowCount(0)
        self.verticalLayout_3.addWidget(self.format_table)
        self.verticalLayout_2.addWidget(self.res_list_box)
        self.horizontalGroupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.horizontalGroupBox_2.setFlat(False)
        self.horizontalGroupBox_2.setObjectName("horizontalGroupBox_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.horizontalGroupBox_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.aud_best_rad = QtWidgets.QRadioButton(self.horizontalGroupBox_2)
        self.aud_best_rad.setObjectName("aud_best_rad")
        self.aud_btn_grp = QtWidgets.QButtonGroup(MainWindow)
        self.aud_btn_grp.setObjectName("aud_btn_grp")
        self.aud_btn_grp.addButton(self.aud_best_rad)
        self.gridLayout.addWidget(self.aud_best_rad, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.vid_best_rad = QtWidgets.QRadioButton(self.horizontalGroupBox_2)
        self.vid_best_rad.setObjectName("vid_best_rad")
        self.vid_btn_grp = QtWidgets.QButtonGroup(MainWindow)
        self.vid_btn_grp.setObjectName("vid_btn_grp")
        self.vid_btn_grp.addButton(self.vid_best_rad)
        self.gridLayout.addWidget(self.vid_best_rad, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.save_dir_btn = QtWidgets.QToolButton(self.horizontalGroupBox_2)
        self.save_dir_btn.setObjectName("save_dir_btn")
        self.gridLayout.addWidget(self.save_dir_btn, 0, 5, 1, 1)
        self.save_dir_line = QtWidgets.QLineEdit(self.horizontalGroupBox_2)
        self.save_dir_line.setEnabled(True)
        self.save_dir_line.setReadOnly(True)
        self.save_dir_line.setObjectName("save_dir_line")
        self.gridLayout.addWidget(self.save_dir_line, 0, 1, 1, 4)
        self.ck_file_btn = QtWidgets.QToolButton(self.horizontalGroupBox_2)
        self.ck_file_btn.setCheckable(False)
        self.ck_file_btn.setObjectName("ck_file_btn")
        self.gridLayout.addWidget(self.ck_file_btn, 3, 5, 1, 1)
        self.ck_file_line = QtWidgets.QLineEdit(self.horizontalGroupBox_2)
        self.ck_file_line.setReadOnly(True)
        self.ck_file_line.setClearButtonEnabled(False)
        self.ck_file_line.setObjectName("ck_file_line")
        self.gridLayout.addWidget(self.ck_file_line, 3, 1, 1, 4)
        self.ret_def_btn = QtWidgets.QPushButton(self.horizontalGroupBox_2)
        self.ret_def_btn.setObjectName("ret_def_btn")
        self.gridLayout.addWidget(self.ret_def_btn, 4, 1, 1, 1)
        self.ck_check = QtWidgets.QCheckBox(self.horizontalGroupBox_2)
        self.ck_check.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.ck_check.setObjectName("ck_check")
        self.gridLayout.addWidget(self.ck_check, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.horizontalGroupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.vid_none_rad = QtWidgets.QRadioButton(self.horizontalGroupBox_2)
        self.vid_none_rad.setObjectName("vid_none_rad")
        self.vid_btn_grp.addButton(self.vid_none_rad)
        self.gridLayout.addWidget(self.vid_none_rad, 1, 2, 1, 1)
        self.vid_custom_line = QtWidgets.QLineEdit(self.horizontalGroupBox_2)
        self.vid_custom_line.setObjectName("vid_custom_line")
        self.gridLayout.addWidget(self.vid_custom_line, 1, 4, 1, 1)
        self.vid_custom_rad = QtWidgets.QRadioButton(self.horizontalGroupBox_2)
        self.vid_custom_rad.setObjectName("vid_custom_rad")
        self.vid_btn_grp.addButton(self.vid_custom_rad)
        self.gridLayout.addWidget(self.vid_custom_rad, 1, 3, 1, 1)
        self.aud_custom_rad = QtWidgets.QRadioButton(self.horizontalGroupBox_2)
        self.aud_custom_rad.setObjectName("aud_custom_rad")
        self.aud_btn_grp.addButton(self.aud_custom_rad)
        self.gridLayout.addWidget(self.aud_custom_rad, 2, 3, 1, 1)
        self.aud_none_rad = QtWidgets.QRadioButton(self.horizontalGroupBox_2)
        self.aud_none_rad.setObjectName("aud_none_rad")
        self.aud_btn_grp.addButton(self.aud_none_rad)
        self.gridLayout.addWidget(self.aud_none_rad, 2, 2, 1, 1)
        self.aud_custom_line = QtWidgets.QLineEdit(self.horizontalGroupBox_2)
        self.aud_custom_line.setObjectName("aud_custom_line")
        self.gridLayout.addWidget(self.aud_custom_line, 2, 4, 1, 1)
        self.save_def_btn = QtWidgets.QPushButton(self.horizontalGroupBox_2)
        self.save_def_btn.setObjectName("save_def_btn")
        self.gridLayout.addWidget(self.save_def_btn, 4, 4, 1, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.horizontalGroupBox_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.dl_btn = QtWidgets.QPushButton(self.centralwidget)
        self.dl_btn.setObjectName("dl_btn")
        self.horizontalLayout_6.addWidget(self.dl_btn)
        self.dl_bar = QtWidgets.QProgressBar(self.centralwidget)
        self.dl_bar.setProperty("value", 0)
        self.dl_bar.setObjectName("dl_bar")
        self.horizontalLayout_6.addWidget(self.dl_bar)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 6)
        self.verticalLayout_2.setStretch(2, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.horizontalGroupBox.setTitle(_translate("MainWindow", "Download URL"))
        self.search_btn.setText(_translate("MainWindow", "Search"))
        self.res_list_box.setTitle(_translate("MainWindow", "Found Video"))
        self.horizontalGroupBox_2.setTitle(_translate("MainWindow", "Save Option"))
        self.aud_best_rad.setText(_translate("MainWindow", "Best"))
        self.label_2.setText(_translate("MainWindow", "Video Option :"))
        self.vid_best_rad.setText(_translate("MainWindow", "Best"))
        self.label.setText(_translate("MainWindow", "Save Folder :"))
        self.save_dir_btn.setText(_translate("MainWindow", "..."))
        self.ck_file_btn.setText(_translate("MainWindow", "..."))
        self.ret_def_btn.setText(_translate("MainWindow", "Return To Default"))
        self.ck_check.setText(_translate("MainWindow", "Cookie :"))
        self.label_3.setText(_translate("MainWindow", "Audio Option :"))
        self.vid_none_rad.setText(_translate("MainWindow", "None"))
        self.vid_custom_rad.setText(_translate("MainWindow", "Specific :"))
        self.aud_custom_rad.setText(_translate("MainWindow", "Specific :"))
        self.aud_none_rad.setText(_translate("MainWindow", "None"))
        self.save_def_btn.setText(_translate("MainWindow", "Save As Default"))
        self.dl_btn.setText(_translate("MainWindow", "Download"))
