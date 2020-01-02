#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

import pandas as pd
import pandas_datareader.data as web


# In[2]:


style.use('ggplot')


# In[3]:


#start = dt.datetime(2000,1,1)
#end = dt.datetime(2019,11,30)


# In[4]:


#df = web.DataReader('TSLA', 'yahoo', start, end)
#print(df.head())
#print(df.tail())


# In[5]:


#df.to_csv('tsla.csv')


# In[6]:


df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
print(df.head())


# In[7]:


df.plot()
plt.show()


# In[8]:


df['Adj Close'].plot()
plt.show()


# In[9]:


print(df[['Open', 'High']].head())


# In[10]:


df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()

#df.dropna(inplace=True) # Is used to remove nan

print(df.head())


# In[11]:


ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1, sharex=ax1)
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.plot(df.index, df['Volume'])
plt.show(plt.figure(figsize=(12,8)))


# In[12]:


# Resample

df_ohlc = df['Adj Close'].resample('10D').ohlc()
df_volume = df['Volume'].resample('10D').sum()

print(df_ohlc.head())
print(df_volume.head())


# In[13]:


from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
from matplotlib.dates import date2num


# In[15]:


df_ohlc.reset_index(inplace=True)
df_ohlc.head()


# In[16]:


df_ohlc['Date'] = df_ohlc['Date'].map(date2num) 
print(df_ohlc.head())


# In[18]:


ax1.xaxis.date() 


# In[ ]:


candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup'g')

