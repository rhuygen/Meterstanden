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
        MainWindow.resize(1013, 519)
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
        self.Gas_per_Dag = QtWidgets.QWidget()
        self.Gas_per_Dag.setObjectName("Gas_per_Dag")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.Gas_per_Dag)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gas_per_dag = DrawingCanvas(self.Gas_per_Dag)
        self.gas_per_dag.setObjectName("gas_per_dag")
        self.horizontalLayout_5.addWidget(self.gas_per_dag)
        self.tabWidget.addTab(self.Gas_per_Dag, "")
        self.Elektriciteit = QtWidgets.QWidget()
        self.Elektriciteit.setObjectName("Elektriciteit")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.Elektriciteit)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.elektriciteit = DrawingCanvas(self.Elektriciteit)
        self.elektriciteit.setObjectName("elektriciteit")
        self.horizontalLayout_3.addWidget(self.elektriciteit)
        self.tabWidget.addTab(self.Elektriciteit, "")
        self.Elektriciteit_per_Dag = QtWidgets.QWidget()
        self.Elektriciteit_per_Dag.setObjectName("Elektriciteit_per_Dag")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.Elektriciteit_per_Dag)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.elektriciteit_per_dag = DrawingCanvas(self.Elektriciteit_per_Dag)
        self.elektriciteit_per_dag.setObjectName("elektriciteit_per_dag")
        self.horizontalLayout_6.addWidget(self.elektriciteit_per_dag)
        self.tabWidget.addTab(self.Elektriciteit_per_Dag, "")
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
        self.toolBar = QtWidgets.QWidget(self.centralwidget)
        self.toolBar.setMinimumSize(QtCore.QSize(0, 30))
        self.toolBar.setObjectName("toolBar")
        self.gridLayout.addWidget(self.toolBar, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1013, 22))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Gas_per_Dag), _translate("MainWindow", "Gas per Dag"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Elektriciteit), _translate("MainWindow", "Elektriciteit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Elektriciteit_per_Dag), _translate("MainWindow", "Elektriciteit per Dag"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Zonnepanelen), _translate("MainWindow", "Zonnepanelen"))

from drawing_canvas import DrawingCanvas
