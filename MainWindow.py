# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 550)
        MainWindow.setMinimumSize(QtCore.QSize(750, 550))
        MainWindow.setMaximumSize(QtCore.QSize(750, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(750, 550))
        self.centralwidget.setMaximumSize(QtCore.QSize(750, 550))
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 750, 550))
        self.stackedWidget.setMinimumSize(QtCore.QSize(750, 550))
        self.stackedWidget.setMaximumSize(QtCore.QSize(750, 550))
        self.stackedWidget.setObjectName("stackedWidget")
        self.start = QtWidgets.QWidget()
        self.start.setObjectName("start")
        self.gridLayout = QtWidgets.QGridLayout(self.start)
        self.gridLayout.setObjectName("gridLayout")
        self.send_btn = QtWidgets.QPushButton(self.start)
        self.send_btn.setMinimumSize(QtCore.QSize(300, 40))
        self.send_btn.setMaximumSize(QtCore.QSize(300, 40))
        self.send_btn.setObjectName("send_btn")
        self.gridLayout.addWidget(self.send_btn, 0, 0, 1, 1)
        self.receive_btn = QtWidgets.QPushButton(self.start)
        self.receive_btn.setMinimumSize(QtCore.QSize(300, 40))
        self.receive_btn.setMaximumSize(QtCore.QSize(300, 40))
        self.receive_btn.setObjectName("receive_btn")
        self.gridLayout.addWidget(self.receive_btn, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.start)
        self.send = QtWidgets.QWidget()
        self.send.setObjectName("send")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.send)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.connectionGroupBox = QtWidgets.QGroupBox(self.send)
        self.connectionGroupBox.setMinimumSize(QtCore.QSize(700, 0))
        self.connectionGroupBox.setMaximumSize(QtCore.QSize(700, 16777215))
        self.connectionGroupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.connectionGroupBox.setObjectName("connectionGroupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.connectionGroupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.connectionLbl = QtWidgets.QLabel(self.connectionGroupBox)
        self.connectionLbl.setMinimumSize(QtCore.QSize(650, 23))
        self.connectionLbl.setMaximumSize(QtCore.QSize(650, 23))
        self.connectionLbl.setText("")
        self.connectionLbl.setObjectName("connectionLbl")
        self.gridLayout_2.addWidget(self.connectionLbl, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(281, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 1, 0, 1, 1)
        self.disconnectBtn = QtWidgets.QPushButton(self.connectionGroupBox)
        self.disconnectBtn.setMinimumSize(QtCore.QSize(100, 23))
        self.disconnectBtn.setMaximumSize(QtCore.QSize(100, 23))
        self.disconnectBtn.setObjectName("disconnectBtn")
        self.gridLayout_2.addWidget(self.disconnectBtn, 1, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(281, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 1, 2, 1, 1)
        self.gridLayout_9.addWidget(self.connectionGroupBox, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.send)
        self.receive = QtWidgets.QWidget()
        self.receive.setObjectName("receive")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.receive)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.searchGroupBox = QtWidgets.QGroupBox(self.receive)
        self.searchGroupBox.setMinimumSize(QtCore.QSize(700, 150))
        self.searchGroupBox.setMaximumSize(QtCore.QSize(700, 150))
        self.searchGroupBox.setObjectName("searchGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.searchGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem2, 4, 0, 1, 1)
        self.searchInput_2 = QtWidgets.QLineEdit(self.searchGroupBox)
        self.searchInput_2.setMinimumSize(QtCore.QSize(250, 23))
        self.searchInput_2.setMaximumSize(QtCore.QSize(250, 23))
        self.searchInput_2.setObjectName("searchInput_2")
        self.gridLayout_7.addWidget(self.searchInput_2, 0, 2, 1, 1)
        self.ipRadio_2 = QtWidgets.QRadioButton(self.searchGroupBox)
        self.ipRadio_2.setMinimumSize(QtCore.QSize(145, 20))
        self.ipRadio_2.setMaximumSize(QtCore.QSize(145, 20))
        self.ipRadio_2.setObjectName("ipRadio_2")
        self.gridLayout_7.addWidget(self.ipRadio_2, 0, 0, 1, 1)
        self.searchBtn_2 = QtWidgets.QPushButton(self.searchGroupBox)
        self.searchBtn_2.setMinimumSize(QtCore.QSize(100, 23))
        self.searchBtn_2.setMaximumSize(QtCore.QSize(100, 23))
        self.searchBtn_2.setObjectName("searchBtn_2")
        self.gridLayout_7.addWidget(self.searchBtn_2, 0, 3, 1, 1)
        self.networkRadio_2 = QtWidgets.QRadioButton(self.searchGroupBox)
        self.networkRadio_2.setMinimumSize(QtCore.QSize(145, 20))
        self.networkRadio_2.setMaximumSize(QtCore.QSize(145, 20))
        self.networkRadio_2.setObjectName("networkRadio_2")
        self.gridLayout_7.addWidget(self.networkRadio_2, 2, 0, 1, 1)
        self.nameRadio_2 = QtWidgets.QRadioButton(self.searchGroupBox)
        self.nameRadio_2.setMinimumSize(QtCore.QSize(145, 20))
        self.nameRadio_2.setMaximumSize(QtCore.QSize(145, 20))
        self.nameRadio_2.setObjectName("nameRadio_2")
        self.gridLayout_7.addWidget(self.nameRadio_2, 1, 0, 1, 1)
        self.optionsCombo_2 = QtWidgets.QComboBox(self.searchGroupBox)
        self.optionsCombo_2.setMinimumSize(QtCore.QSize(250, 23))
        self.optionsCombo_2.setMaximumSize(QtCore.QSize(250, 23))
        self.optionsCombo_2.setObjectName("optionsCombo_2")
        self.gridLayout_7.addWidget(self.optionsCombo_2, 2, 2, 1, 1)
        self.connectBtn_2 = QtWidgets.QPushButton(self.searchGroupBox)
        self.connectBtn_2.setMinimumSize(QtCore.QSize(100, 23))
        self.connectBtn_2.setMaximumSize(QtCore.QSize(100, 23))
        self.connectBtn_2.setObjectName("connectBtn_2")
        self.gridLayout_7.addWidget(self.connectBtn_2, 2, 3, 1, 1)
        self.previousRadio_2 = QtWidgets.QRadioButton(self.searchGroupBox)
        self.previousRadio_2.setMinimumSize(QtCore.QSize(145, 20))
        self.previousRadio_2.setMaximumSize(QtCore.QSize(145, 20))
        self.previousRadio_2.setObjectName("previousRadio_2")
        self.gridLayout_7.addWidget(self.previousRadio_2, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem3, 1, 3, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem4, 1, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem5, 3, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem6, 3, 3, 1, 1)
        self.searchLbl_2 = QtWidgets.QLabel(self.searchGroupBox)
        self.searchLbl_2.setMinimumSize(QtCore.QSize(100, 23))
        self.searchLbl_2.setMaximumSize(QtCore.QSize(100, 23))
        self.searchLbl_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.searchLbl_2.setObjectName("searchLbl_2")
        self.gridLayout_7.addWidget(self.searchLbl_2, 0, 1, 1, 1)
        self.selectLbl_2 = QtWidgets.QLabel(self.searchGroupBox)
        self.selectLbl_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.selectLbl_2.setObjectName("selectLbl_2")
        self.gridLayout_7.addWidget(self.selectLbl_2, 2, 1, 1, 1)
        self.gridLayout_8.addWidget(self.searchGroupBox, 0, 0, 1, 1)
        self.connectionGroupBox_2 = QtWidgets.QGroupBox(self.receive)
        self.connectionGroupBox_2.setMinimumSize(QtCore.QSize(700, 120))
        self.connectionGroupBox_2.setMaximumSize(QtCore.QSize(700, 120))
        self.connectionGroupBox_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.connectionGroupBox_2.setObjectName("connectionGroupBox_2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.connectionGroupBox_2)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.connectionLbl_2 = QtWidgets.QLabel(self.connectionGroupBox_2)
        self.connectionLbl_2.setMinimumSize(QtCore.QSize(650, 23))
        self.connectionLbl_2.setMaximumSize(QtCore.QSize(700, 23))
        self.connectionLbl_2.setText("")
        self.connectionLbl_2.setAlignment(QtCore.Qt.AlignCenter)
        self.connectionLbl_2.setObjectName("connectionLbl_2")
        self.gridLayout_5.addWidget(self.connectionLbl_2, 0, 0, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(281, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem7, 1, 0, 1, 1)
        self.disconnectBtn_2 = QtWidgets.QPushButton(self.connectionGroupBox_2)
        self.disconnectBtn_2.setMinimumSize(QtCore.QSize(100, 23))
        self.disconnectBtn_2.setMaximumSize(QtCore.QSize(100, 23))
        self.disconnectBtn_2.setObjectName("disconnectBtn_2")
        self.gridLayout_5.addWidget(self.disconnectBtn_2, 1, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(281, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem8, 1, 2, 1, 1)
        self.gridLayout_8.addWidget(self.connectionGroupBox_2, 1, 0, 1, 1)
        self.syncGroupBox = QtWidgets.QGroupBox(self.receive)
        self.syncGroupBox.setMinimumSize(QtCore.QSize(700, 180))
        self.syncGroupBox.setMaximumSize(QtCore.QSize(700, 180))
        self.syncGroupBox.setObjectName("syncGroupBox")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.syncGroupBox)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem9, 5, 6, 1, 1)
        self.folderLbl_2 = QtWidgets.QLabel(self.syncGroupBox)
        self.folderLbl_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.folderLbl_2.setObjectName("folderLbl_2")
        self.gridLayout_6.addWidget(self.folderLbl_2, 3, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(118, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem10, 5, 2, 1, 1)
        self.drivesComboBox_2 = QtWidgets.QComboBox(self.syncGroupBox)
        self.drivesComboBox_2.setMaximumSize(QtCore.QSize(60, 16777215))
        self.drivesComboBox_2.setObjectName("drivesComboBox_2")
        self.gridLayout_6.addWidget(self.drivesComboBox_2, 1, 2, 1, 1)
        self.rbBtn_2 = QtWidgets.QPushButton(self.syncGroupBox)
        self.rbBtn_2.setMinimumSize(QtCore.QSize(120, 23))
        self.rbBtn_2.setMaximumSize(QtCore.QSize(120, 23))
        self.rbBtn_2.setObjectName("rbBtn_2")
        self.gridLayout_6.addWidget(self.rbBtn_2, 5, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem11, 6, 2, 1, 1)
        self.folderInput_2 = QtWidgets.QLineEdit(self.syncGroupBox)
        self.folderInput_2.setMinimumSize(QtCore.QSize(382, 23))
        self.folderInput_2.setMaximumSize(QtCore.QSize(382, 23))
        self.folderInput_2.setObjectName("folderInput_2")
        self.gridLayout_6.addWidget(self.folderInput_2, 3, 2, 1, 3)
        self.audioBtn_2 = QtWidgets.QPushButton(self.syncGroupBox)
        self.audioBtn_2.setMinimumSize(QtCore.QSize(120, 23))
        self.audioBtn_2.setMaximumSize(QtCore.QSize(120, 23))
        self.audioBtn_2.setObjectName("audioBtn_2")
        self.gridLayout_6.addWidget(self.audioBtn_2, 5, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem12, 4, 1, 1, 1)
        self.drivesLbl_2 = QtWidgets.QLabel(self.syncGroupBox)
        self.drivesLbl_2.setMinimumSize(QtCore.QSize(130, 23))
        self.drivesLbl_2.setMaximumSize(QtCore.QSize(130, 23))
        self.drivesLbl_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.drivesLbl_2.setObjectName("drivesLbl_2")
        self.gridLayout_6.addWidget(self.drivesLbl_2, 1, 1, 1, 1)
        self.allBtn_2 = QtWidgets.QPushButton(self.syncGroupBox)
        self.allBtn_2.setMinimumSize(QtCore.QSize(120, 23))
        self.allBtn_2.setMaximumSize(QtCore.QSize(120, 23))
        self.allBtn_2.setObjectName("allBtn_2")
        self.gridLayout_6.addWidget(self.allBtn_2, 5, 5, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem13, 2, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(118, 15, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem14, 5, 4, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem15, 0, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem16, 5, 0, 1, 1)
        self.musicFolderBtn_2 = QtWidgets.QToolButton(self.syncGroupBox)
        self.musicFolderBtn_2.setMinimumSize(QtCore.QSize(25, 23))
        self.musicFolderBtn_2.setMaximumSize(QtCore.QSize(25, 23))
        self.musicFolderBtn_2.setObjectName("musicFolderBtn_2")
        self.gridLayout_6.addWidget(self.musicFolderBtn_2, 3, 5, 1, 1)
        self.gridLayout_8.addWidget(self.syncGroupBox, 2, 0, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem17, 3, 0, 1, 1)
        self.stackedWidget.addWidget(self.receive)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSettings = QtWidgets.QAction(MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.send_btn.setText(_translate("MainWindow", "Send"))
        self.receive_btn.setText(_translate("MainWindow", "Receive"))
        self.connectionGroupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.disconnectBtn.setText(_translate("MainWindow", "Disconnect"))
        self.searchGroupBox.setTitle(_translate("MainWindow", "Search"))
        self.ipRadio_2.setText(_translate("MainWindow", "Local IP Address"))
        self.searchBtn_2.setText(_translate("MainWindow", "Search"))
        self.networkRadio_2.setText(_translate("MainWindow", "Scan Network"))
        self.nameRadio_2.setText(_translate("MainWindow", "Computer Name"))
        self.connectBtn_2.setText(_translate("MainWindow", "Connect"))
        self.previousRadio_2.setText(_translate("MainWindow", "Previous Connections"))
        self.searchLbl_2.setText(_translate("MainWindow", "Search:"))
        self.selectLbl_2.setText(_translate("MainWindow", "Select:"))
        self.connectionGroupBox_2.setTitle(_translate("MainWindow", "Connection"))
        self.disconnectBtn_2.setText(_translate("MainWindow", "Disconnect"))
        self.syncGroupBox.setTitle(_translate("MainWindow", "Sync"))
        self.folderLbl_2.setText(_translate("MainWindow", "Music folder:"))
        self.rbBtn_2.setText(_translate("MainWindow", "Sync Rekordbox only"))
        self.audioBtn_2.setText(_translate("MainWindow", "Sync Audio Files only"))
        self.drivesLbl_2.setText(_translate("MainWindow", "Rekorbox Data Drive:"))
        self.allBtn_2.setText(_translate("MainWindow", "Sync All"))
        self.musicFolderBtn_2.setText(_translate("MainWindow", "..."))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
