import numpy as np
import pandas as pd
import matplotlib as plt
#import seaborn as sns
import matplotlib.dates as date
import datetime
%matplotlib inline
from numpy.random import randn
df = pd.read_csv('SQQQ.csv', parse_dates=['Date'], dayfirst =True)
df=df.sort_values(by=['Date'])
df = df.drop(df.columns[[2,3]], axis=1)
df.set_index('Date', inplace=True)
df.index = pd.to_datetime(df.index)
df.resample('1M').mean()        
daily_returns = df['Adj Close'].pct_change()
monthly_returns = df['Adj Close'].resample('M').ffill().pct_change()
pd.options.display.float_format = '{:.2%}'.format
pd.set_option('display.max_rows', df.shape[0]+1)
print(monthly_returns)


