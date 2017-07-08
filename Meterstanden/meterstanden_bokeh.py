import numpy as np

from bokeh.plotting import figure, show
from bokeh.io import output_notebook, output_file, save
from datetime import datetime

output_notebook()

datadir = '/Users/rik/Dropbox/Documents/Meterstanden/'
filename = datadir + 'Meterstanden.csv'

data = np.recfromcsv(filename)

#print (data)
#print (data[0])
#print (data['date_time'])


### Convert the byte string b'' into a 'normal' string

dt = [datetime.strptime(x.decode('UTF-8'), '%Y-%m-%d %H:%M') for x in data['date_time']]

dt[0]

# Maak een plot voor het gasverbruik

p = figure(x_axis_label='Datum', x_axis_type='datetime', y_axis_label='Volume (m^3)', \
           plot_height=500, plot_width=900, title='Verbruik Gas')

p.circle(dt, data['gas'])

#show(p)
output_file(datadir + "Verbruik_Gas.html")
save(p)

# Maak een plot voor het gasverbruik per dag

# Bereken het verbruik in gas tussen twee opeenvolgende metingen

g1 = data['gas'][0:-1]
g2 = data['gas'][1:]
g_diff = np.array(g2-g1)

# Bereken de tijd tussen twee opeenvolgende metingen in dagen

d1 = dt[0:-1]
d2 = dt[1:]

helper = np.vectorize(lambda x: x.total_seconds())
dt_sec = helper(np.array(d2)-np.array(d1))
dt_days = dt_sec / 60. / 60. / 24.

# Bereken het verbruik van gas per dag

gpd = g_diff / dt_days


from bokeh.models import LinearAxis, Range1d

p = figure(x_axis_label='Datum', x_axis_type='datetime', y_axis_label='Verbruik (m^3/dag)', \
           plot_height=500, plot_width=900, title='Verbruik Gas per dag')

p.y_range = Range1d(-20,20)
p.line(dt[1:], gpd, line_width=1)
p.circle(dt[1:], gpd, fill_color='white', size=4)

p.extra_y_ranges = {"temp": Range1d(start=-10, end=60)}
p.add_layout(LinearAxis(y_range_name="temp"), 'right')

p.line(dt, data['temperatuur'], color='green', y_range_name='temp')
p.circle(dt, data['temperatuur'], color='green', fill_color='white', size=4, y_range_name='temp')

#show(p)
output_file(datadir + "Verbruik_Gas_per_dag.html")
save(p)

# Verbruik elektriciteit

e_total = data['edag'] + data['enacht']

p = figure(x_axis_label='Datum', x_axis_type='datetime', y_axis_label='Verbruik (kWh)', \
           plot_height=500, plot_width=900, title='Verbruik Elektriciteit')
p.line(dt, e_total)
p.circle(dt, e_total, size=3)

#show(p)
output_file(datadir + "Verbruik_Elektriciteit.html")
save(p)

# Verbruik elektriciteit per dag

# Bereken het verbruik in elektriciteit tussen twee opeenvolgende metingen
# Elektriciteit voor de dag en nacht teller eerst bijeen tellen

e_total = data['edag'] + data['enacht']
e1 = e_total[0:-1]
e2 = e_total[1:]
e_diff = np.array(e2-e1)

# Bereken de totale opbrengst per dag van de zonnepanelen

z_total = data['sma_3000'] + data['sma_7000']

epd = e_diff + z_total[:-1] / dt_days



p = figure(x_axis_label='Datum', x_axis_type='datetime', y_axis_label='Verbruik (kWh/dag)', plot_height=500, plot_width=900, title='Verbruik Elektriciteit per dag')

p.line(dt[1:], epd, line_width=1)
p.circle(dt[1:], epd, fill_color='white', size=4)

#show(p)
output_file(datadir + "Verbruik_Elektriciteit_per_dag.html")
save(p)

# Verhouding opbrengst zonnepanelen

sma_ratio = data['sma_7000'] / data['sma_3000']

p = figure(x_axis_label='Datum', x_axis_type='datetime', y_axis_label='SMA 7000 / SMA 3000', \
           plot_height=500, plot_width=900, title='Verhouding SMA 7000 vs SMA 3000')

p.circle(dt, sma_ratio)

output_file(datadir + "Ratio_Zonnepanelen.html")
save(p)


