import datetime

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as md
import seaborn as sns

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

fn = "/Users/rik/Private/Git/Meterstanden/Data/Meterstanden.csv"
df = pd.read_csv(fn)

df['time'] = pd.to_datetime(df['Date_Time'], format='%Y-%m-%d %H:%M')
df['month'] = pd.to_datetime(df['time'].dt.month, format='%m')
df['year'] = df['time'].dt.year
df['doy'] = df['time'].dt.dayofyear

df = df[['year', 'doy', 'Gas', 'eDag']]
df = df.dropna()

piv = pd.pivot_table(df, index=['doy'], columns=['year'], values=['Gas'], aggfunc='mean')

# Find out what the offset could be e.g. for 27th January

piv.iloc[26]


piv[("Gas", 2016)] -= 688.233
piv[("Gas", 2017)] -= 2780.371
piv[("Gas", 2018)] -= 4699.153
piv[("Gas", 2019)] -= 7220.
piv[("Gas", 2020)] -= 10500.
piv[("Gas", 2021)] -= 14032.494
piv[("Gas", 2022)] -= 17744.537

# piv[[("Gas", 2016), ("Gas", 2017), ("Gas", 2018), ("Gas", 2019), ("Gas", 2020), ("Gas", 2021), ("Gas", 2022)]].plot()


# piv.plot()


# offset for day of year

doy_280 = datetime.datetime(2022, 10, 7, 0, 0, 0, 0).strftime("%j")
doy_226 = datetime.datetime(2022, 8, 14, 0, 0, 0, 0).strftime("%j")
doy_027 = datetime.datetime(2022, 1, 27, 0, 0, 0, 0).strftime("%j")

# -------------------- Make the plot for Gas ---------------------------------------------------------------------------

offset_gas_280 = {2015: 0.288, 2016: 1664.936, 2017: 3936.008, 2019: 8700.027, 2022: 19096.456}
offset_gas_226 = {2016: 1587.984, 2017: 3846.380, 2018: 5533.090, 2019: 8453.316, 2022: 19032.746}
offset_gas_027 = {2016: 688, 2017: 2780, 2018: 4700, 2019: 7220, 2020: 10500, 2021: 14032, 2022: 17745}
offsets = offset_gas_027

# 110.x DPI -> 1440 Pixels = 13"
# 130.x DPI -> 1680 Pixels = 13"
# 147.x DPI -> 1920 Pixels = 13"

fig, (ax_gas, ax_edag) = plt.subplots(2, 1, sharex=True, figsize=(7, 7), dpi=130, layout='tight')

for year in offsets:
    x = df[df['year'] == year]['doy']
    y = df[df['year'] == year]['Gas']
    ax_gas.scatter(x, y-offsets[year], label=year)

ax_gas.set_ylabel("m$^3$")
ax_gas.set_title("Jaarlijks Gasverbruik")
ax_gas.legend()

# -------------------- Make the plot for electricity -------------------------------------------------------------------

offset_edag_027 = {2016: 164082, 2017: 167001, 2018: 169195, 2019: 168437, 2020: 168600, 2021: 168812, 2022: 170393}
offsets = offset_edag_027

for year in offsets:
    x = df[df['year'] == year]['doy']
    y = df[df['year'] == year]['eDag']
    ax_edag.scatter(x, y-offsets[year], label=year)

ax_edag.set_ylabel("kWh")
ax_edag.set_title("Jaarlijks Elektriciteitsverbruik")
ax_edag.legend()

plt.show()

# palette = sns.color_palette('Set1', n_colors = len(df['year'].unique()))
# sns.lineplot(
#     ax=ax,
#     data=df,
#     x='month',
#     y='Gas',
#     hue='year',
#     palette=palette,
#     ci=None)

# ax.xaxis.set_major_locator(md.DMonthLocator())
# ax.xaxis.set_major_formatter(md.DateFormatter('%b'))
# ax.set_xlim([df['month'].iloc[0], df['month'].iloc[-1]])
