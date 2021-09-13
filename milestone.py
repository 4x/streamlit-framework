# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import datetime
import pandas_datareader.data as web
from pandas import Series, DataFrame
from pandas_datareader import data as pdr
import yfinance as yf

import streamlit as st
import fix_yahoo_finance
from math import pi
from bokeh.plotting import figure, show, output_file

yf.pdr_override()
data = pdr.get_data_yahoo(symbol, start="2017-01-01", end="2017-04-30")







# Does NOT work
data = pdr.get_data_yahoo('NVDA')
# Display Info
print(data.info())

# Request historical data for past 5 years
symbol = "TSLA"
data = yf.Ticker("NVDA").history(period='5y')
data = yf.download(symbol, start="2017-01-01", end="2017-04-30")

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
w = 12*60*60*1000/2000

p = figure(x_axis_type="datetime", tools=TOOLS, plot_width=1000, title = "Candlestick")
p.xaxis.major_label_orientation = pi/4

p.segment(data.index, data.High, data.index, data.Low, color="black")
p.vbar(data.index, w, data.Open, data.Close, fill_color="#D5E1DD", line_color="black")
p.vbar(data.datetime[dec], w, data.open[dec], data.close, fill_color="#F2583E", line_color="black")
p.vbar(data.datetime[inc], w, data.open[inc], data.close[inc], fill_color="#D5E1DD", line_color="black")
p.vbar(data.datetime[dec], w, data.open[dec], data.close[dec], fill_color="#F2583E", line_color="black")

show(p)



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

