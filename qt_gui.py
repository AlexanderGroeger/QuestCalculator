# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Alex\Games_And_Tech\QuestCalculator\QCGUI\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1680, 1050)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setStyleSheet("QMainWindow {\n"
"background-color: rgb(0, 0, 0);\n"
"}")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setEnabled(True)
        self.centralWidget.setStyleSheet("#centralWidget {\n"
"border-image: url(:/bg/LegacyBackground.png) 0 0 0 0 stretch stretch;\n"
"}")
        self.centralWidget.setObjectName("centralWidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 1680, 1050))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.stackedWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.stackedWidget.setObjectName("stackedWidget")
        self.file_select_page = QtWidgets.QWidget()
        self.file_select_page.setMinimumSize(QtCore.QSize(0, 0))
        self.file_select_page.setStyleSheet("#file_select_page {\n"
"background: rgba(0,0,0,0);\n"
"}")
        self.file_select_page.setObjectName("file_select_page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.file_select_page)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.background_frame = QtWidgets.QFrame(self.file_select_page)
        self.background_frame.setEnabled(True)
        self.background_frame.setMinimumSize(QtCore.QSize(1280, 720))
        self.background_frame.setStyleSheet("#background_frame {\n"
"background: rgba(0,0,0,0);\n"
"}")
        self.background_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.background_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.background_frame.setLineWidth(0)
        self.background_frame.setObjectName("background_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.background_frame)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 5, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 7, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 6, 9, 1, 1)
        self.file_select_button2 = QtWidgets.QPushButton(self.background_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.file_select_button2.sizePolicy().hasHeightForWidth())
        self.file_select_button2.setSizePolicy(sizePolicy)
        self.file_select_button2.setMinimumSize(QtCore.QSize(400, 400))
        self.file_select_button2.setMaximumSize(QtCore.QSize(400, 400))
        self.file_select_button2.setBaseSize(QtCore.QSize(10, 10))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(200)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.file_select_button2.setFont(font)
        self.file_select_button2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.file_select_button2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.file_select_button2.setStyleSheet("QPushButton {\n"
"color: rgba(255,255,255,128);\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_dim_yellow.png);\n"
"}\n"
"QPushButton::hover {\n"
"color: white;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.file_select_button2.setFlat(True)
        self.file_select_button2.setObjectName("file_select_button2")
        self.gridLayout_3.addWidget(self.file_select_button2, 6, 3, 1, 1, QtCore.Qt.AlignHCenter)
        self.qc_label = QtWidgets.QLabel(self.background_frame)
        self.qc_label.setMinimumSize(QtCore.QSize(550, 100))
        self.qc_label.setMaximumSize(QtCore.QSize(720, 200))
        font = QtGui.QFont()
        font.setFamily("Script MT Bold")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.qc_label.setFont(font)
        self.qc_label.setStyleSheet("")
        self.qc_label.setTextFormat(QtCore.Qt.RichText)
        self.qc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.qc_label.setWordWrap(False)
        self.qc_label.setObjectName("qc_label")
        self.gridLayout_3.addWidget(self.qc_label, 0, 3, 1, 1)
        self.file_select_label = QtWidgets.QLabel(self.background_frame)
        self.file_select_label.setMinimumSize(QtCore.QSize(550, 100))
        self.file_select_label.setMaximumSize(QtCore.QSize(720, 100))
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
        self.gridLayout_3.addWidget(self.file_select_label, 3, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem3, 6, 0, 1, 1)
        self.file_select_label_2 = QtWidgets.QLabel(self.background_frame)
        self.file_select_label_2.setMinimumSize(QtCore.QSize(550, 0))
        self.file_select_label_2.setMaximumSize(QtCore.QSize(720, 16777215))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.file_select_label_2.setFont(font)
        self.file_select_label_2.setStyleSheet("")
        self.file_select_label_2.setTextFormat(QtCore.Qt.RichText)
        self.file_select_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.file_select_label_2.setWordWrap(False)
        self.file_select_label_2.setObjectName("file_select_label_2")
        self.gridLayout_3.addWidget(self.file_select_label_2, 4, 3, 1, 1)
        self.file_select_button3 = QtWidgets.QPushButton(self.background_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.file_select_button3.sizePolicy().hasHeightForWidth())
        self.file_select_button3.setSizePolicy(sizePolicy)
        self.file_select_button3.setMinimumSize(QtCore.QSize(400, 400))
        self.file_select_button3.setMaximumSize(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(200)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.file_select_button3.setFont(font)
        self.file_select_button3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.file_select_button3.setStyleSheet("QPushButton {\n"
"color: rgba(255,255,255,128);\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_dim_yellow.png);\n"
"}\n"
"QPushButton::hover {\n"
"color: white;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.file_select_button3.setFlat(True)
        self.file_select_button3.setObjectName("file_select_button3")
        self.gridLayout_3.addWidget(self.file_select_button3, 6, 4, 1, 1)
        self.file_select_button1 = QtWidgets.QPushButton(self.background_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.file_select_button1.sizePolicy().hasHeightForWidth())
        self.file_select_button1.setSizePolicy(sizePolicy)
        self.file_select_button1.setMinimumSize(QtCore.QSize(400, 400))
        self.file_select_button1.setMaximumSize(QtCore.QSize(400, 400))
        self.file_select_button1.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(200)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.file_select_button1.setFont(font)
        self.file_select_button1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.file_select_button1.setAutoFillBackground(False)
        self.file_select_button1.setStyleSheet("QPushButton {\n"
"color: rgba(255,255,255,128);\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_dim_yellow.png);\n"
"}\n"
"QPushButton::hover {\n"
"color: white;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.file_select_button1.setDefault(False)
        self.file_select_button1.setFlat(True)
        self.file_select_button1.setObjectName("file_select_button1")
        self.gridLayout_3.addWidget(self.file_select_button1, 6, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem4, 1, 3, 1, 1)
        self.gridLayout_2.addWidget(self.background_frame, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.file_select_page)
        self.active_file_page = QtWidgets.QWidget()
        self.active_file_page.setEnabled(True)
        self.active_file_page.setMinimumSize(QtCore.QSize(1920, 1080))
        self.active_file_page.setStyleSheet("#active_file_page {\n"
"    \n"
"    background: rgba(0,0,0,0);\n"
"}")
        self.active_file_page.setObjectName("active_file_page")
        self.qc_tabs = QtWidgets.QTabWidget(self.active_file_page)
        self.qc_tabs.setGeometry(QtCore.QRect(300, 0, 1380, 1050))
        self.qc_tabs.setMinimumSize(QtCore.QSize(1080, 720))
        self.qc_tabs.setMaximumSize(QtCore.QSize(1620, 1080))
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
"}\n"
"#qc_tabs::tab-bar {\n"
"left: 16px; /* move to the right by 5px */\n"
"}\n"
"#qc_tabs>QTabBar::tab {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(224,224,224), stop: 0.4 rgb(192,192,192), stop: 0.5 rgb(224,224,224), stop: 1.0 rgb(192,192,192));\n"
"border-top-left-radius: 16px;\n"
"border-top-right-radius: 16px;\n"
"border-bottom-left-radius: 16px;\n"
"border-bottom-right-radius: 16px;\n"
"min-width: 144px;\n"
"padding: 3px;\n"
"color: rgb(128,128,128);\n"
"}\n"
"#qc_tabs>QTabBar::tab:selected {\n"
"background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 rgb(224,224,224), stop: 0.4 rgb(255,255,255), stop: 0.5 rgb(255,255,255), stop: 1.0 rgb(224,224,224));\n"
"}\n"
"#qc_tabs>QTabBar::tab:!selected {\n"
"margin-top: 0px;\n"
"} ")
        self.qc_tabs.setTabPosition(QtWidgets.QTabWidget.North)
        self.qc_tabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.qc_tabs.setIconSize(QtCore.QSize(16, 16))
        self.qc_tabs.setElideMode(QtCore.Qt.ElideLeft)
        self.qc_tabs.setDocumentMode(False)
        self.qc_tabs.setTabsClosable(False)
        self.qc_tabs.setMovable(False)
        self.qc_tabs.setTabBarAutoHide(False)
        self.qc_tabs.setObjectName("qc_tabs")
        self.entity_tab = QtWidgets.QWidget()
        self.entity_tab.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.entity_tab.setStyleSheet("#entity_tab { \n"
"background-color: rgba(0,0,0,0);\n"
"border: 0px;\n"
"}")
        self.entity_tab.setObjectName("entity_tab")
        self.player_list = QtWidgets.QListWidget(self.entity_tab)
        self.player_list.setGeometry(QtCore.QRect(10, 90, 350, 300))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player_list.sizePolicy().hasHeightForWidth())
        self.player_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.player_list.setFont(font)
        self.player_list.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.player_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.player_list.setStyleSheet("QListWidget {\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    outline: 0px;\n"
"}\n"
"QListWidget::item {\n"
"    color: rgba(255,255,255,128);\n"
"    background: rgba(0,0,0,0);\n"
"}\n"
"QListWidget::item:selected {\n"
"    color: white;\n"
"    background: rgba(255,255,255,64);\n"
"    image: url(:/bg/checkmark.png);\n"
"    image-position: left;\n"
"}\n"
"QListWidget::item:focus {\n"
"    color: white;\n"
"    background: rgba(255,255,255,128);\n"
"}\n"
"QListWidget::item:!selected:!focus:hover {\n"
"    color: white;\n"
"}")
        self.player_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.player_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.player_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.player_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.player_list.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.player_list.setFlow(QtWidgets.QListView.TopToBottom)
        self.player_list.setUniformItemSizes(True)
        self.player_list.setBatchSize(15)
        self.player_list.setObjectName("player_list")
        self.players_label = QtWidgets.QLabel(self.entity_tab)
        self.players_label.setGeometry(QtCore.QRect(10, 0, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.players_label.setFont(font)
        self.players_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.players_label.setAlignment(QtCore.Qt.AlignCenter)
        self.players_label.setObjectName("players_label")
        self.entity_general_frame = QtWidgets.QFrame(self.entity_tab)
        self.entity_general_frame.setGeometry(QtCore.QRect(370, 40, 400, 975))
        self.entity_general_frame.setStyleSheet("#entity_general_frame {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.entity_general_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.entity_general_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entity_general_frame.setObjectName("entity_general_frame")
        self.entity_name_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_name_label.setGeometry(QtCore.QRect(10, 5, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.entity_name_label.setFont(font)
        self.entity_name_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_name_label.setObjectName("entity_name_label")
        self.entity_exp_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_exp_label.setGeometry(QtCore.QRect(10, 140, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_exp_label.setFont(font)
        self.entity_exp_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_exp_label.setStyleSheet("")
        self.entity_exp_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_exp_label.setObjectName("entity_exp_label")
        self.entity_exp_bar = QtWidgets.QProgressBar(self.entity_general_frame)
        self.entity_exp_bar.setGeometry(QtCore.QRect(90, 140, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.entity_exp_bar.setFont(font)
        self.entity_exp_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_exp_bar.setStyleSheet("QProgressBar {\n"
"color: rgb(192,240,255);\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0  rgb(32,96,224), stop: 1 rgb(128,192,255));\n"
"}")
        self.entity_exp_bar.setMaximum(10)
        self.entity_exp_bar.setProperty("value", 0)
        self.entity_exp_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_exp_bar.setTextVisible(True)
        self.entity_exp_bar.setInvertedAppearance(False)
        self.entity_exp_bar.setObjectName("entity_exp_bar")
        self.entity_jewels_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_jewels_box.setGeometry(QtCore.QRect(150, 100, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_jewels_box.setFont(font)
        self.entity_jewels_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.entity_jewels_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_jewels_box.setStyleSheet("QSpinBox {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(224,96,255);\n"
"}")
        self.entity_jewels_box.setWrapping(False)
        self.entity_jewels_box.setFrame(False)
        self.entity_jewels_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_jewels_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_jewels_box.setPrefix("")
        self.entity_jewels_box.setMaximum(99999)
        self.entity_jewels_box.setProperty("value", 0)
        self.entity_jewels_box.setObjectName("entity_jewels_box")
        self.entity_gold_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_gold_box.setGeometry(QtCore.QRect(150, 70, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_gold_box.setFont(font)
        self.entity_gold_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.entity_gold_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_gold_box.setStyleSheet("QSpinBox {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(255,236,90);\n"
"}")
        self.entity_gold_box.setWrapping(False)
        self.entity_gold_box.setFrame(False)
        self.entity_gold_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_gold_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_gold_box.setPrefix("")
        self.entity_gold_box.setMaximum(999999999)
        self.entity_gold_box.setProperty("value", 0)
        self.entity_gold_box.setObjectName("entity_gold_box")
        self.entity_name_box = QtWidgets.QLineEdit(self.entity_general_frame)
        self.entity_name_box.setGeometry(QtCore.QRect(100, 5, 290, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_name_box.setFont(font)
        self.entity_name_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_name_box.setStyleSheet("QLineEdit {\n"
"border: 0px;\n"
"background-color:  rgba(255,255,255,0);\n"
"color: rgb(240,240,255);\n"
"}")
        self.entity_name_box.setText("")
        self.entity_name_box.setMaxLength(20)
        self.entity_name_box.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_name_box.setDragEnabled(False)
        self.entity_name_box.setObjectName("entity_name_box")
        self.player_attack_change_label = QtWidgets.QLabel(self.entity_general_frame)
        self.player_attack_change_label.setGeometry(QtCore.QRect(270, 620, 64, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.player_attack_change_label.setFont(font)
        self.player_attack_change_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_attack_change_label.setObjectName("player_attack_change_label")
        self.player_critical_change_label = QtWidgets.QLabel(self.entity_general_frame)
        self.player_critical_change_label.setGeometry(QtCore.QRect(270, 770, 64, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.player_critical_change_label.setFont(font)
        self.player_critical_change_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_critical_change_label.setObjectName("player_critical_change_label")
        self.entity_hp_bar = QtWidgets.QProgressBar(self.entity_general_frame)
        self.entity_hp_bar.setGeometry(QtCore.QRect(90, 180, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.entity_hp_bar.setFont(font)
        self.entity_hp_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_hp_bar.setStyleSheet("QProgressBar {\n"
"color: rgb(255,192,160);\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgb(224,16,16), stop: 1 rgb(255,192,128));\n"
"}")
        self.entity_hp_bar.setMaximum(1)
        self.entity_hp_bar.setProperty("value", 1)
        self.entity_hp_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_hp_bar.setTextVisible(True)
        self.entity_hp_bar.setInvertedAppearance(False)
        self.entity_hp_bar.setObjectName("entity_hp_bar")
        self.entity_accuracy_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_accuracy_box.setGeometry(QtCore.QRect(200, 660, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_accuracy_box.setFont(font)
        self.entity_accuracy_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_accuracy_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_accuracy_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;")
        self.entity_accuracy_box.setWrapping(False)
        self.entity_accuracy_box.setFrame(False)
        self.entity_accuracy_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_accuracy_box.setReadOnly(True)
        self.entity_accuracy_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_accuracy_box.setPrefix("")
        self.entity_accuracy_box.setMinimum(1)
        self.entity_accuracy_box.setMaximum(9999)
        self.entity_accuracy_box.setSingleStep(1)
        self.entity_accuracy_box.setProperty("value", 1)
        self.entity_accuracy_box.setObjectName("entity_accuracy_box")
        self.entity_food_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_food_label.setGeometry(QtCore.QRect(10, 260, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_food_label.setFont(font)
        self.entity_food_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_food_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_food_label.setObjectName("entity_food_label")
        self.entity_special_defense_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_special_defense_box.setGeometry(QtCore.QRect(200, 620, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_special_defense_box.setFont(font)
        self.entity_special_defense_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_special_defense_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_special_defense_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"")
        self.entity_special_defense_box.setWrapping(False)
        self.entity_special_defense_box.setFrame(False)
        self.entity_special_defense_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_special_defense_box.setReadOnly(True)
        self.entity_special_defense_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_special_defense_box.setPrefix("")
        self.entity_special_defense_box.setMinimum(1)
        self.entity_special_defense_box.setMaximum(9999)
        self.entity_special_defense_box.setSingleStep(1)
        self.entity_special_defense_box.setProperty("value", 1)
        self.entity_special_defense_box.setObjectName("entity_special_defense_box")
        self.entity_sp_bar = QtWidgets.QProgressBar(self.entity_general_frame)
        self.entity_sp_bar.setGeometry(QtCore.QRect(90, 220, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.entity_sp_bar.setFont(font)
        self.entity_sp_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_sp_bar.setStyleSheet("QProgressBar {\n"
"color: rgb(192,255,192);\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgb(16,192,16), stop: 1 rgb(160,255,160));\n"
"}")
        self.entity_sp_bar.setMaximum(1)
        self.entity_sp_bar.setProperty("value", 1)
        self.entity_sp_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_sp_bar.setTextVisible(True)
        self.entity_sp_bar.setInvertedAppearance(False)
        self.entity_sp_bar.setObjectName("entity_sp_bar")
        self.entity_blessing_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_blessing_box.setGeometry(QtCore.QRect(200, 780, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_blessing_box.setFont(font)
        self.entity_blessing_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_blessing_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_blessing_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"")
        self.entity_blessing_box.setWrapping(False)
        self.entity_blessing_box.setFrame(False)
        self.entity_blessing_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_blessing_box.setReadOnly(True)
        self.entity_blessing_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_blessing_box.setPrefix("")
        self.entity_blessing_box.setMinimum(1)
        self.entity_blessing_box.setMaximum(9999)
        self.entity_blessing_box.setSingleStep(1)
        self.entity_blessing_box.setProperty("value", 1)
        self.entity_blessing_box.setObjectName("entity_blessing_box")
        self.entity_food_bar = QtWidgets.QProgressBar(self.entity_general_frame)
        self.entity_food_bar.setGeometry(QtCore.QRect(90, 260, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.entity_food_bar.setFont(font)
        self.entity_food_bar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_food_bar.setStyleSheet("QProgressBar {\n"
"color: rgb(255,255,192);\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"}\n"
"QProgressBar::chunk:horizontal {\n"
"background: qlineargradient(x1: 0, y1: 0.5, x2: 1, y2: 0.5, stop: 0 rgb(192,192,32), stop: 1 rgb(255,224,128));\n"
"}")
        self.entity_food_bar.setMaximum(100)
        self.entity_food_bar.setProperty("value", 100)
        self.entity_food_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_food_bar.setTextVisible(True)
        self.entity_food_bar.setInvertedAppearance(False)
        self.entity_food_bar.setObjectName("entity_food_bar")
        self.entity_sp_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_sp_label.setGeometry(QtCore.QRect(10, 220, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_sp_label.setFont(font)
        self.entity_sp_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_sp_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_sp_label.setObjectName("entity_sp_label")
        self.entity_evasion_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_evasion_box.setGeometry(QtCore.QRect(200, 700, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_evasion_box.setFont(font)
        self.entity_evasion_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_evasion_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_evasion_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"")
        self.entity_evasion_box.setWrapping(False)
        self.entity_evasion_box.setFrame(False)
        self.entity_evasion_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_evasion_box.setReadOnly(True)
        self.entity_evasion_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_evasion_box.setPrefix("")
        self.entity_evasion_box.setMinimum(1)
        self.entity_evasion_box.setMaximum(9999)
        self.entity_evasion_box.setSingleStep(1)
        self.entity_evasion_box.setProperty("value", 1)
        self.entity_evasion_box.setObjectName("entity_evasion_box")
        self.entity_hp_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_hp_label.setGeometry(QtCore.QRect(10, 180, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_hp_label.setFont(font)
        self.entity_hp_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_hp_label.setStyleSheet("")
        self.entity_hp_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_hp_label.setObjectName("entity_hp_label")
        self.player_special_defense_change_label = QtWidgets.QLabel(self.entity_general_frame)
        self.player_special_defense_change_label.setGeometry(QtCore.QRect(270, 695, 64, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.player_special_defense_change_label.setFont(font)
        self.player_special_defense_change_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_special_defense_change_label.setObjectName("player_special_defense_change_label")
        self.player_defense_change_label = QtWidgets.QLabel(self.entity_general_frame)
        self.player_defense_change_label.setGeometry(QtCore.QRect(270, 645, 64, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.player_defense_change_label.setFont(font)
        self.player_defense_change_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_defense_change_label.setObjectName("player_defense_change_label")
        self.entity_defense_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_defense_box.setGeometry(QtCore.QRect(200, 540, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_defense_box.setFont(font)
        self.entity_defense_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_defense_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_defense_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;")
        self.entity_defense_box.setWrapping(False)
        self.entity_defense_box.setFrame(False)
        self.entity_defense_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_defense_box.setReadOnly(True)
        self.entity_defense_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_defense_box.setPrefix("")
        self.entity_defense_box.setMinimum(1)
        self.entity_defense_box.setMaximum(9999)
        self.entity_defense_box.setSingleStep(1)
        self.entity_defense_box.setProperty("value", 1)
        self.entity_defense_box.setObjectName("entity_defense_box")
        self.entity_special_attack_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_special_attack_box.setGeometry(QtCore.QRect(200, 580, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_special_attack_box.setFont(font)
        self.entity_special_attack_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_special_attack_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_special_attack_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"")
        self.entity_special_attack_box.setWrapping(False)
        self.entity_special_attack_box.setFrame(False)
        self.entity_special_attack_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_special_attack_box.setReadOnly(True)
        self.entity_special_attack_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_special_attack_box.setPrefix("")
        self.entity_special_attack_box.setMinimum(1)
        self.entity_special_attack_box.setMaximum(9999)
        self.entity_special_attack_box.setSingleStep(1)
        self.entity_special_attack_box.setProperty("value", 1)
        self.entity_special_attack_box.setObjectName("entity_special_attack_box")
        self.player_blessing_change_label = QtWidgets.QLabel(self.entity_general_frame)
        self.player_blessing_change_label.setGeometry(QtCore.QRect(270, 795, 64, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.player_blessing_change_label.setFont(font)
        self.player_blessing_change_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_blessing_change_label.setObjectName("player_blessing_change_label")
        self.player_accuracy_change_label = QtWidgets.QLabel(self.entity_general_frame)
        self.player_accuracy_change_label.setGeometry(QtCore.QRect(270, 720, 64, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.player_accuracy_change_label.setFont(font)
        self.player_accuracy_change_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_accuracy_change_label.setObjectName("player_accuracy_change_label")
        self.entity_critical_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_critical_box.setGeometry(QtCore.QRect(200, 740, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_critical_box.setFont(font)
        self.entity_critical_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_critical_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_critical_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"")
        self.entity_critical_box.setWrapping(False)
        self.entity_critical_box.setFrame(False)
        self.entity_critical_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_critical_box.setReadOnly(True)
        self.entity_critical_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_critical_box.setPrefix("")
        self.entity_critical_box.setMinimum(1)
        self.entity_critical_box.setMaximum(9999)
        self.entity_critical_box.setSingleStep(1)
        self.entity_critical_box.setProperty("value", 1)
        self.entity_critical_box.setObjectName("entity_critical_box")
        self.player_evasion_change_label = QtWidgets.QLabel(self.entity_general_frame)
        self.player_evasion_change_label.setGeometry(QtCore.QRect(270, 745, 64, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.player_evasion_change_label.setFont(font)
        self.player_evasion_change_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_evasion_change_label.setObjectName("player_evasion_change_label")
        self.entity_attack_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_attack_box.setGeometry(QtCore.QRect(200, 500, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_attack_box.setFont(font)
        self.entity_attack_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_attack_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_attack_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;")
        self.entity_attack_box.setWrapping(False)
        self.entity_attack_box.setFrame(False)
        self.entity_attack_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_attack_box.setReadOnly(True)
        self.entity_attack_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_attack_box.setPrefix("")
        self.entity_attack_box.setMinimum(1)
        self.entity_attack_box.setMaximum(9999)
        self.entity_attack_box.setSingleStep(1)
        self.entity_attack_box.setProperty("value", 1)
        self.entity_attack_box.setObjectName("entity_attack_box")
        self.player_special_attack_change_label = QtWidgets.QLabel(self.entity_general_frame)
        self.player_special_attack_change_label.setGeometry(QtCore.QRect(270, 670, 64, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.player_special_attack_change_label.setFont(font)
        self.player_special_attack_change_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.player_special_attack_change_label.setObjectName("player_special_attack_change_label")
        self.entity_level_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_level_box.setGeometry(QtCore.QRect(10, 40, 140, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_level_box.setFont(font)
        self.entity_level_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.entity_level_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_level_box.setStyleSheet("QSpinBox {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.entity_level_box.setWrapping(False)
        self.entity_level_box.setFrame(False)
        self.entity_level_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_level_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_level_box.setMinimum(1)
        self.entity_level_box.setMaximum(999)
        self.entity_level_box.setProperty("value", 1)
        self.entity_level_box.setObjectName("entity_level_box")
        self.entity_strength_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_strength_box.setGeometry(QtCore.QRect(200, 300, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_strength_box.setFont(font)
        self.entity_strength_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_strength_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_strength_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(255, 170, 96);\n"
"")
        self.entity_strength_box.setWrapping(False)
        self.entity_strength_box.setFrame(False)
        self.entity_strength_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_strength_box.setReadOnly(True)
        self.entity_strength_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_strength_box.setPrefix("")
        self.entity_strength_box.setMinimum(0)
        self.entity_strength_box.setMaximum(999)
        self.entity_strength_box.setSingleStep(1)
        self.entity_strength_box.setProperty("value", 0)
        self.entity_strength_box.setObjectName("entity_strength_box")
        self.entity_dexterity_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_dexterity_box.setGeometry(QtCore.QRect(200, 340, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_dexterity_box.setFont(font)
        self.entity_dexterity_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_dexterity_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_dexterity_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(85, 255, 127);\n"
"")
        self.entity_dexterity_box.setWrapping(False)
        self.entity_dexterity_box.setFrame(False)
        self.entity_dexterity_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_dexterity_box.setReadOnly(True)
        self.entity_dexterity_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_dexterity_box.setPrefix("")
        self.entity_dexterity_box.setMinimum(0)
        self.entity_dexterity_box.setMaximum(999)
        self.entity_dexterity_box.setSingleStep(1)
        self.entity_dexterity_box.setProperty("value", 0)
        self.entity_dexterity_box.setObjectName("entity_dexterity_box")
        self.entity_constitution_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_constitution_box.setGeometry(QtCore.QRect(200, 380, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_constitution_box.setFont(font)
        self.entity_constitution_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_constitution_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_constitution_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(255, 224, 96);\n"
"")
        self.entity_constitution_box.setWrapping(False)
        self.entity_constitution_box.setFrame(False)
        self.entity_constitution_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_constitution_box.setReadOnly(True)
        self.entity_constitution_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_constitution_box.setPrefix("")
        self.entity_constitution_box.setMinimum(0)
        self.entity_constitution_box.setMaximum(999)
        self.entity_constitution_box.setSingleStep(1)
        self.entity_constitution_box.setProperty("value", 0)
        self.entity_constitution_box.setObjectName("entity_constitution_box")
        self.entity_intelligence_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_intelligence_box.setGeometry(QtCore.QRect(200, 420, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_intelligence_box.setFont(font)
        self.entity_intelligence_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_intelligence_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_intelligence_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(64, 192, 255);")
        self.entity_intelligence_box.setWrapping(False)
        self.entity_intelligence_box.setFrame(False)
        self.entity_intelligence_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_intelligence_box.setReadOnly(True)
        self.entity_intelligence_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_intelligence_box.setPrefix("")
        self.entity_intelligence_box.setMinimum(0)
        self.entity_intelligence_box.setMaximum(999)
        self.entity_intelligence_box.setSingleStep(1)
        self.entity_intelligence_box.setProperty("value", 0)
        self.entity_intelligence_box.setObjectName("entity_intelligence_box")
        self.entity_integrity_box = QtWidgets.QSpinBox(self.entity_general_frame)
        self.entity_integrity_box.setGeometry(QtCore.QRect(200, 460, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_integrity_box.setFont(font)
        self.entity_integrity_box.setFocusPolicy(QtCore.Qt.NoFocus)
        self.entity_integrity_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_integrity_box.setStyleSheet("border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;")
        self.entity_integrity_box.setWrapping(False)
        self.entity_integrity_box.setFrame(False)
        self.entity_integrity_box.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.entity_integrity_box.setReadOnly(True)
        self.entity_integrity_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_integrity_box.setPrefix("")
        self.entity_integrity_box.setMinimum(0)
        self.entity_integrity_box.setMaximum(999)
        self.entity_integrity_box.setSingleStep(1)
        self.entity_integrity_box.setProperty("value", 0)
        self.entity_integrity_box.setObjectName("entity_integrity_box")
        self.entity_element_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_element_label.setGeometry(QtCore.QRect(180, 40, 150, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_element_label.setFont(font)
        self.entity_element_label.setStyleSheet("QLabel {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.entity_element_label.setObjectName("entity_element_label")
        self.entity_gold_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_gold_label.setGeometry(QtCore.QRect(10, 70, 80, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.entity_gold_label.setFont(font)
        self.entity_gold_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_gold_label.setObjectName("entity_gold_label")
        self.entity_gold_label_2 = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_gold_label_2.setGeometry(QtCore.QRect(10, 100, 90, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.entity_gold_label_2.setFont(font)
        self.entity_gold_label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_gold_label_2.setObjectName("entity_gold_label_2")
        self.entity_strength_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_strength_label.setGeometry(QtCore.QRect(10, 300, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_strength_label.setFont(font)
        self.entity_strength_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_strength_label.setStyleSheet("")
        self.entity_strength_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_strength_label.setObjectName("entity_strength_label")
        self.entity_dexterity_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_dexterity_label.setGeometry(QtCore.QRect(10, 340, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_dexterity_label.setFont(font)
        self.entity_dexterity_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_dexterity_label.setStyleSheet("")
        self.entity_dexterity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_dexterity_label.setObjectName("entity_dexterity_label")
        self.entity_constitution_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_constitution_label.setGeometry(QtCore.QRect(10, 380, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_constitution_label.setFont(font)
        self.entity_constitution_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_constitution_label.setStyleSheet("")
        self.entity_constitution_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_constitution_label.setObjectName("entity_constitution_label")
        self.entity_intelligence_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_intelligence_label.setGeometry(QtCore.QRect(10, 420, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_intelligence_label.setFont(font)
        self.entity_intelligence_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_intelligence_label.setStyleSheet("")
        self.entity_intelligence_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_intelligence_label.setObjectName("entity_intelligence_label")
        self.entity_integrity_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_integrity_label.setGeometry(QtCore.QRect(10, 460, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_integrity_label.setFont(font)
        self.entity_integrity_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_integrity_label.setStyleSheet("")
        self.entity_integrity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_integrity_label.setObjectName("entity_integrity_label")
        self.entity_attack_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_attack_label.setGeometry(QtCore.QRect(10, 500, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.entity_attack_label.setFont(font)
        self.entity_attack_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_attack_label.setStyleSheet("")
        self.entity_attack_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_attack_label.setObjectName("entity_attack_label")
        self.entity_defense_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_defense_label.setGeometry(QtCore.QRect(10, 540, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.entity_defense_label.setFont(font)
        self.entity_defense_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_defense_label.setStyleSheet("")
        self.entity_defense_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_defense_label.setObjectName("entity_defense_label")
        self.entity_special_defense_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_special_defense_label.setGeometry(QtCore.QRect(10, 620, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.entity_special_defense_label.setFont(font)
        self.entity_special_defense_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_special_defense_label.setStyleSheet("")
        self.entity_special_defense_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_special_defense_label.setObjectName("entity_special_defense_label")
        self.entity_special_attack_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_special_attack_label.setGeometry(QtCore.QRect(10, 580, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.entity_special_attack_label.setFont(font)
        self.entity_special_attack_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_special_attack_label.setStyleSheet("")
        self.entity_special_attack_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_special_attack_label.setObjectName("entity_special_attack_label")
        self.entity_accuracy_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_accuracy_label.setGeometry(QtCore.QRect(10, 660, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.entity_accuracy_label.setFont(font)
        self.entity_accuracy_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_accuracy_label.setStyleSheet("")
        self.entity_accuracy_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_accuracy_label.setObjectName("entity_accuracy_label")
        self.entity_evasion_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_evasion_label.setGeometry(QtCore.QRect(10, 700, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.entity_evasion_label.setFont(font)
        self.entity_evasion_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_evasion_label.setStyleSheet("")
        self.entity_evasion_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_evasion_label.setObjectName("entity_evasion_label")
        self.entity_critical_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_critical_label.setGeometry(QtCore.QRect(10, 740, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.entity_critical_label.setFont(font)
        self.entity_critical_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_critical_label.setStyleSheet("")
        self.entity_critical_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_critical_label.setObjectName("entity_critical_label")
        self.entity_blessing_label = QtWidgets.QLabel(self.entity_general_frame)
        self.entity_blessing_label.setGeometry(QtCore.QRect(10, 780, 180, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.entity_blessing_label.setFont(font)
        self.entity_blessing_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_blessing_label.setStyleSheet("")
        self.entity_blessing_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.entity_blessing_label.setObjectName("entity_blessing_label")
        self.general_label = QtWidgets.QLabel(self.entity_tab)
        self.general_label.setGeometry(QtCore.QRect(370, 0, 400, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.general_label.setFont(font)
        self.general_label.setAlignment(QtCore.Qt.AlignCenter)
        self.general_label.setObjectName("general_label")
        self.enemy_list = QtWidgets.QListWidget(self.entity_tab)
        self.enemy_list.setGeometry(QtCore.QRect(10, 540, 350, 420))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.enemy_list.setFont(font)
        self.enemy_list.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.enemy_list.setStyleSheet("QListWidget {\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    outline: 0px;\n"
"}\n"
"QListWidget::item {\n"
"    color: rgba(255,255,255,128);\n"
"    background: rgba(0,0,0,0);\n"
"}\n"
"QListWidget::item:selected {\n"
"    color: white;\n"
"    background: rgba(255,255,255,64);\n"
"    image: url(:/bg/checkmark.png);\n"
"    image-position: left;\n"
"}\n"
"QListWidget::item:focus {\n"
"    color: white;\n"
"    background: rgba(255,255,255,128);\n"
"}\n"
"QListWidget::item:!selected:!focus:hover {\n"
"    color: white;\n"
"}")
        self.enemy_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.enemy_list.setObjectName("enemy_list")
        self.enemies_label = QtWidgets.QLabel(self.entity_tab)
        self.enemies_label.setGeometry(QtCore.QRect(10, 450, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.enemies_label.setFont(font)
        self.enemies_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.enemies_label.setStyleSheet("")
        self.enemies_label.setAlignment(QtCore.Qt.AlignCenter)
        self.enemies_label.setObjectName("enemies_label")
        self.player_add_button = QtWidgets.QPushButton(self.entity_tab)
        self.player_add_button.setGeometry(QtCore.QRect(10, 400, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.player_add_button.setFont(font)
        self.player_add_button.setToolTipDuration(1)
        self.player_add_button.setStyleSheet("QPushButton {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: rgba(255,255,255,128);\n"
"}\n"
"QPushButton::hover {\n"
"color: white;\n"
"}\n"
"QPushButton:checked {\n"
"color: rgb(224,224,224);\n"
"    border-image: url(:/bg/pane_thin_dark_yellow.png);\n"
"}")
        self.player_add_button.setCheckable(False)
        self.player_add_button.setFlat(True)
        self.player_add_button.setObjectName("player_add_button")
        self.player_delete_button = QtWidgets.QPushButton(self.entity_tab)
        self.player_delete_button.setGeometry(QtCore.QRect(250, 400, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.player_delete_button.setFont(font)
        self.player_delete_button.setToolTipDuration(1)
        self.player_delete_button.setStyleSheet("QPushButton {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: rgba(255,255,255,128);\n"
"}\n"
"QPushButton::hover {\n"
"color: white;\n"
"}\n"
"QPushButton:checked {\n"
"color: rgb(224,224,224);\n"
"    border-image: url(:/bg/pane_thin_dark_yellow.png);\n"
"}")
        self.player_delete_button.setCheckable(False)
        self.player_delete_button.setFlat(True)
        self.player_delete_button.setObjectName("player_delete_button")
        self.player_copy_button = QtWidgets.QPushButton(self.entity_tab)
        self.player_copy_button.setGeometry(QtCore.QRect(130, 400, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.player_copy_button.setFont(font)
        self.player_copy_button.setToolTipDuration(1)
        self.player_copy_button.setStyleSheet("QPushButton {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: rgba(255,255,255,128);\n"
"}\n"
"QPushButton::hover {\n"
"color: white;\n"
"}\n"
"QPushButton:checked {\n"
"color: rgb(224,224,224);\n"
"    border-image: url(:/bg/pane_thin_dark_yellow.png);\n"
"}")
        self.player_copy_button.setCheckable(False)
        self.player_copy_button.setFlat(True)
        self.player_copy_button.setObjectName("player_copy_button")
        self.entity_change_frame = QtWidgets.QFrame(self.entity_tab)
        self.entity_change_frame.setGeometry(QtCore.QRect(780, 40, 250, 510))
        self.entity_change_frame.setStyleSheet("#entity_change_frame {\n"
"border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.entity_change_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.entity_change_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entity_change_frame.setObjectName("entity_change_frame")
        self.entity_stats_change_box = QtWidgets.QSpinBox(self.entity_change_frame)
        self.entity_stats_change_box.setGeometry(QtCore.QRect(20, 400, 210, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_stats_change_box.setFont(font)
        self.entity_stats_change_box.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.entity_stats_change_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_stats_change_box.setStyleSheet("QSpinBox {\n"
"border: 5px;\n"
"background-color: rgba(255,255,255,0);\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: white;\n"
"}")
        self.entity_stats_change_box.setWrapping(False)
        self.entity_stats_change_box.setFrame(False)
        self.entity_stats_change_box.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_stats_change_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.entity_stats_change_box.setSuffix("")
        self.entity_stats_change_box.setPrefix("")
        self.entity_stats_change_box.setMinimum(-99999999)
        self.entity_stats_change_box.setMaximum(99999999)
        self.entity_stats_change_box.setProperty("value", 1)
        self.entity_stats_change_box.setObjectName("entity_stats_change_box")
        self.entity_change_status_gold = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_gold.setGeometry(QtCore.QRect(20, 20, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_gold.setFont(font)
        self.entity_change_status_gold.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_gold.setStyleSheet("QCheckBox {\n"
"    color: rgb(255,236,90);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    \n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.entity_change_status_gold.setObjectName("entity_change_status_gold")
        self.entity_change_status_jewels = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_jewels.setGeometry(QtCore.QRect(20, 50, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_jewels.setFont(font)
        self.entity_change_status_jewels.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_jewels.setStyleSheet("QCheckBox {\n"
"    color: rgb(224,96,255);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}")
        self.entity_change_status_jewels.setObjectName("entity_change_status_jewels")
        self.entity_change_status_exp = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_exp.setGeometry(QtCore.QRect(20, 80, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_exp.setFont(font)
        self.entity_change_status_exp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_exp.setStyleSheet("QCheckBox {\n"
"    color: rgb(192,255,255);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    \n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}")
        self.entity_change_status_exp.setObjectName("entity_change_status_exp")
        self.entity_change_status_hp = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_hp.setGeometry(QtCore.QRect(20, 110, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_hp.setFont(font)
        self.entity_change_status_hp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_hp.setStyleSheet("QCheckBox {\n"
"    color: rgb(255,160,128);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}")
        self.entity_change_status_hp.setObjectName("entity_change_status_hp")
        self.entity_change_status_sp = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_sp.setGeometry(QtCore.QRect(20, 140, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_sp.setFont(font)
        self.entity_change_status_sp.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_sp.setStyleSheet("QCheckBox {\n"
"    color: rgb(160,255,128);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}")
        self.entity_change_status_sp.setObjectName("entity_change_status_sp")
        self.entity_change_status_food = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_food.setGeometry(QtCore.QRect(20, 170, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_food.setFont(font)
        self.entity_change_status_food.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_food.setStyleSheet("QCheckBox {\n"
"    color: rgb(255,255,128);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}")
        self.entity_change_status_food.setObjectName("entity_change_status_food")
        self.entity_stats_change_add_button = QtWidgets.QPushButton(self.entity_change_frame)
        self.entity_stats_change_add_button.setGeometry(QtCore.QRect(20, 450, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_stats_change_add_button.setFont(font)
        self.entity_stats_change_add_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_stats_change_add_button.setToolTipDuration(1)
        self.entity_stats_change_add_button.setStyleSheet("QPushButton {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_dim_yellow.png);\n"
"color: rgba(255,255,255,128);\n"
"}\n"
"QPushButton::hover {\n"
"color: white;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"}\n"
"QPushButton:checked {\n"
"color: rgb(224,224,224);\n"
"    border-image: url(:/bg/pane_thin_dark_yellow.png);\n"
"}")
        self.entity_stats_change_add_button.setCheckable(False)
        self.entity_stats_change_add_button.setFlat(True)
        self.entity_stats_change_add_button.setObjectName("entity_stats_change_add_button")
        self.entity_stats_change_set_button = QtWidgets.QPushButton(self.entity_change_frame)
        self.entity_stats_change_set_button.setGeometry(QtCore.QRect(130, 450, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_stats_change_set_button.setFont(font)
        self.entity_stats_change_set_button.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_stats_change_set_button.setToolTipDuration(1)
        self.entity_stats_change_set_button.setStyleSheet("QPushButton {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_dim_yellow.png);\n"
"color: rgba(255,255,255,128);\n"
"}\n"
"QPushButton::hover {\n"
"color: white;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"}\n"
"QPushButton:checked {\n"
"color: rgb(224,224,224);\n"
"    border-image: url(:/bg/pane_thin_dark_yellow.png);\n"
"}")
        self.entity_stats_change_set_button.setCheckable(False)
        self.entity_stats_change_set_button.setFlat(True)
        self.entity_stats_change_set_button.setObjectName("entity_stats_change_set_button")
        self.entity_change_status_strength = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_strength.setGeometry(QtCore.QRect(20, 200, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_strength.setFont(font)
        self.entity_change_status_strength.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_strength.setStyleSheet("QCheckBox {\n"
"    color: rgb(255, 170, 96);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.entity_change_status_strength.setObjectName("entity_change_status_strength")
        self.entity_change_status_dexterity = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_dexterity.setGeometry(QtCore.QRect(20, 230, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_dexterity.setFont(font)
        self.entity_change_status_dexterity.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_dexterity.setStyleSheet("QCheckBox {\n"
"    color: rgb(85, 255, 127);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.entity_change_status_dexterity.setObjectName("entity_change_status_dexterity")
        self.entity_change_status_constitution = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_constitution.setGeometry(QtCore.QRect(20, 260, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_constitution.setFont(font)
        self.entity_change_status_constitution.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_constitution.setStyleSheet("QCheckBox {    \n"
"    color: rgb(255, 224, 96);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.entity_change_status_constitution.setObjectName("entity_change_status_constitution")
        self.entity_change_status_intelligence = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_intelligence.setGeometry(QtCore.QRect(20, 290, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_intelligence.setFont(font)
        self.entity_change_status_intelligence.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_intelligence.setStyleSheet("QCheckBox {\n"
"    color: rgb(64, 192, 255);\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.entity_change_status_intelligence.setObjectName("entity_change_status_intelligence")
        self.entity_change_status_integrity = QtWidgets.QCheckBox(self.entity_change_frame)
        self.entity_change_status_integrity.setGeometry(QtCore.QRect(20, 320, 220, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.entity_change_status_integrity.setFont(font)
        self.entity_change_status_integrity.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_change_status_integrity.setStyleSheet("QCheckBox {\n"
"    color: white;\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 25px;\n"
"    min-height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.entity_change_status_integrity.setObjectName("entity_change_status_integrity")
        self.entity_stats_change_type_box = QtWidgets.QComboBox(self.entity_change_frame)
        self.entity_stats_change_type_box.setGeometry(QtCore.QRect(20, 360, 210, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entity_stats_change_type_box.sizePolicy().hasHeightForWidth())
        self.entity_stats_change_type_box.setSizePolicy(sizePolicy)
        self.entity_stats_change_type_box.setMinimumSize(QtCore.QSize(210, 40))
        self.entity_stats_change_type_box.setMaximumSize(QtCore.QSize(210, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.entity_stats_change_type_box.setFont(font)
        self.entity_stats_change_type_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.entity_stats_change_type_box.setStyleSheet("QComboBox {\n"
"    color: white;\n"
"    border: 0px;\n"
"    background: rgba(255,255,255,128);\n"
"}\n"
"QComboBox::down-arrow {\n"
"    background: rgba(0,0,0,0);\n"
"    size: 0;\n"
"}\n"
"QComboBox::drop-down {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 0px;\n"
"    size: 0;\n"
"    color: white;\n"
"}\n"
"QComboBox::editable {\n"
"    background: rgba(255,255,255,128);\n"
"    border: 0px;\n"
"    color: white;\n"
"}\n"
"QComboBox::editable:indicator {\n"
"    background: rgba(255,255,255,0);\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: white;\n"
"    background: rgba(255,255,255,64);\n"
"    selection-background-color: rgba(255,255,255,128);\n"
"    border: 0px;\n"
"    outline: 0px;\n"
"}")
        self.entity_stats_change_type_box.setEditable(False)
        self.entity_stats_change_type_box.setMaxCount(10)
        self.entity_stats_change_type_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.entity_stats_change_type_box.setFrame(False)
        self.entity_stats_change_type_box.setObjectName("entity_stats_change_type_box")
        self.entity_stats_change_type_box.addItem("")
        self.entity_stats_change_type_box.addItem("")
        self.entity_stats_change_type_box.addItem("")
        self.entity_stats_change_type_box.addItem("")
        self.change_label = QtWidgets.QLabel(self.entity_tab)
        self.change_label.setGeometry(QtCore.QRect(780, 0, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.change_label.setFont(font)
        self.change_label.setAlignment(QtCore.Qt.AlignCenter)
        self.change_label.setObjectName("change_label")
        self.enemy_add_button = QtWidgets.QPushButton(self.entity_tab)
        self.enemy_add_button.setGeometry(QtCore.QRect(10, 970, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.enemy_add_button.setFont(font)
        self.enemy_add_button.setToolTipDuration(1)
        self.enemy_add_button.setStyleSheet("#enemy_add_button {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: white;\n"
"\n"
"}\n"
"#enemy_add_button::hover {\n"
"border-image: url(:/bg/pane_thin_blue.png);\n"
"color: rgb(160,192,255);\n"
"}")
        self.enemy_add_button.setCheckable(False)
        self.enemy_add_button.setFlat(True)
        self.enemy_add_button.setObjectName("enemy_add_button")
        self.enemy_copy_button = QtWidgets.QPushButton(self.entity_tab)
        self.enemy_copy_button.setGeometry(QtCore.QRect(130, 970, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.enemy_copy_button.setFont(font)
        self.enemy_copy_button.setToolTipDuration(1)
        self.enemy_copy_button.setStyleSheet("#enemy_copy_button {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: white;\n"
"\n"
"}\n"
"#enemy_copy_button::hover {\n"
"border-image: url(:/bg/pane_thin_blue.png);\n"
"color: rgb(160,192,255);\n"
"}")
        self.enemy_copy_button.setCheckable(False)
        self.enemy_copy_button.setFlat(True)
        self.enemy_copy_button.setObjectName("enemy_copy_button")
        self.enemy_delete_button = QtWidgets.QPushButton(self.entity_tab)
        self.enemy_delete_button.setGeometry(QtCore.QRect(250, 970, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.enemy_delete_button.setFont(font)
        self.enemy_delete_button.setToolTipDuration(1)
        self.enemy_delete_button.setStyleSheet("#enemy_delete_button {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color:white;\n"
"\n"
"}\n"
"#enemy_delete_button::hover {\n"
"border-image: url(:/bg/pane_thin_blue.png);\n"
"color: rgb(160,192,255);\n"
"}")
        self.enemy_delete_button.setCheckable(False)
        self.enemy_delete_button.setFlat(True)
        self.enemy_delete_button.setObjectName("enemy_delete_button")
        self.entity_item_list = QtWidgets.QListWidget(self.entity_tab)
        self.entity_item_list.setGeometry(QtCore.QRect(1040, 40, 340, 400))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entity_item_list.sizePolicy().hasHeightForWidth())
        self.entity_item_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.entity_item_list.setFont(font)
        self.entity_item_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.entity_item_list.setStyleSheet("#entity_item_list {\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    outline: 0px;\n"
"}\n"
"#entity_item_list::item {\n"
"    font-size: 18px;\n"
"    font: bold \"Maiandra GD\";\n"
"    color: white;\n"
"}\n"
"#entity_item_list::item:selected {\n"
"    color: rgb(255,224,64);\n"
"    background: rgba(255,224,64,64);\n"
"    image: url(:/bg/checkmark.png);\n"
"    image-position: left;\n"
"}\n"
"#entity_item_list::item:focus {\n"
"    color: rgb(255,224,64);\n"
"    background: rgba(255,224,64,192);\n"
"}\n"
"#entity_item_list::item:!selected:!focus:hover {\n"
"    color: rgb(255,224,128);\n"
"    background: rgba(0,0,0,0);\n"
"}")
        self.entity_item_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.entity_item_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.entity_item_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.entity_item_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.entity_item_list.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.entity_item_list.setUniformItemSizes(True)
        self.entity_item_list.setBatchSize(15)
        self.entity_item_list.setObjectName("entity_item_list")
        self.entity_items_label = QtWidgets.QLabel(self.entity_tab)
        self.entity_items_label.setGeometry(QtCore.QRect(1040, 0, 340, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.entity_items_label.setFont(font)
        self.entity_items_label.setAlignment(QtCore.Qt.AlignCenter)
        self.entity_items_label.setObjectName("entity_items_label")
        self.player_search_box = QtWidgets.QLineEdit(self.entity_tab)
        self.player_search_box.setGeometry(QtCore.QRect(10, 40, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.player_search_box.setFont(font)
        self.player_search_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.player_search_box.setStyleSheet("QLineEdit {\n"
"border: 5px;\n"
"background-color:  rgba(255,255,255,0);\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: rgb(255,255,255);\n"
"}")
        self.player_search_box.setText("")
        self.player_search_box.setMaxLength(22)
        self.player_search_box.setAlignment(QtCore.Qt.AlignCenter)
        self.player_search_box.setDragEnabled(False)
        self.player_search_box.setObjectName("player_search_box")
        self.enemy_search_box = QtWidgets.QLineEdit(self.entity_tab)
        self.enemy_search_box.setGeometry(QtCore.QRect(10, 490, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.enemy_search_box.setFont(font)
        self.enemy_search_box.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.enemy_search_box.setStyleSheet("QLineEdit {\n"
"border: 5px;\n"
"background-color:  rgba(255,255,255,0);\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: rgb(255,255,255);\n"
"}\n"
"QLineEdit:hover {\n"
"    color: white;\n"
"}")
        self.enemy_search_box.setText("")
        self.enemy_search_box.setMaxLength(22)
        self.enemy_search_box.setAlignment(QtCore.Qt.AlignCenter)
        self.enemy_search_box.setDragEnabled(False)
        self.enemy_search_box.setObjectName("enemy_search_box")
        self.qc_tabs.addTab(self.entity_tab, "")
        self.item_tab = QtWidgets.QWidget()
        self.item_tab.setStyleSheet("#item_tab {\n"
"background-color: rgba(0,0,0,0);\n"
"border: 0px;\n"
"}")
        self.item_tab.setObjectName("item_tab")
        self.item_properties_frame = QtWidgets.QFrame(self.item_tab)
        self.item_properties_frame.setGeometry(QtCore.QRect(370, 40, 800, 975))
        self.item_properties_frame.setStyleSheet("#item_properties_frame {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"}")
        self.item_properties_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.item_properties_frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.item_properties_frame.setObjectName("item_properties_frame")
        self.item_attack_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_attack_box.setGeometry(QtCore.QRect(10, 270, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_attack_box.setFont(font)
        self.item_attack_box.setStyleSheet("#item_attack_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_attack_box.setWrapping(False)
        self.item_attack_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_attack_box.setProperty("showGroupSeparator", False)
        self.item_attack_box.setMinimum(-9999)
        self.item_attack_box.setMaximum(9999)
        self.item_attack_box.setProperty("value", 0)
        self.item_attack_box.setObjectName("item_attack_box")
        self.item_defense_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_defense_box.setGeometry(QtCore.QRect(10, 300, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_defense_box.setFont(font)
        self.item_defense_box.setStyleSheet("#item_defense_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_defense_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_defense_box.setProperty("showGroupSeparator", False)
        self.item_defense_box.setMinimum(-9999)
        self.item_defense_box.setMaximum(9999)
        self.item_defense_box.setProperty("value", 0)
        self.item_defense_box.setObjectName("item_defense_box")
        self.item_special_defense_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_special_defense_box.setGeometry(QtCore.QRect(10, 360, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_special_defense_box.setFont(font)
        self.item_special_defense_box.setStyleSheet("#item_special_defense_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_special_defense_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_special_defense_box.setProperty("showGroupSeparator", False)
        self.item_special_defense_box.setMinimum(-9999)
        self.item_special_defense_box.setMaximum(9999)
        self.item_special_defense_box.setProperty("value", 0)
        self.item_special_defense_box.setObjectName("item_special_defense_box")
        self.item_special_attack_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_special_attack_box.setGeometry(QtCore.QRect(10, 330, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_special_attack_box.setFont(font)
        self.item_special_attack_box.setStyleSheet("#item_special_attack_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_special_attack_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_special_attack_box.setProperty("showGroupSeparator", False)
        self.item_special_attack_box.setMinimum(-9999)
        self.item_special_attack_box.setMaximum(9999)
        self.item_special_attack_box.setProperty("value", 0)
        self.item_special_attack_box.setObjectName("item_special_attack_box")
        self.item_accuracy_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_accuracy_box.setGeometry(QtCore.QRect(10, 390, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_accuracy_box.setFont(font)
        self.item_accuracy_box.setStyleSheet("#item_accuracy_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_accuracy_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_accuracy_box.setProperty("showGroupSeparator", False)
        self.item_accuracy_box.setMinimum(-9999)
        self.item_accuracy_box.setMaximum(9999)
        self.item_accuracy_box.setProperty("value", 0)
        self.item_accuracy_box.setObjectName("item_accuracy_box")
        self.item_evasion_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_evasion_box.setGeometry(QtCore.QRect(10, 420, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_evasion_box.setFont(font)
        self.item_evasion_box.setStyleSheet("#item_evasion_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_evasion_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_evasion_box.setProperty("showGroupSeparator", False)
        self.item_evasion_box.setMinimum(-9999)
        self.item_evasion_box.setMaximum(9999)
        self.item_evasion_box.setProperty("value", 0)
        self.item_evasion_box.setObjectName("item_evasion_box")
        self.item_critical_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_critical_box.setGeometry(QtCore.QRect(10, 450, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_critical_box.setFont(font)
        self.item_critical_box.setStyleSheet("#item_critical_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_critical_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_critical_box.setProperty("showGroupSeparator", False)
        self.item_critical_box.setMinimum(-9999)
        self.item_critical_box.setMaximum(9999)
        self.item_critical_box.setProperty("value", 0)
        self.item_critical_box.setObjectName("item_critical_box")
        self.item_blessing_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_blessing_box.setGeometry(QtCore.QRect(10, 480, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_blessing_box.setFont(font)
        self.item_blessing_box.setStyleSheet("#item_blessing_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_blessing_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.item_blessing_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_blessing_box.setAccelerated(False)
        self.item_blessing_box.setProperty("showGroupSeparator", False)
        self.item_blessing_box.setSuffix("")
        self.item_blessing_box.setMinimum(-9999)
        self.item_blessing_box.setMaximum(9999)
        self.item_blessing_box.setProperty("value", 0)
        self.item_blessing_box.setObjectName("item_blessing_box")
        self.item_hp_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_hp_box.setGeometry(QtCore.QRect(10, 210, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_hp_box.setFont(font)
        self.item_hp_box.setStyleSheet("#item_hp_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(255,170,128);\n"
"}")
        self.item_hp_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_hp_box.setProperty("showGroupSeparator", False)
        self.item_hp_box.setMinimum(-999999)
        self.item_hp_box.setMaximum(999999)
        self.item_hp_box.setProperty("value", 0)
        self.item_hp_box.setObjectName("item_hp_box")
        self.item_sp_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_sp_box.setGeometry(QtCore.QRect(10, 240, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_sp_box.setFont(font)
        self.item_sp_box.setStyleSheet("#item_sp_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(170,255,128);\n"
"}")
        self.item_sp_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_sp_box.setProperty("showGroupSeparator", False)
        self.item_sp_box.setMinimum(-999999)
        self.item_sp_box.setMaximum(999999)
        self.item_sp_box.setProperty("value", 0)
        self.item_sp_box.setObjectName("item_sp_box")
        self.item_properties_equip_label = QtWidgets.QLabel(self.item_properties_frame)
        self.item_properties_equip_label.setGeometry(QtCore.QRect(10, 170, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.item_properties_equip_label.setFont(font)
        self.item_properties_equip_label.setStyleSheet("")
        self.item_properties_equip_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_properties_equip_label.setObjectName("item_properties_equip_label")
        self.item_properties_value_label = QtWidgets.QLabel(self.item_properties_frame)
        self.item_properties_value_label.setGeometry(QtCore.QRect(270, 40, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_properties_value_label.setFont(font)
        self.item_properties_value_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_properties_value_label.setObjectName("item_properties_value_label")
        self.item_gold_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_gold_box.setGeometry(QtCore.QRect(270, 80, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_gold_box.setFont(font)
        self.item_gold_box.setStyleSheet("#item_gold_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(255,236,90);\n"
"}")
        self.item_gold_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_gold_box.setProperty("showGroupSeparator", False)
        self.item_gold_box.setMinimum(0)
        self.item_gold_box.setMaximum(99999999)
        self.item_gold_box.setProperty("value", 0)
        self.item_gold_box.setObjectName("item_gold_box")
        self.item_jewels_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_jewels_box.setGeometry(QtCore.QRect(270, 110, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_jewels_box.setFont(font)
        self.item_jewels_box.setStyleSheet("#item_jewels_box {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: rgb(224,128,255);\n"
"}")
        self.item_jewels_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_jewels_box.setProperty("showGroupSeparator", False)
        self.item_jewels_box.setMinimum(0)
        self.item_jewels_box.setMaximum(9999999)
        self.item_jewels_box.setProperty("value", 0)
        self.item_jewels_box.setObjectName("item_jewels_box")
        self.item_properties_misc_label = QtWidgets.QLabel(self.item_properties_frame)
        self.item_properties_misc_label.setGeometry(QtCore.QRect(250, 400, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_properties_misc_label.setFont(font)
        self.item_properties_misc_label.setStyleSheet("")
        self.item_properties_misc_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_properties_misc_label.setObjectName("item_properties_misc_label")
        self.item_import_file_box = QtWidgets.QLineEdit(self.item_properties_frame)
        self.item_import_file_box.setGeometry(QtCore.QRect(250, 440, 245, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_import_file_box.setFont(font)
        self.item_import_file_box.setStyleSheet("#item_import_file_box {\n"
"    color: white;\n"
"    border: 0px;\n"
"    background: rgba(0,0,0,0);\n"
"}")
        self.item_import_file_box.setMaxLength(16)
        self.item_import_file_box.setAlignment(QtCore.Qt.AlignCenter)
        self.item_import_file_box.setObjectName("item_import_file_box")
        self.item_toggle_consumable_button = QtWidgets.QCheckBox(self.item_properties_frame)
        self.item_toggle_consumable_button.setGeometry(QtCore.QRect(270, 240, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.item_toggle_consumable_button.setFont(font)
        self.item_toggle_consumable_button.setStyleSheet("QCheckBox {\n"
"    color: white;\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.item_toggle_consumable_button.setObjectName("item_toggle_consumable_button")
        self.item_toggle_dual_wield_button = QtWidgets.QCheckBox(self.item_properties_frame)
        self.item_toggle_dual_wield_button.setGeometry(QtCore.QRect(270, 360, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.item_toggle_dual_wield_button.setFont(font)
        self.item_toggle_dual_wield_button.setStyleSheet("QCheckBox {\n"
"    color: white;\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.item_toggle_dual_wield_button.setObjectName("item_toggle_dual_wield_button")
        self.item_toggle_stackable_button = QtWidgets.QCheckBox(self.item_properties_frame)
        self.item_toggle_stackable_button.setGeometry(QtCore.QRect(270, 210, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.item_toggle_stackable_button.setFont(font)
        self.item_toggle_stackable_button.setStyleSheet("QCheckBox {\n"
"    color: white;\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.item_toggle_stackable_button.setObjectName("item_toggle_stackable_button")
        self.item_quantity_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_quantity_box.setGeometry(QtCore.QRect(270, 270, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_quantity_box.setFont(font)
        self.item_quantity_box.setStyleSheet("QSpinBox {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_quantity_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_quantity_box.setProperty("showGroupSeparator", False)
        self.item_quantity_box.setSuffix("")
        self.item_quantity_box.setMinimum(1)
        self.item_quantity_box.setMaximum(999)
        self.item_quantity_box.setProperty("value", 1)
        self.item_quantity_box.setObjectName("item_quantity_box")
        self.item_max_quantity_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_max_quantity_box.setGeometry(QtCore.QRect(270, 300, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_max_quantity_box.setFont(font)
        self.item_max_quantity_box.setStyleSheet("QSpinBox {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_max_quantity_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_max_quantity_box.setProperty("showGroupSeparator", False)
        self.item_max_quantity_box.setSuffix("")
        self.item_max_quantity_box.setMinimum(1)
        self.item_max_quantity_box.setMaximum(999)
        self.item_max_quantity_box.setProperty("value", 1)
        self.item_max_quantity_box.setObjectName("item_max_quantity_box")
        self.item_type_box = QtWidgets.QComboBox(self.item_properties_frame)
        self.item_type_box.setGeometry(QtCore.QRect(350, 330, 170, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_type_box.sizePolicy().hasHeightForWidth())
        self.item_type_box.setSizePolicy(sizePolicy)
        self.item_type_box.setMinimumSize(QtCore.QSize(170, 30))
        self.item_type_box.setMaximumSize(QtCore.QSize(170, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_type_box.setFont(font)
        self.item_type_box.setStyleSheet("QComboBox {\n"
"    color: white;\n"
"    border: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    background: rgba(0,0,0,0);\n"
"    max-width: 0px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 0px;\n"
"    max-width: 0px;\n"
"    color: white;\n"
"}\n"
"QComboBox::editable {\n"
"    background: rgba(255,224,255,64);\n"
"    border: 0px;\n"
"    color: white;\n"
"}\n"
"QComboBox::editable:indicator {\n"
"    background: rgba(255,224,255,0);\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: white;\n"
"    background: rgba(255,224,255,96);\n"
"    selection-background-color: rgba(255,224,255,128);\n"
"    border: 0px;\n"
"    outline: 0px;\n"
"}")
        self.item_type_box.setMaxCount(10)
        self.item_type_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLength)
        self.item_type_box.setFrame(False)
        self.item_type_box.setObjectName("item_type_box")
        self.item_type_box.addItem("")
        self.item_type_box.addItem("")
        self.item_type_box.addItem("")
        self.item_type_box.addItem("")
        self.item_type_box.addItem("")
        self.item_type_box.addItem("")
        self.item_type_box.addItem("")
        self.item_type_box.addItem("")
        self.item_type_box.addItem("")
        self.item_type_box.addItem("")
        self.item_properties_type_label = QtWidgets.QLabel(self.item_properties_frame)
        self.item_properties_type_label.setGeometry(QtCore.QRect(270, 330, 70, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_properties_type_label.setFont(font)
        self.item_properties_type_label.setStyleSheet("")
        self.item_properties_type_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.item_properties_type_label.setObjectName("item_properties_type_label")
        self.item_properties_requirements_label = QtWidgets.QLabel(self.item_properties_frame)
        self.item_properties_requirements_label.setGeometry(QtCore.QRect(10, 40, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.item_properties_requirements_label.setFont(font)
        self.item_properties_requirements_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_properties_requirements_label.setObjectName("item_properties_requirements_label")
        self.item_lvl_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_lvl_box.setGeometry(QtCore.QRect(10, 80, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_lvl_box.setFont(font)
        self.item_lvl_box.setStyleSheet("QSpinBox {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_lvl_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_lvl_box.setProperty("showGroupSeparator", False)
        self.item_lvl_box.setMinimum(0)
        self.item_lvl_box.setMaximum(999)
        self.item_lvl_box.setProperty("value", 0)
        self.item_lvl_box.setObjectName("item_lvl_box")
        self.item_max_level_box = QtWidgets.QSpinBox(self.item_properties_frame)
        self.item_max_level_box.setGeometry(QtCore.QRect(10, 110, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_max_level_box.setFont(font)
        self.item_max_level_box.setStyleSheet("QSpinBox {\n"
"border: 0px;\n"
"background-color: rgba(255,255,255,0);\n"
"color: white;\n"
"}")
        self.item_max_level_box.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.item_max_level_box.setProperty("showGroupSeparator", False)
        self.item_max_level_box.setMinimum(0)
        self.item_max_level_box.setMaximum(999)
        self.item_max_level_box.setProperty("value", 0)
        self.item_max_level_box.setObjectName("item_max_level_box")
        self.item_name_label = QtWidgets.QLabel(self.item_properties_frame)
        self.item_name_label.setGeometry(QtCore.QRect(10, 5, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.item_name_label.setFont(font)
        self.item_name_label.setStyleSheet("")
        self.item_name_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.item_name_label.setObjectName("item_name_label")
        self.item_name_box = QtWidgets.QLineEdit(self.item_properties_frame)
        self.item_name_box.setGeometry(QtCore.QRect(100, 5, 680, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.item_name_box.setFont(font)
        self.item_name_box.setStyleSheet("QLineEdit {\n"
"border: 0px;\n"
"background-color:  rgba(255,255,255,0);\n"
"color: rgb(255,255,225);\n"
"}")
        self.item_name_box.setText("")
        self.item_name_box.setMaxLength(25)
        self.item_name_box.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.item_name_box.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.item_name_box.setObjectName("item_name_box")
        self.item_toggle_consumable_button_2 = QtWidgets.QCheckBox(self.item_properties_frame)
        self.item_toggle_consumable_button_2.setGeometry(QtCore.QRect(10, 140, 250, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.item_toggle_consumable_button_2.setFont(font)
        self.item_toggle_consumable_button_2.setStyleSheet("QCheckBox {\n"
"    color: white;\n"
"}\n"
"QCheckBox::indicator {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    min-width: 20px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    image: url(:/bg/checkmark.png);\n"
"}\n"
"")
        self.item_toggle_consumable_button_2.setObjectName("item_toggle_consumable_button_2")
        self.item_properties_carry_label = QtWidgets.QLabel(self.item_properties_frame)
        self.item_properties_carry_label.setGeometry(QtCore.QRect(270, 170, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_properties_carry_label.setFont(font)
        self.item_properties_carry_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_properties_carry_label.setObjectName("item_properties_carry_label")
        self.item_restore_type_box = QtWidgets.QComboBox(self.item_properties_frame)
        self.item_restore_type_box.setGeometry(QtCore.QRect(590, 400, 70, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_restore_type_box.sizePolicy().hasHeightForWidth())
        self.item_restore_type_box.setSizePolicy(sizePolicy)
        self.item_restore_type_box.setMinimumSize(QtCore.QSize(70, 25))
        self.item_restore_type_box.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.item_restore_type_box.setFont(font)
        self.item_restore_type_box.setStyleSheet("QComboBox {\n"
"    color: white;\n"
"    border: 0px;\n"
"}\n"
"QComboBox::down-arrow {\n"
"    background: rgba(0,0,0,0);\n"
"    max-width: 0px;\n"
"}\n"
"QComboBox::drop-down {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 0px;\n"
"    max-width: 0px;\n"
"    color: white;\n"
"}\n"
"QComboBox::editable {\n"
"    background: rgba(255,224,64,128);\n"
"    border: 0px;\n"
"    color: white;\n"
"}\n"
"QComboBox::editable:indicator {\n"
"    background: rgba(255,224,64,0);\n"
"    border: 0px;\n"
"    margin: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    color: white;\n"
"    background: rgba(255,224,64,128);\n"
"    selection-background-color: rgba(255,224,64,128);\n"
"    border: 0px;\n"
"    outline: 0px;\n"
"}")
        self.item_restore_type_box.setEditable(False)
        self.item_restore_type_box.setMaxCount(10)
        self.item_restore_type_box.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.item_restore_type_box.setFrame(False)
        self.item_restore_type_box.setObjectName("item_restore_type_box")
        self.item_restore_type_box.addItem("")
        self.item_restore_type_box.addItem("")
        self.item_restore_type_box.addItem("")
        self.item_restore_type_box.addItem("")
        self.item_list = QtWidgets.QListWidget(self.item_tab)
        self.item_list.setGeometry(QtCore.QRect(10, 90, 350, 870))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.item_list.sizePolicy().hasHeightForWidth())
        self.item_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.item_list.setFont(font)
        self.item_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_list.setStyleSheet("QListWidget {\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    outline: 0px;\n"
"}\n"
"QListWidget::item {\n"
"    color: rgba(255,255,255,128);\n"
"    background: rgba(0,0,0,0);\n"
"}\n"
"QListWidget::item:selected {\n"
"    color: white;\n"
"    background: rgba(255,255,255,64);\n"
"    image: url(:/bg/checkmark.png);\n"
"    image-position: left;\n"
"}\n"
"QListWidget::item:focus {\n"
"    color: white;\n"
"    background: rgba(255,255,255,128);\n"
"}\n"
"QListWidget::item:!selected:!focus:hover {\n"
"    color: white;\n"
"}")
        self.item_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.item_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.item_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.item_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.item_list.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.item_list.setUniformItemSizes(True)
        self.item_list.setBatchSize(15)
        self.item_list.setObjectName("item_list")
        self.items_label = QtWidgets.QLabel(self.item_tab)
        self.items_label.setGeometry(QtCore.QRect(10, 0, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.items_label.setFont(font)
        self.items_label.setAlignment(QtCore.Qt.AlignCenter)
        self.items_label.setObjectName("items_label")
        self.item_properties_label = QtWidgets.QLabel(self.item_tab)
        self.item_properties_label.setGeometry(QtCore.QRect(370, 0, 800, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.item_properties_label.setFont(font)
        self.item_properties_label.setAlignment(QtCore.Qt.AlignCenter)
        self.item_properties_label.setObjectName("item_properties_label")
        self.item_delete_button = QtWidgets.QPushButton(self.item_tab)
        self.item_delete_button.setGeometry(QtCore.QRect(250, 970, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.item_delete_button.setFont(font)
        self.item_delete_button.setToolTipDuration(1)
        self.item_delete_button.setStyleSheet("QPushButton {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"border-image: url(:/bg/pane_thin_blue.png);\n"
"color: rgb(160,192,255);\n"
"}")
        self.item_delete_button.setCheckable(False)
        self.item_delete_button.setFlat(True)
        self.item_delete_button.setObjectName("item_delete_button")
        self.item_add_button = QtWidgets.QPushButton(self.item_tab)
        self.item_add_button.setGeometry(QtCore.QRect(10, 970, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.item_add_button.setFont(font)
        self.item_add_button.setToolTipDuration(1)
        self.item_add_button.setStyleSheet("QPushButton {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"border-image: url(:/bg/pane_thin_blue.png);\n"
"color: rgb(160,192,255);\n"
"}")
        self.item_add_button.setCheckable(False)
        self.item_add_button.setFlat(True)
        self.item_add_button.setObjectName("item_add_button")
        self.item_copy_button = QtWidgets.QPushButton(self.item_tab)
        self.item_copy_button.setGeometry(QtCore.QRect(130, 970, 110, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.item_copy_button.setFont(font)
        self.item_copy_button.setToolTipDuration(1)
        self.item_copy_button.setStyleSheet("QPushButton {\n"
"border: 5px;\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: white;\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"border-image: url(:/bg/pane_thin_blue.png);\n"
"color: rgb(160,192,255);\n"
"}")
        self.item_copy_button.setCheckable(False)
        self.item_copy_button.setFlat(True)
        self.item_copy_button.setObjectName("item_copy_button")
        self.item_search_box = QtWidgets.QLineEdit(self.item_tab)
        self.item_search_box.setGeometry(QtCore.QRect(10, 40, 350, 40))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.item_search_box.setFont(font)
        self.item_search_box.setStyleSheet("QLineEdit {\n"
"border: 5px;\n"
"background-color:  rgba(255,255,255,0);\n"
"border-image: url(:/bg/pane_thin_yellow.png);\n"
"color: rgb(255,255,255);\n"
"}")
        self.item_search_box.setInputMask("")
        self.item_search_box.setText("")
        self.item_search_box.setMaxLength(25)
        self.item_search_box.setAlignment(QtCore.Qt.AlignCenter)
        self.item_search_box.setDragEnabled(False)
        self.item_search_box.setObjectName("item_search_box")
        self.qc_tabs.addTab(self.item_tab, "")
        self.skill_tab = QtWidgets.QWidget()
        self.skill_tab.setStyleSheet("#skill_tab {\n"
"background-color: rgba(0,0,0,0);\n"
"border: 0px;\n"
"}")
        self.skill_tab.setObjectName("skill_tab")
        self.qc_tabs.addTab(self.skill_tab, "")
        self.effect_tab = QtWidgets.QWidget()
        self.effect_tab.setStyleSheet("#effect_tab {\n"
"background-color: rgba(0,0,0,0);\n"
"border: 0px;\n"
"}")
        self.effect_tab.setObjectName("effect_tab")
        self.qc_tabs.addTab(self.effect_tab, "")
        self.battle_tab = QtWidgets.QWidget()
        self.battle_tab.setStyleSheet("#battle_tab {\n"
"background-color: rgba(0,0,0,0);\n"
"border: 0px;\n"
"}")
        self.battle_tab.setObjectName("battle_tab")
        self.battle_player_list = QtWidgets.QListWidget(self.battle_tab)
        self.battle_player_list.setGeometry(QtCore.QRect(10, 10, 200, 250))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.battle_player_list.sizePolicy().hasHeightForWidth())
        self.battle_player_list.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(14)
        self.battle_player_list.setFont(font)
        self.battle_player_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.battle_player_list.setStyleSheet("#player_list {\n"
"    border: 5px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    outline: 0px;\n"
"}\n"
"#player_list::item {\n"
"    font-size: 18px;\n"
"    font: bold \"Maiandra GD\";\n"
"    color: white;\n"
"    background: rgba(0,0,0,0);\n"
"}\n"
"#player_list::item:selected {\n"
"    color: rgb(255,224,64);\n"
"    image: url(:/bg/checkmark.png);\n"
"    image-position: left;\n"
"}\n"
"#player_list::item:focus {\n"
"    color: rgb(255,224,64);\n"
"    background: rgba(255,224,64,192);\n"
"}\n"
"#player_list::item:!selected:!focus:hover {\n"
"    color: rgb(255,224,128)\n"
"}")
        self.battle_player_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.battle_player_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.battle_player_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.battle_player_list.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.battle_player_list.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.battle_player_list.setFlow(QtWidgets.QListView.TopToBottom)
        self.battle_player_list.setUniformItemSizes(True)
        self.battle_player_list.setBatchSize(15)
        self.battle_player_list.setObjectName("battle_player_list")
        self.qc_tabs.addTab(self.battle_tab, "")
        self.quest_tab = QtWidgets.QWidget()
        self.quest_tab.setStyleSheet("#quest_tab { \n"
"background-color: rgba(0,0,0,0);\n"
"border: 0px;\n"
"}")
        self.quest_tab.setObjectName("quest_tab")
        self.qc_tabs.addTab(self.quest_tab, "")
        self.shop_tab = QtWidgets.QWidget()
        self.shop_tab.setStyleSheet("#shop_tab {\n"
"background-color: rgba(0,0,0,0);\n"
"border: 0px;\n"
"}")
        self.shop_tab.setObjectName("shop_tab")
        self.qc_tabs.addTab(self.shop_tab, "")
        self.music_tab = QtWidgets.QWidget()
        self.music_tab.setStyleSheet("#music_tab {\n"
"background-color: rgba(0,0,0,0);\n"
"border: 0px;\n"
"}")
        self.music_tab.setObjectName("music_tab")
        self.qc_tabs.addTab(self.music_tab, "")
        self.option_tab = QtWidgets.QWidget()
        self.option_tab.setStyleSheet("#option_tab {\n"
"background-color: rgba(0,0,0,0);\n"
"border: 0px;\n"
"}")
        self.option_tab.setObjectName("option_tab")
        self.qc_tabs.addTab(self.option_tab, "")
        self.output_label = QtWidgets.QLabel(self.active_file_page)
        self.output_label.setGeometry(QtCore.QRect(0, 20, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.output_label.setFont(font)
        self.output_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label.setObjectName("output_label")
        self.last_activity_label = QtWidgets.QLabel(self.active_file_page)
        self.last_activity_label.setGeometry(QtCore.QRect(0, 0, 300, 30))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.last_activity_label.setFont(font)
        self.last_activity_label.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.last_activity_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.last_activity_label.setObjectName("last_activity_label")
        self.output_list = QtWidgets.QListWidget(self.active_file_page)
        self.output_list.setGeometry(QtCore.QRect(0, 75, 300, 975))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_list.sizePolicy().hasHeightForWidth())
        self.output_list.setSizePolicy(sizePolicy)
        self.output_list.setMinimumSize(QtCore.QSize(200, 600))
        self.output_list.setMaximumSize(QtCore.QSize(300, 1005))
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.output_list.setFont(font)
        self.output_list.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.output_list.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.output_list.setStyleSheet("QListWidget {\n"
"    background: rgba(0,0,0,0);\n"
"    border: 5px;\n"
"    outline: 0px;\n"
"    border-image: url(:/bg/pane_thin_yellow.png);\n"
"    color: white;\n"
"}\n"
"QListWidget::item {\n"
"    outline: 0px;\n"
"}\n"
"QListWidget::item:indicator {\n"
"    outline: 0px;\n"
"    border: 0px;\n"
"}\n"
"QListWidget::item:hover {\n"
"    background: rgba(255,255,255,128);\n"
"}")
        self.output_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.output_list.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.output_list.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.output_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.output_list.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.output_list.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.output_list.setUniformItemSizes(True)
        self.output_list.setBatchSize(15)
        self.output_list.setWordWrap(True)
        self.output_list.setObjectName("output_list")
        self.stackedWidget.addWidget(self.active_file_page)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        self.qc_tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.file_select_button2.setText(_translate("MainWindow", "2"))
        self.qc_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:72pt; color:#ffffff;\">Quest Calculator</span></p></body></html>"))
        self.file_select_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">Profile Select</span></p></body></html>"))
        self.file_select_label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600; font-style:italic; color:#ffffff;\">Select your profile to load it</span></p></body></html>"))
        self.file_select_button3.setText(_translate("MainWindow", "3"))
        self.file_select_button1.setText(_translate("MainWindow", "1"))
        self.player_list.setSortingEnabled(True)
        self.players_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Players</span></p></body></html>"))
        self.entity_name_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffffff;\">Name</span></p></body></html>"))
        self.entity_exp_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaffff;\">XP</span></p></body></html>"))
        self.entity_exp_bar.setFormat(_translate("MainWindow", "%v/%m"))
        self.player_attack_change_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.player_critical_change_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.entity_hp_bar.setFormat(_translate("MainWindow", "%v/%m"))
        self.entity_food_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffff7f;\">Food</span></p></body></html>"))
        self.entity_sp_bar.setFormat(_translate("MainWindow", "%v/%m"))
        self.entity_food_bar.setFormat(_translate("MainWindow", "%v/%m"))
        self.entity_sp_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#aaff7f;\">SP</span></p></body></html>"))
        self.entity_hp_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffaa7f;\">HP</span></p></body></html>"))
        self.player_special_defense_change_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.player_defense_change_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.player_blessing_change_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.player_accuracy_change_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.player_evasion_change_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.player_special_attack_change_label.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.entity_level_box.setPrefix(_translate("MainWindow", "Level  "))
        self.entity_element_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Element</span></p></body></html>"))
        self.entity_gold_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#ffec5a;\">Gold</span></p></body></html>"))
        self.entity_gold_label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; color:#e060ff;\">Jewels</span></p></body></html>"))
        self.entity_strength_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffaa60;\">Strength</span></p></body></html>"))
        self.entity_dexterity_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#55ff7f;\">Dexterity</span></p></body></html>"))
        self.entity_constitution_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffe060;\">Constitution</span></p></body></html>"))
        self.entity_intelligence_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#40c0ff;\">Intelligence</span></p></body></html>"))
        self.entity_integrity_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Integrity</span></p></body></html>"))
        self.entity_attack_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Attack</span></p></body></html>"))
        self.entity_defense_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Defense</span></p></body></html>"))
        self.entity_special_defense_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Special Defense</span></p></body></html>"))
        self.entity_special_attack_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Special Attack</span></p></body></html>"))
        self.entity_accuracy_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Accuracy</span></p></body></html>"))
        self.entity_evasion_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Evasion</span></p></body></html>"))
        self.entity_critical_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Critical</span></p></body></html>"))
        self.entity_blessing_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Blessing</span></p></body></html>"))
        self.general_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Entity Data</span></p></body></html>"))
        self.enemy_list.setSortingEnabled(True)
        self.enemies_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Enemies</span></p></body></html>"))
        self.player_add_button.setToolTip(_translate("MainWindow", "Add a player"))
        self.player_add_button.setText(_translate("MainWindow", "Add"))
        self.player_delete_button.setToolTip(_translate("MainWindow", "Add a player"))
        self.player_delete_button.setText(_translate("MainWindow", "Delete"))
        self.player_copy_button.setToolTip(_translate("MainWindow", "Duplicate a player"))
        self.player_copy_button.setText(_translate("MainWindow", "Copy"))
        self.entity_change_status_gold.setText(_translate("MainWindow", "Gold"))
        self.entity_change_status_jewels.setText(_translate("MainWindow", "Jewels"))
        self.entity_change_status_exp.setText(_translate("MainWindow", "XP"))
        self.entity_change_status_hp.setText(_translate("MainWindow", "HP"))
        self.entity_change_status_sp.setText(_translate("MainWindow", "SP"))
        self.entity_change_status_food.setText(_translate("MainWindow", "Food"))
        self.entity_stats_change_add_button.setToolTip(_translate("MainWindow", "Add a player"))
        self.entity_stats_change_add_button.setText(_translate("MainWindow", "Add"))
        self.entity_stats_change_set_button.setToolTip(_translate("MainWindow", "Add a player"))
        self.entity_stats_change_set_button.setText(_translate("MainWindow", "Set"))
        self.entity_change_status_strength.setText(_translate("MainWindow", "Strength"))
        self.entity_change_status_dexterity.setText(_translate("MainWindow", "Dexterity"))
        self.entity_change_status_constitution.setText(_translate("MainWindow", "Constitution"))
        self.entity_change_status_intelligence.setText(_translate("MainWindow", "Intelligence"))
        self.entity_change_status_integrity.setText(_translate("MainWindow", "Integrity"))
        self.entity_stats_change_type_box.setItemText(0, _translate("MainWindow", "Fixed"))
        self.entity_stats_change_type_box.setItemText(1, _translate("MainWindow", "Percent"))
        self.entity_stats_change_type_box.setItemText(2, _translate("MainWindow", "Lost"))
        self.entity_stats_change_type_box.setItemText(3, _translate("MainWindow", "Max"))
        self.change_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Change Status</span></p></body></html>"))
        self.enemy_add_button.setToolTip(_translate("MainWindow", "Add a player"))
        self.enemy_add_button.setText(_translate("MainWindow", "Add"))
        self.enemy_copy_button.setToolTip(_translate("MainWindow", "Duplicate a player"))
        self.enemy_copy_button.setText(_translate("MainWindow", "Copy"))
        self.enemy_delete_button.setToolTip(_translate("MainWindow", "Add a player"))
        self.enemy_delete_button.setText(_translate("MainWindow", "Delete"))
        self.entity_items_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Entity Items</span></p></body></html>"))
        self.player_search_box.setPlaceholderText(_translate("MainWindow", "Search For Player"))
        self.enemy_search_box.setPlaceholderText(_translate("MainWindow", "Search For Enemy"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.entity_tab), _translate("MainWindow", "Entity"))
        self.item_attack_box.setPrefix(_translate("MainWindow", "Attack          "))
        self.item_defense_box.setPrefix(_translate("MainWindow", "Defense        "))
        self.item_special_defense_box.setPrefix(_translate("MainWindow", "SP Defense    "))
        self.item_special_attack_box.setPrefix(_translate("MainWindow", "SP Attack      "))
        self.item_accuracy_box.setPrefix(_translate("MainWindow", "Accuracy       "))
        self.item_evasion_box.setPrefix(_translate("MainWindow", "Evasion         "))
        self.item_critical_box.setPrefix(_translate("MainWindow", "Critical          "))
        self.item_blessing_box.setPrefix(_translate("MainWindow", "Blessing         "))
        self.item_hp_box.setPrefix(_translate("MainWindow", "HP     "))
        self.item_sp_box.setPrefix(_translate("MainWindow", "SP      "))
        self.item_properties_equip_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#ffffff;\">Equipped Bonuses</span></p></body></html>"))
        self.item_properties_value_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-style:italic; color:#ffffff;\">Value</span></p></body></html>"))
        self.item_gold_box.setPrefix(_translate("MainWindow", "Gold     "))
        self.item_jewels_box.setPrefix(_translate("MainWindow", "Jewels    "))
        self.item_properties_misc_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-style:italic; color:#ffffff;\">Miscellaneous</span></p></body></html>"))
        self.item_import_file_box.setPlaceholderText(_translate("MainWindow", "default standard"))
        self.item_toggle_consumable_button.setText(_translate("MainWindow", "Consumable"))
        self.item_toggle_dual_wield_button.setText(_translate("MainWindow", "Dual Wield"))
        self.item_toggle_stackable_button.setText(_translate("MainWindow", "Stackable"))
        self.item_quantity_box.setPrefix(_translate("MainWindow", "Quantity: "))
        self.item_max_quantity_box.setPrefix(_translate("MainWindow", "Max: "))
        self.item_type_box.setItemText(0, _translate("MainWindow", "Weapon"))
        self.item_type_box.setItemText(1, _translate("MainWindow", "Ammo"))
        self.item_type_box.setItemText(2, _translate("MainWindow", "Head"))
        self.item_type_box.setItemText(3, _translate("MainWindow", "Chest"))
        self.item_type_box.setItemText(4, _translate("MainWindow", "Back"))
        self.item_type_box.setItemText(5, _translate("MainWindow", "Hands"))
        self.item_type_box.setItemText(6, _translate("MainWindow", "Legs"))
        self.item_type_box.setItemText(7, _translate("MainWindow", "Feet"))
        self.item_type_box.setItemText(8, _translate("MainWindow", "Accessory"))
        self.item_type_box.setItemText(9, _translate("MainWindow", "Item"))
        self.item_properties_type_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#ffffff;\">Type</span></p></body></html>"))
        self.item_properties_requirements_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-style:italic; color:#ffffff;\">Requirements</span></p></body></html>"))
        self.item_lvl_box.setPrefix(_translate("MainWindow", "Level "))
        self.item_max_level_box.setPrefix(_translate("MainWindow", "Max Level "))
        self.item_name_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Name</span></p></body></html>"))
        self.item_toggle_consumable_button_2.setText(_translate("MainWindow", "Requires Ammo"))
        self.item_properties_carry_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:20pt; font-style:italic; color:#ffffff;\">Carry</span></p></body></html>"))
        self.item_restore_type_box.setItemText(0, _translate("MainWindow", "Fixed"))
        self.item_restore_type_box.setItemText(1, _translate("MainWindow", "Lost"))
        self.item_restore_type_box.setItemText(2, _translate("MainWindow", "Max"))
        self.item_restore_type_box.setItemText(3, _translate("MainWindow", "Damage"))
        self.item_list.setSortingEnabled(True)
        self.items_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Items</span></p></body></html>"))
        self.item_properties_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; color:#ffffff;\">Properties</span></p></body></html>"))
        self.item_delete_button.setToolTip(_translate("MainWindow", "Add a player"))
        self.item_delete_button.setText(_translate("MainWindow", "Delete"))
        self.item_add_button.setToolTip(_translate("MainWindow", "Add a player"))
        self.item_add_button.setText(_translate("MainWindow", "Add"))
        self.item_copy_button.setToolTip(_translate("MainWindow", "Duplicate a player"))
        self.item_copy_button.setText(_translate("MainWindow", "Copy"))
        self.item_search_box.setPlaceholderText(_translate("MainWindow", "Search For Item"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.item_tab), _translate("MainWindow", "Item"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.skill_tab), _translate("MainWindow", "Skill"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.effect_tab), _translate("MainWindow", "Effect"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.battle_tab), _translate("MainWindow", "Battle"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.quest_tab), _translate("MainWindow", "Quest"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.shop_tab), _translate("MainWindow", "Shop"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.music_tab), _translate("MainWindow", "Music"))
        self.qc_tabs.setTabText(self.qc_tabs.indexOf(self.option_tab), _translate("MainWindow", "Options"))
        self.output_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ffffff;\">Output</span></p></body></html>"))
        self.last_activity_label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; color:#ffffff;\">Last Activity: </span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

