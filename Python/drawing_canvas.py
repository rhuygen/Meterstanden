from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from PyQt5 import QtWidgets

DPI = 96
FIGSIZE_X = 1280
FIGSIZE_Y = 960

years = mdates.YearLocator()   # every year
months = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y')


class GraphicsView(QtWidgets.QGraphicsView):   
    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.NoButton:
            print("Simple mouse motion")
        elif event.buttons() == QtCore.Qt.LeftButton:
            print("Left click drag")
        elif event.buttons() == QtCore.Qt.RightButton:
            print("Right click drag")
        super(GraphicsView, self).mouseMoveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            print("Press!")
        super(GraphicsView, self).mousePressEvent(event)


class DrawingCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)

        import data
        self.data, self.dt = data.load_data()

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        self.draw_initial_figure()


        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


    def draw_initial_figure(self):

        self.drawWaterVerbruik()


    def drawWaterVerbruik(self):

        #fig = plt.figure(figsize=(FIGSIZE_X/DPI, FIGSIZE_Y/DPI), dpi=DPI)
        #fig.suptitle("Meterstanden")
        
        title = "Verbruik Water"
        
        self.axes.cla()

        self.axes.set_title(title)
        
        self.axes.plot(self.dt, self.data['water'], 'k-')
        self.axes.plot(self.dt, self.data['water'], 'b.')
        
        self.axes.set_xlabel("Datum")
        self.axes.set_ylabel("Verbruik Water [m$^3$]")
        
        # format the ticks
        self.axes.xaxis.set_major_locator(years)
        self.axes.xaxis.set_major_formatter(yearsFmt)
        self.axes.xaxis.set_minor_locator(months)
        
        #datemin = datetime.date(dt.min().year, 1, 1)
        #datemax = datetime.date(dt.max().year + 1, 1, 1)
        #self.axes.set_xlim(datemin, datemax)
        
        self.axes.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        self.axes.grid(True)
        
        # Tell matplotlib to interpret the x-axis values as dates
        
        #self.axes.xaxis_date()
        
        # Create a 5% (0.05) and 10% (0.1) padding in the
        # x and y directions respectively.
        #plt.margins(0.05, 0.1)
        
        # Make space for and rotate the x-axis tick labels
        
        #fig.autofmt_xdate()
        
        #plt.show()
        #plt.close()
        
        self.draw()

        pass


    def drawGasVerbruik(self):
        
        # Tell matplotlib to interpret the x-axis values as dates
        
        #self.axes.xaxis_date()
        
        title = "Verbruik Gas"
        
        self.axes.cla()

        self.axes.set_title(title)

        self.axes.plot(self.dt, self.data['gas'], 'k-')
        self.axes.plot(self.dt, self.data['gas'], 'b.')
        
        self.axes.set_xlabel("Datum")
        self.axes.set_ylabel("Verbruik Gas [m$^3$]")
        
        self.axes.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        self.axes.grid(True)
        
        plt.setp(self.axes.xaxis.get_majorticklabels(), rotation=30)
        #self.axes.get_xmajorticklabels().set_rotation(30)
        # Create a 5% (0.05) and 10% (0.1) padding in the
        # x and y directions respectively.
        #plt.margins(0.05, 0.1)
        
        # Make space for and rotate the x-axis tick labels
        
        #fig.autofmt_xdate()

        self.draw()


    def drawElektriciteitsVerbruik(self):

        e_total = self.data['edag'] + self.data['enacht']

        self.axes.cla()

        self.axes.xaxis_date()
        self.axes.set_xlabel("Datum")
        self.axes.set_ylabel("Verbruik (kWh)")
        self.axes.plot(self.dt, e_total)
        self.axes.plot(self.dt, e_total, 'r.')
        
        plt.margins(0.05, 0.1)

        self.draw()


    def drawZonnepanelen(self):

        sma_ratio = self.data['sma_7000'] / self.data['sma_3000']

        self.axes.cla()
        
        self.axes.xaxis_date()        
        self.axes.set_xlabel("Datum")
        self.axes.set_ylabel("SMA 7000 / SMA 3000")
        self.axes.plot(self.dt, sma_ratio, "b.")
        
        plt.margins(0.05, 0.1)

        self.draw()

        pass

