# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'teams.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(10, 10, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 10, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
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
        self.comboBox.setItemText(0, _translate("MainWindow", "选择联赛"))
        self.comboBox.setItemText(1, _translate("MainWindow", "英超"))
        self.comboBox.setItemText(2, _translate("MainWindow", "西甲"))
        self.comboBox.setItemText(3, _translate("MainWindow", "意甲"))
        self.comboBox.setItemText(4, _translate("MainWindow", "德甲"))
        self.comboBox.setItemText(5, _translate("MainWindow", "法甲"))
        self.comboBox.setItemText(6, _translate("MainWindow", "巴甲"))
        self.comboBox.setItemText(7, _translate("MainWindow", "荷甲"))
        self.comboBox.setItemText(8, _translate("MainWindow", "葡超"))
        self.comboBox.setItemText(9, _translate("MainWindow", "英冠"))
        self.comboBox.setItemText(10, _translate("MainWindow", "俄超"))
        self.comboBox.setItemText(11, _translate("MainWindow", "土超"))
        self.comboBox.setItemText(12, _translate("MainWindow", "阿甲"))
        self.comboBox.setItemText(13, _translate("MainWindow", "中超"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "选择球队"))

