# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
import pandas_datareader as pdr

import streamlit as st
import fix_yahoo_finance


# Does NOT work
data = pdr.get_data_yahoo('NVDA')
# Display Info
print(data.info())

import yfinance as yf
# Request historical data for past 5 years
symbol = "TSLA"
data = yf.Ticker("NVDA").history(period='5y')
data = yf.download(symbol, start="2017-01-01", end="2017-04-30")





st.title("Streamlit 101: An in-depth introduction")
adjusted = st.checkbox("Display adjusted prices")

month = st.sidebar.number_input("Month", min_value=1)
year = st.sidebar.number_input("Year", min_value=1990, value=2020)
start = datetime.datetime(2017, 1, 1)
end = datetime.datetime(2019, 1, 11)
df = pdr.get_data_yahoo(symbol, start=start, end='2017-05-24')

#df = web.DataReader(symbol, 'yahoo', start, end)
#df.tail()

df

close_px = df['Adj Close']
mavg = close_px.rolling(window=100).mean()

# matplotlib inline
import matplotlib.pyplot as plt
from matplotlib import style

# Adjusting the size of matplotlib
import matplotlib as mpl
mpl.rc('figure', figsize=(8, 7))
mpl.__version__

# Adjusting the style of matplotlib
style.use('ggplot')

close_px.plot(label='AAPL')
mavg.plot(label='mavg')
plt.legend()

