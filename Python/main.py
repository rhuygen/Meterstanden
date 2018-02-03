#!/usr/bin/env python

import sys, os, logging
import numpy as np
import pandas as pd

import qdarkstyle

from PyQt5 import QtCore, QtWidgets

from main_window import Ui_MainWindow

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

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
        self.data, self.df, self.dt = data.load_data()

        self.ui.tabWidget.currentChanged['int'].connect(self.tabSelected)

        self.tabSelected(self.ui.tabWidget.currentIndex())

    def tabSelected(self, arg=None):

        drawMethod = {
            0 : self.drawWaterVerbruik,
            1 : self.drawGasVerbruik,
            2 : self.drawGasVerbruikPerDag,
            3 : self.drawElektriciteitsVerbruik,
            4 : self.drawElektriciteitsVerbruikPerDag,
            5 : self.drawZonnepanelen
        }

        drawCanvas = {
            0 : self.ui.water,
            1 : self.ui.gas,
            2 : self.ui.gas_per_dag,
            3 : self.ui.elektriciteit,
            4 : self.ui.elektriciteit_per_dag,
            5 : self.ui.zonnepanelen
        }

        # Replace QWidget toolBar with what we really want
        
        self.ui.toolBar.hide()
        self.toolBar = NavigationToolbar(drawCanvas[arg], self.MainWindow, coordinates=False) 
        self.ui.gridLayout.addWidget(self.toolBar, 1, 1, 1, 1)

        drawMethod[arg](drawCanvas[arg])



    def drawWaterVerbruik(self, canvas):

        #fig = plt.figure(figsize=(FIGSIZE_X/DPI, FIGSIZE_Y/DPI), dpi=DPI)
        #fig.suptitle("Meterstanden")
        
        title = "Verbruik Water"
        
        canvas.axes.cla()
        canvas.setColorScheme("default")

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
        
        #plt.setp(canvas.axes.xaxis.get_majorticklabels(), rotation=30)

        #canvas.axes.get_xmajorticklabels().set_rotation(30)
        
        # Create a 5% (0.05) and 10% (0.1) padding in the
        # x and y directions respectively.
        #plt.margins(0.05, 0.1)
        
        # Make space for and rotate the x-axis tick labels
        
        #fig.autofmt_xdate()

        canvas.draw()


    def drawGasVerbruikPerDag(self, canvas):

        title = "Gas verbruik per dag"

        # Bereken het verbruik in gas tussen twee opeenvolgende metingen
        
        g_diff = self.df['Gas'].diff().dropna()
        
        # Bereken de tijd tussen twee opeenvolgende metingen in dagen (both options are the same)
        
        time_diff_days = g_diff.index.to_series().diff().astype('timedelta64[s]') / 60. / 60. / 24.
        time_diff_days = g_diff.index.to_series().diff().dt.total_seconds().fillna(0) / 60. / 60. / 24.
        
        # Bereken het verbruik van gas per dag
        
        g_per_dag = g_diff / time_diff_days

        canvas.axes.cla()
        canvas.setColorScheme("default")

        canvas.axes.set_title(title)

        canvas.axes.plot(g_per_dag, '-')
        canvas.axes.plot(g_per_dag, '.')

        canvas.axes.set_xlabel("Datum")
        canvas.axes.set_ylabel("Verbruik Gas per Dag [m$^3$/dag]")

        canvas.axes.grid(True)

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


    def drawElektriciteitsVerbruikPerDag(self, canvas):

        title = "Elektriciteitsverbruik per dag"

        # Bereken het verbruik in elektriciteit tussen twee opeenvolgende metingen
        # Elektriciteit voor de dag en nacht teller eerst bijeen tellen
        
        e_total = self.df.eDag + self.df.eNacht
        e_diff = e_total.diff().dropna()
        
        # Bereken de tijd tussen twee opeenvolgende metingen in dagen
        
        time_diff_days = e_diff.index.to_series().diff().dt.total_seconds().fillna(0) / 60. / 60. / 24.
        
        # Bereken het elektriciteitsverbruik per dag
        
        e_per_dag = e_diff / time_diff_days
        
        # Bereken de totale opbrengst per dag van de zonnepanelen
        
        z_total = self.df.SMA_3000.shift(1) + self.df.SMA_7000.shift(1)
        z_total = z_total.dropna()
        
        print ("Totale opbrengst zonnepanelen op {}: {} [kWh]".format(z_total.index[-1], z_total[-1]))
        
        # Het totaal verbruik per dag is de sum van het elektriciteitsverbruik en de opbrengst van de zonnepanelen
        
        ez_per_dag = e_per_dag + z_total


        canvas.axes.cla()
        canvas.setColorScheme("default")

        canvas.axes.set_title(title)

        canvas.axes.plot(ez_per_dag, '-')
        canvas.axes.plot(ez_per_dag, '.')

        canvas.axes.set_xlabel("Datum")
        canvas.axes.set_ylabel("Verbruik Elektriciteit per Dag [kWh/dag]")

        canvas.axes.grid(True)

        canvas.draw()


    def drawZonnepanelen(self, canvas):

        # De SMA 7000 bevat 32 zonnepanelen, de SMA 3000 bevat er 14. 
        # De verhouding zou dus ± 2.28 moeten zijn
        
        sma_ratio = self.df.SMA_7000 / self.df.SMA_3000

        title = "Zonnepanelen"

        canvas.axes.cla()

        canvas.setColorScheme("default")

        canvas.axes.set_title(title)
        
        canvas.axes.xaxis_date()        
        canvas.axes.set_xlabel("Datum")
        canvas.axes.set_ylabel("SMA 7000 / SMA 3000")
        canvas.axes.plot(sma_ratio, ".")
        canvas.axes.grid(True)
        
        plt.margins(0.05, 0.1)

        canvas.draw()



#-------------------------------------------------------------------------------
if __name__ == "__main__":
    MainWindow_EXEC()
