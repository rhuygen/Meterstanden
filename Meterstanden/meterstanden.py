import numpy as np
import matplotlib.pyplot as plt
import requests
import urllib.request, urllib.parse, urllib.error
import os
from datetime import datetime


# This is the location of the file in dropbox. 
dropbox_location = "Documents/Meterstanden/Meterstanden.csv"

# This is where the file should be copied to on my local iPad/Laptop.
input_filename = 'from Working Copy/Pythonista/Meterstanden/Meterstanden.csv'

def copy_file_from_dropbox(source, destination):
    TOKEN='TDmFIIPHxcwAAAAAAAAJsP2t869VCS1HFZMuqoeE3Mh2J3MM2KvBQydibirg6RxZ'
    headers = {'Authorization': 'Bearer %s' % (TOKEN,)}
    url_path = urllib.parse.quote(source.encode('utf-8'))
    url = 'https://api-content.dropbox.com/1/files/dropbox/%s' % (url_path,)
    r = requests.get(url, stream=True, headers=headers)
    dest_path = os.path.join(os.path.expanduser('~/Documents/'), destination)
    size = r.headers.get('Content-Length', 0)
    bytes_written = 0
    with open(dest_path, 'wb') as f:
        for chunk in r.iter_content(1024*10):
            f.write(chunk)
            bytes_written += len(chunk)
    return bytes_written

#n = copy_file_from_dropbox(dropbox_location, input_filename)

#print("{} copied from dropbox, {} bytes copied, destination is {}"\
#    .format(dropbox_location, n, input_filename))

data = np.recfromcsv(os.path.join(os.path.expanduser('~/Documents/'), input_filename))

#print (data)
#print (data[0])
#print (data['date_time'])


### Convert the byte string b'' into a 'normal' string

dt = [datetime.strptime(x.decode('UTF-8'), '%Y-%m-%d %H:%M') for x in data['date_time']]

# Maak een plot voor het gasverbruik
fig, ax = plt.subplots()

# Make space for and rotate the x-axis tick labels
fig.autofmt_xdate()

# Tell matplotlib to interpret the x-axis values as dates
ax.xaxis_date()

ax.plot(dt, data['gas'], 'k-')
ax.plot(dt, data['gas'], 'bo')

ax.set_xlabel("Datum")
ax.set_ylabel("Verbruik Gas [m$^3$]")

# Create a 5% (0.05) and 10% (0.1) padding in the
# x and y directions respectively.
plt.margins(0.05, 0.1)

plt.show()
plt.close()

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

fig, ax = plt.subplots()

fig.autofmt_xdate()
ax.xaxis_date()

ax.set_xlabel("Datum")
ax.set_ylabel("Verbruik Gas [m$^3$/dag]")

ax.plot(dt[1:], gpd, 'k-', linewidth=2.0, color='blue')
ax.plot(dt[1:], gpd, 'wo')

plt.margins(0.05, 0.1)
plt.show()
plt.close()

#p.extra_y_ranges = {"temp": Range1d(start=-10, end=60)}
#p.add_layout(LinearAxis(y_range_name="temp"), 'right')

#p.line(dt, data['temperatuur'], color='green', y_range_name='temp')
#p.circle(dt, data['temperatuur'], color='green', fill_color='white', size=4, y_range_name='temp')


# Verbruik elektriciteit

e_total = data['edag'] + data['enacht']

fig,ax = plt.subplots()
fig.autofmt_xdate()
ax.xaxis_date()
ax.set_xlabel("Datum")
ax.set_ylabel("Verbruik (kWh)")
ax.plot(dt, e_total)
ax.plot(dt, e_total, 'r.')

plt.margins(0.05, 0.1)
plt.show()
plt.close()


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


fig,ax = plt.subplots()
fig.autofmt_xdate()
ax.xaxis_date()
ax.plot(dt[1:], epd, linewidth=1)
ax.plot(dt[1:], epd, 'wo')

plt.margins(0.05, 0.1)
plt.show()
plt.close()


# Verschil tussen het berekende z_totaal en data['sma']

data_sma = data['sma']
where_isnan = np.isnan(data_sma)
data_sma[where_isnan] = 0.0

sma_diff = z_total - data_sma

small_values = sma_diff < 0.0001
sma_diff[small_values] = 0.0

fig,ax = plt.subplots()
fig.autofmt_xdate()
ax.xaxis_date()
ax.set_xlabel("Datum")
ax.set_ylabel("Controle SMA berekening")
ax.plot(dt[-10:], sma_diff[-10:], linewidth=1)
ax.plot(dt[-10:], sma_diff[-10:], 'b.')
plt.text(dt[-2], sma_diff[-2], sma_diff[-2])

plt.margins(0.05, 0.1)
plt.show()
plt.close()


# Verhouding opbrengst zonnepanelen

sma_ratio = data['sma_7000'] / data['sma_3000']

fig,ax = plt.subplots()

fig.autofmt_xdate()
ax.xaxis_date()

ax.set_xlabel("Datum")
ax.set_ylabel("SMA 7000 / SMA 3000")
ax.plot(dt, sma_ratio, "b.")

plt.margins(0.05, 0.1)
plt.show()
plt.close()


