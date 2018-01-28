# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(974, 604)
        MainWindow.setMinimumSize(QtCore.QSize(637, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.Water = QtWidgets.QWidget()
        self.Water.setObjectName("Water")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.Water)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.water = DrawingCanvas(self.Water)
        self.water.setObjectName("water")
        self.horizontalLayout.addWidget(self.water)
        self.tabWidget.addTab(self.Water, "")
        self.Gas = QtWidgets.QWidget()
        self.Gas.setObjectName("Gas")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Gas)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gas = DrawingCanvas(self.Gas)
        self.gas.setObjectName("gas")
        self.horizontalLayout_2.addWidget(self.gas)
        self.tabWidget.addTab(self.Gas, "")
        self.Elektriciteit = QtWidgets.QWidget()
        self.Elektriciteit.setObjectName("Elektriciteit")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Elektriciteit)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.elektriciteit = DrawingCanvas(self.Elektriciteit)
        self.elektriciteit.setObjectName("elektriciteit")
        self.horizontalLayout_3.addWidget(self.elektriciteit)
        self.tabWidget.addTab(self.Elektriciteit, "")
        self.Zonnepanelen = QtWidgets.QWidget()
        self.Zonnepanelen.setObjectName("Zonnepanelen")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Zonnepanelen)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.zonnepanelen = DrawingCanvas(self.Zonnepanelen)
        self.zonnepanelen.setObjectName("zonnepanelen")
        self.horizontalLayout_4.addWidget(self.zonnepanelen)
        self.tabWidget.addTab(self.Zonnepanelen, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 974, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Water), _translate("MainWindow", "Water"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Gas), _translate("MainWindow", "Gas"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Elektriciteit), _translate("MainWindow", "Elektriciteit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Zonnepanelen), _translate("MainWindow", "Zonnepanelen"))

from drawing_canvas import DrawingCanvas
