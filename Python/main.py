#!/usr/bin/env python

import sys, os, logging
import numpy as np
import qdarkstyle

from PyQt5 import QtCore, QtWidgets

from main_window import Ui_MainWindow

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')


logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")


class MainWindow_EXEC():
            
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        
        # set dark style sheet
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        app.setApplicationDisplayName('Meterstanden')
        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self.MainWindow)   
        
        self.MainWindow.show()

        self.init_tabs()

        sys.exit(app.exec_()) 
        
    #---------------------------------------------------------------------------
    def init_tabs(self):
        import data
        self.data, self.dt = data.load_data()

        self.ui.tabWidget.currentChanged['int'].connect(self.tabSelected)

        self.tabSelected(self.ui.tabWidget.currentIndex())

    def tabSelected(self, arg=None):

        print ("tabSelected: {}". format(arg))

        drawMethod = {
            0 : self.drawWaterVerbruik,
            1 : self.drawGasVerbruik,
            2 : self.drawElektriciteitsVerbruik,
            3 : self.drawZonnepanelen
        }

        drawCanvas = {
            0 : self.ui.water,
            1 : self.ui.gas,
            2 : self.ui.elektriciteit,
            3 : self.ui.zonnepanelen
        }

        drawMethod[arg](drawCanvas[arg])


    def drawWaterVerbruik(self, canvas):

        #fig = plt.figure(figsize=(FIGSIZE_X/DPI, FIGSIZE_Y/DPI), dpi=DPI)
        #fig.suptitle("Meterstanden")
        
        title = "Verbruik Water"
        
        canvas.axes.cla()
        canvas.setColorScheme("dark")

        canvas.axes.set_title(title)
        
        canvas.axes.plot(self.dt, self.data['water'], '-')
        canvas.axes.plot(self.dt, self.data['water'], '.')
        
        canvas.axes.set_xlabel("Datum")
        canvas.axes.set_ylabel("Volume [m$^3$]")
        
        # format the ticks
        canvas.axes.xaxis.set_major_locator(years)
        canvas.axes.xaxis.set_major_formatter(yearsFmt)
        canvas.axes.xaxis.set_minor_locator(months)
        
        #datemin = datetime.date(dt.min().year, 1, 1)
        #datemax = datetime.date(dt.max().year + 1, 1, 1)
        #self.axes.set_xlim(datemin, datemax)
        
        canvas.axes.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        canvas.axes.grid(True)
        
        # Tell matplotlib to interpret the x-axis values as dates
        
        #self.axes.xaxis_date()
        
        # Create a 5% (0.05) and 10% (0.1) padding in the
        # x and y directions respectively.
        #plt.margins(0.05, 0.1)
        
        # Make space for and rotate the x-axis tick labels
        
        #fig.autofmt_xdate()
        
        #plt.show()
        #plt.close()
        
        canvas.draw()

        pass


    def drawGasVerbruik(self, canvas):
        
        # Tell matplotlib to interpret the x-axis values as dates
        
        title = "Verbruik Gas"
        
        canvas.axes.cla()

        canvas.setColorScheme("default")

        canvas.axes.set_title(title)

        canvas.axes.plot(self.dt, self.data['gas'], '-')
        canvas.axes.plot(self.dt, self.data['gas'], '.')
        
        canvas.axes.set_xlabel("Datum")
        canvas.axes.set_ylabel("Verbruik Gas [m$^3$]")
        
        canvas.axes.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        canvas.axes.grid(True)
        
        plt.setp(canvas.axes.xaxis.get_majorticklabels(), rotation=30)
        #canvas.axes.get_xmajorticklabels().set_rotation(30)
        # Create a 5% (0.05) and 10% (0.1) padding in the
        # x and y directions respectively.
        #plt.margins(0.05, 0.1)
        
        # Make space for and rotate the x-axis tick labels
        
        #fig.autofmt_xdate()

        canvas.draw()


    def drawElektriciteitsVerbruik(self, canvas):

        e_total = self.data['edag'] + self.data['enacht']

        title = "Verbruik Elektriciteit"

        canvas.axes.cla()

        canvas.setColorScheme("default")

        canvas.axes.set_title(title)

        canvas.axes.xaxis_date()
        canvas.axes.set_xlabel("Datum")
        canvas.axes.set_ylabel("Verbruik (kWh)")
        canvas.axes.plot(self.dt, e_total)
        canvas.axes.plot(self.dt, e_total, '.')
        canvas.axes.grid(True)
        
        plt.margins(0.05, 0.1)

        canvas.draw()


    def drawZonnepanelen(self, canvas):

        sma_ratio = self.data['sma_7000'] / self.data['sma_3000']

        title = "Zonnepanelen"

        canvas.axes.cla()

        canvas.setColorScheme("default")

        canvas.axes.set_title(title)
        
        canvas.axes.xaxis_date()        
        canvas.axes.set_xlabel("Datum")
        canvas.axes.set_ylabel("SMA 7000 / SMA 3000")
        canvas.axes.plot(self.dt, sma_ratio, ".")
        canvas.axes.grid(True)
        
        plt.margins(0.05, 0.1)

        canvas.draw()



#-------------------------------------------------------------------------------
if __name__ == "__main__":
    MainWindow_EXEC()
