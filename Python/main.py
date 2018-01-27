#!/usr/bin/env python

import sys, os, logging
import numpy as np
import qdarkstyle

from PyQt5 import QtWidgets

from main_window import Ui_MainWindow

logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")

app = QtWidgets.QApplication(sys.argv)

app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

