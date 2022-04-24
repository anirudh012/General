import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dd_window = 1000
Slow_MA = 100
Fast_MA = 20

df = pd.read_table('NIFTY_DATA2.txt', delimiter=',')

df.drop(labels=['Symbol','Open', 'High', 'Low'], axis=1, inplace=True)

df['Return'] = (df.Close / df.Close.shift(1)) - 1
df['Ending'] = (df.Return + 1).cumprod()
df['Peak'] = df.Ending.rolling(window = dd_window, min_periods=dd_window).max()
df['Drawdown'] = df.Ending - df.Peak
df['Slow_MA'] = df.Close.rolling(window = Slow_MA, min_periods=Slow_MA).mean()
df['Fast_MA'] = df.Close.rolling(window = Fast_MA, min_periods=Fast_MA).mean()
df['MA_cross'] = np.where(df.Fast_MA > df.Slow_MA,1,0)
df['Comm'] = np.where(df.MA_cross != df.MA_cross.shift(1),1,0)
df['Final'] = np.where(df.MA_cross.shift(1) == 1, df.Return , df.Return * -1)
df['Final2'] = np.where(df.Comm.shift(-1) == 1, df.Final - 0.0002, df.Final)
df['Final3'] = (df.Final2 + 1).cumprod()
df['Over'] = (df.Final3 / df.Ending)

print(df.tail(10))
plt.plot(df.Ending)
plt.plot(df.Final3)
plt.show()