# -*- coding: utf-8 -*-
"""
Data Incubator milestone project: stock chart
"""

from datetime import datetime, timedelta
#from pandas import DataFrame
import yfinance as yf
from math import pi
from calendar import monthrange
import streamlit as st
from pandas_datareader import data as pdr
import plotly.graph_objects as go

yf.pdr_override()

st.title("Shahar's milestone project")

with st.form("form"):
    symbol = st.text_input("Ticker?")
    date = st.date_input('Click month/year to scroll; select any day on require month')
    adjusted = st.checkbox("Display adjusted prices")
    month = date.month
    year = date.year
    submitted = st.form_submit_button("Submit")
    if submitted:
        start = datetime(year, month, 1)
        end = datetime(year, month, monthrange(year, month)[1])
        data = pdr.get_data_yahoo(symbol, start=start, end=end)
        if adjusted:
            close = data['Adj Close']
        else:
            close = data['Close']
        title = symbol.upper() + " share prices " + str(month)+"/"+str(year)
        candlestick = go.Candlestick(x=data.index,
                    open=data.Open, high=data.High,
                    low=data.Low, close=close)
        fig = go.Figure(data=[candlestick])
        fig.update_layout(title=title,
                          yaxis_title='Price [US$]',
                          xaxis_rangeslider_visible=False)
        st.plotly_chart(fig)