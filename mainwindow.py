# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Games_And_Tech\QuestCalculatorClass\QCGUI\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import img_gui
from pygame import mixer

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1280, 720))
        MainWindow.setMaximumSize(QtCore.QSize(1280, 720))
        MainWindow.setStyleSheet("")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setStyleSheet("")
        self.centralWidget.setObjectName("centralWidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.stackedWidget.setMinimumSize(QtCore.QSize(1280, 720))
        self.stackedWidget.setMaximumSize(QtCore.QSize(1280, 720))
        self.stackedWidget.setObjectName("stackedWidget")
        self.file_select_page = QtWidgets.QWidget()
        self.file_select_page.setObjectName("file_select_page")
        self.background_frame = QtWidgets.QFrame(self.file_select_page)
        self.background_frame.setEnabled(True)
        self.background_frame.setGeometry(QtCore.QRect(0, 0, 1280, 720))
        self.background_frame.setStyleSheet("#background_frame {\n"
" background-image: url(:/bg/FileSelectWindowBackground.png) \n"
"}")
        self.background_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.background_frame.setLineWidth(0)
        self.background_frame.setObjectName("background_frame")
        self.FileSelectButton2 = QtWidgets.QPushButton(self.background_frame)
        self.FileSelectButton2.setGeometry(QtCore.QRect(512, 256, 256, 256))
        self.FileSelectButton2.setMinimumSize(QtCore.QSize(256, 256))
        self.FileSelectButton2.setMaximumSize(QtCore.QSize(256, 256))
        self.FileSelectButton2.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.FileSelectButton2.setFont(font)
        self.FileSelectButton2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FileSelectButton2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.FileSelectButton2.setStyleSheet("color: white;\n"
"border: 10px;\n"
"border-image: url(:/bg/border_thick_purple.png);")
        self.FileSelectButton2.setFlat(True)
        self.FileSelectButton2.setObjectName("FileSelectButton2")
        self.qc_label = QtWidgets.QLabel(self.background_frame)
        self.qc_label.setGeometry(QtCore.QRect(415, 40, 450, 64))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.qc_label.setFont(font)
        self.qc_label.setTextFormat(QtCore.Qt.RichText)
        self.qc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.qc_label.setWordWrap(False)
        self.qc_label.setObjectName("qc_label")
        self.FileSelectButton1 = QtWidgets.QPushButton(self.background_frame)
        self.FileSelectButton1.setGeometry(QtCore.QRect(128, 256, 256, 256))
        self.FileSelectButton1.setMinimumSize(QtCore.QSize(256, 256))
        self.FileSelectButton1.setMaximumSize(QtCore.QSize(256, 256))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.FileSelectButton1.setFont(font)
        self.FileSelectButton1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.FileSelectButton1.setAutoFillBackground(False)
        self.FileSelectButton1.setStyleSheet("color: white;\n"
"border: 10px;\n"
"border-image: url(:/bg/border_thick_purple.png);")
        self.FileSelectButton1.setDefault(False)
        self.FileSelectButton1.setFlat(True)
        self.FileSelectButton1.setObjectName("FileSelectButton1")
        self.pushButton_4 = QtWidgets.QPushButton(self.background_frame)
        self.pushButton_4.setGeometry(QtCore.QRect(896, 256, 256, 256))
        self.pushButton_4.setMinimumSize(QtCore.QSize(256, 256))
        self.pushButton_4.setMaximumSize(QtCore.QSize(256, 256))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("color: white;\n"
"border: 10px;\n"
"border-image: url(:/bg/border_thick_purple.png);")
        self.pushButton_4.setFlat(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.file_select_label = QtWidgets.QLabel(self.background_frame)
        self.file_select_label.setGeometry(QtCore.QRect(512, 128, 256, 48))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.file_select_label.setFont(font)
        self.file_select_label.setTextFormat(QtCore.Qt.RichText)
        self.file_select_label.setAlignment(QtCore.Qt.AlignCenter)
        self.file_select_label.setWordWrap(False)
        self.file_select_label.setObjectName("file_select_label")
        self.stackedWidget.addWidget(self.file_select_page)
        self.active_file_page = QtWidgets.QWidget()
        self.active_file_page.setEnabled(True)
        self.active_file_page.setMinimumSize(QtCore.QSize(1280, 720))
        self.active_file_page.setStyleSheet("#active_file_page {\n"
"    background-color: black\n"
"}")
        self.active_file_page.setObjectName("active_file_page")
        self.qc_tabs = QtWidgets.QTabWidget(self.active_file_page)
        self.qc_tabs.setGeometry(QtCore.QRect(256, 0, 1024, 720))
        self.qc_tabs.setMinimumSize(QtCore.QSize(1024, 720))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.qc_tabs.setFont(font)
        self.qc_tabs.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.qc_tabs.setStyleSheet("#qc_tabs::pane\n"
"{\n"
"    border: 0px;\n"
"    background: rgb(0,0,0);\n"
"}\n"
"#qc_tabs::tab-bar {\n"
"left: 24px; /* move to the right by 5px */\n"
"}\n"
"QTabBar::tab:first {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(224,224,128), stop: 0.4 rgb(224,192,96), stop: 0.5 rgb(224,224,128), stop: 1.0 rgb(224,192,96));\n"
"border-color: rgb(192,128,64);\n"
"border-top-left-radius: 32px;\n"
"border-top-right-radius: 32px;\n"
"min-width: 240px;\n"
"padding: 3px;\n"
"color: rgb(0,0,0);\n"
"}\n"
"QTabBar::tab:last {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(224,224,128), stop: 0.4 rgb(224,192,96), stop: 0.5 rgb(224,224,128), stop: 1.0 rgb(224,192,96));\n"
"border-color: rgb(192,128,64);\n"
"border-top-left-radius: 32px;\n"
"border-top-right-radius: 32px;\n"
"min-width: 240px;\n"
"padding: 3px;\n"
"color: rgb(255,255,255);\n"
"}\n"
"QTabBar::tab:middle {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(224,224,128), stop: 0.4 rgb(224,192,96), stop: 0.5 rgb(224,224,128), stop: 1.0 rgb(224,192,96));\n"
"border-color: rgb(192,128,64);\n"
"border-top-left-radius: 32px;\n"
"border-top-right-radius: 32px;\n"
"min-width: 240px;\n"
"padding: 3px;\n"
"color: rgb(255,0,255);\n"
"}\n"
"QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(224,224,128), stop: 0.4 rgb(224,192,96), stop: 0.5 rgb(224,224,128), stop: 1.0 rgb(224,192,96));\n"
"border-color: rgb(192,128,64);\n"
"border-top-left-radius: 32px;\n"
"border-top-right-radius: 32px;\n"
"min-width: 240px;\n"
"padding: 3px;\n"
"color: rgb(192,128,64);\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:hover {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(255,224,128), stop: 0.4 rgb(255,255,192), stop: 0.5 rgb(255,255,192), stop: 1.0 rgb(255,224,128));\n"
"}\n"
"QTabBar::tab:selected {\n"
"border-color: rgb(192,128,64);\n"
"}\n"
"QTabBar::tab:!selected {\n"
"margin-top: 16px;\n"
"} ")
        self.qc_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.qc_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.qc_tabs.setIconSize(QtCore.QSize(16, 16))
        self.qc_tabs.setElideMode(QtCore.Qt.ElideLeft)
        self.qc_tabs.setDocumentMode(False)
        self.qc_tabs.setTabsClosable(False)
        self.qc_tabs.setMovable(True)
        self.qc_tabs.setTabBarAutoHide(False)
        self.qc_tabs.setObjectName("qc_tabs")
        self.entity_tab = QtWidgets.QWidget()
        self.entity_tab.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.entity_tab.setStyleSheet("#entity_tab { \n"
"background-image: url(:/bg/EntityWindowBackground.png);\n"
"background-color: rgb(0,0,0);\n"
"border: 5px;\n"
"border-image: url(:/bg/border_thin_yellow.png);\n"
"}")
        self.entity_tab.setObjectName("entity_tab")
        self.player_list = QtWidgets.QListWidget(self.entity_tab)
        self.player_list.setGeometry(QtCore.QRect(24, 36, 128, 256))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.player_list.setFont(font)
        self.player_list.setStyleSheet("#player_list {\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.player_list.setObjectName("player_list")
        self.label = QtWidgets.QLabel(self.entity_tab)
        self.label.setGeometry(QtCore.QRect(24, 10, 128, 24))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.entity_general_frame = QtWidgets.QFrame(self.entity_tab)
        self.entity_general_frame.setGeometry(QtCore.QRect(24, 320, 256, 256))
        self.entity_general_frame.setStyleSheet("#entity_general_frame {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.entity_general_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.entity_general_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entity_general_frame.setObjectName("entity_general_frame")
        self.label_3 = QtWidgets.QLabel(self.entity_general_frame)
        self.label_3.setGeometry(QtCore.QRect(10, 32, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.entity_general_frame)
        self.label_4.setGeometry(QtCore.QRect(10, 4, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.entity_general_frame)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 240, 31))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.entity_exp_bar = QtWidgets.QProgressBar(self.entity_general_frame)
        self.entity_exp_bar.setGeometry(QtCore.QRect(64, 64, 180, 24))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.entity_exp_bar.setFont(font)
        self.entity_exp_bar.setStyleSheet("#entity_exp_bar {\n"
"color: rgb(192,240,255);\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_blue.png);\n"
"}\n"
"#entity_exp_bar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0  rgb(64,128,240), stop: 1 rgb(128,192,255));\n"
"}")
        self.entity_exp_bar.setMaximum(10)
        self.entity_exp_bar.setProperty("value", 10)
        self.entity_exp_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_exp_bar.setTextVisible(True)
        self.entity_exp_bar.setInvertedAppearance(False)
        self.entity_exp_bar.setObjectName("entity_exp_bar")
        self.label_2 = QtWidgets.QLabel(self.entity_tab)
        self.label_2.setGeometry(QtCore.QRect(24, 295, 256, 24))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.enemy_list = QtWidgets.QListWidget(self.entity_tab)
        self.enemy_list.setGeometry(QtCore.QRect(160, 36, 128, 256))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.enemy_list.setFont(font)
        self.enemy_list.setStyleSheet("#enemy_list {\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.enemy_list.setObjectName("enemy_list")
        self.label_5 = QtWidgets.QLabel(self.entity_tab)
        self.label_5.setGeometry(QtCore.QRect(160, 10, 128, 24))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.entity_stat_frame = QtWidgets.QFrame(self.entity_tab)
        self.entity_stat_frame.setGeometry(QtCore.QRect(300, 36, 256, 256))
        self.entity_stat_frame.setStyleSheet("#entity_stat_frame {\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.entity_stat_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.entity_stat_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entity_stat_frame.setObjectName("entity_stat_frame")
        self.label_6 = QtWidgets.QLabel(self.entity_stat_frame)
        self.label_6.setGeometry(QtCore.QRect(10, 32, 240, 32))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.entity_stat_frame)
        self.label_7.setGeometry(QtCore.QRect(10, 4, 240, 32))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.entity_hp_bar = QtWidgets.QProgressBar(self.entity_stat_frame)
        self.entity_hp_bar.setGeometry(QtCore.QRect(50, 8, 200, 24))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.entity_hp_bar.setFont(font)
        self.entity_hp_bar.setStyleSheet("#entity_hp_bar {\n"
"color: rgb(255,160,128);\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_red.png);\n"
"}\n"
"#entity_hp_bar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgb(240,32,16), stop: 1 rgb(255,128,64));\n"
"}")
        self.entity_hp_bar.setMaximum(10)
        self.entity_hp_bar.setProperty("value", 10)
        self.entity_hp_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_hp_bar.setTextVisible(True)
        self.entity_hp_bar.setInvertedAppearance(False)
        self.entity_hp_bar.setObjectName("entity_hp_bar")
        self.entity_sp_bar = QtWidgets.QProgressBar(self.entity_stat_frame)
        self.entity_sp_bar.setGeometry(QtCore.QRect(50, 36, 200, 24))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.entity_sp_bar.setFont(font)
        self.entity_sp_bar.setStyleSheet("#entity_sp_bar {\n"
"color: rgb(192,255,192);\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_green.png);\n"
"}\n"
"#entity_sp_bar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgb(32,224,32), stop: 1 rgb(128,255,128));\n"
"}")
        self.entity_sp_bar.setMaximum(10)
        self.entity_sp_bar.setProperty("value", 10)
        self.entity_sp_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_sp_bar.setTextVisible(True)
        self.entity_sp_bar.setInvertedAppearance(False)
        self.entity_sp_bar.setObjectName("entity_sp_bar")
        self.qc_tabs.addTab(self.entity_tab, "")
        self.item_tab = QtWidgets.QWidget()
        self.item_tab.setStyleSheet("QTabBar::tab {\n"
"    border: 10px solid black;\n"
"}")
        self.item_tab.setObjectName("item_tab")
        self.qc_tabs.addTab(self.item_tab, "")
        self.skill_tab = QtWidgets.QWidget()
        self.skill_tab.setObjectName("skill_tab")
        self.qc_tabs.addTab(self.skill_tab, "")
        self.shop_tab = QtWidgets.QWidget()
        self.shop_tab.setObjectName("shop_tab")
        self.qc_tabs.addTab(self.shop_tab, "")
        self.output_list_view = QtWidgets.QListView(self.active_file_page)
        self.output_list_view.setGeometry(QtCore.QRect(0, 50, 256, 670))
        self.output_list_view.setMinimumSize(QtCore.QSize(256, 670))
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Heavy")
        font.setPointSize(12)
        font.setItalic(True)
        self.output_list_view.setFont(font)
        self.output_list_view.setStyleSheet("#output_list_view::item:hover {\n"
"    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                stop: 0 #FAFBFE, stop: 1 #DCDEF1);\n"
"}\n"
"#output_list_view {\n"
"    background: black;\n"
"    alternate-background-color: rgb(255,224,128);\n"
"    border: 5px;\n"
"    \n"
"    border-image: url(:/bg/border_thin_white.png);\n"
"    border-color: rgb(255,0,0);\n"
"}")
        self.output_list_view.setObjectName("output_list_view")
        self.output_label = QtWidgets.QLabel(self.active_file_page)
        self.output_label.setGeometry(QtCore.QRect(0, 0, 256, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.output_label.setFont(font)
        self.output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label.setObjectName("output_label")
        self.stackedWidget.addWidget(self.active_file_page)
        MainWindow.setCentralWidget(self.centralWidget)
        def on_FileSelectButton1_clicked():
            self.file_select_page.hide()
            self.active_file_page.show()
            mixer.music.stop()
        self.FileSelectButton1.clicked.connect(on_FileSelectButton1_clicked)
        self.retranslateUi(MainWindow)
        self.qc_tabs.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.FileSelectButton2.setText(_translate("MainWindow", "2"))
        self.qc_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aa55ff;\">Quest Calculator</span></p></body></html>"))
        self.FileSelectButton1.setText(_translate("MainWindow", "1"))
        self.pushButton_4.setText(_translate("MainWindow", "3"))
        self.file_select_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:36pt; color:#ffffff;\">File Select</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Players</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Level:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Name:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">EXP</span></p></body></html>"))
        self.entity_exp_bar.setFormat(_translate("MainWindow", "%v/%m"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">General Information</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Enemies</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">SP</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">HP</span></p></body></html>"))
        self.entity_hp_bar.setFormat(_translate("MainWindow", "%v/%m"))
        self.entity_sp_bar.setFormat(_translate("MainWindow", "%v/%m"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.entity_tab), _translate("MainWindow", "Entity"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.item_tab), _translate("MainWindow", "Item"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.skill_tab), _translate("MainWindow", "Skill"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.shop_tab), _translate("MainWindow", "Shop"))
        self.output_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt; color:#ffffff;\">Output</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    mixer.init()
    mixer.music.load('bg\\FileSelect.mp3')
    mixer.music.play()
    sys.exit(app.exec_())
