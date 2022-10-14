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

piv[[("Gas", 2016), ("Gas", 2017), ("Gas", 2018), ("Gas", 2019), ("Gas", 2020), ("Gas", 2021), ("Gas", 2022)]].plot()


# piv.plot()


# offset for day of year

offset_280 = {2015: 0.288, 2016: 1664.936, 2017: 3936.008, 2019: 8700.027, 2022: 19096.456}  # 7 oct
offset_226 = {2016: 1587.984, 2017: 3846.380, 2018: 5533.090, 2019: 8453.316, 2022: 19032.746}  # 14 aug

offsets = offset_226


# fig, ax = plt.subplots(figsize=(16, 8))
#
# for year in offsets:  #2015, 2016, 2017, 2019, 2022:  # df['year'].unique():
#     x = df[df['year'] == year]['doy']
#     y = df[df['year'] == year]['Gas']
#     y = df[df['year'] == year]['eDag']
    # ax.plot(x, y-offsets[year], label=year)
    # ax.plot(x, y, label=year)

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
# plt.legend()
# plt.show()
