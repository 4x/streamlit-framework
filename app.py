# -*- coding: utf-8 -*-
"""
Data Incubator milestone project: stock chart
"""

from datetime import datetime, timedelta
from pandas import DataFrame
import yfinance as yf
from math import pi
from calendar import monthrange
import streamlit as st
from pandas_datareader import data as pdr
import plotly.graph_objects as go

yf.pdr_override()

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
w = 12*60*60*1000/2000

st.title("Shahar's milestone project")

with st.form("my_form"):
    symbol = st.text_input("Ticker?")
    date = st.date_input('Click month/year to scroll')
    adjusted = st.checkbox("Display adjusted prices")
    month = date.month
    submitted = st.form_submit_button("Submit")
    if submitted:
        start = datetime(date.year, month, 1)
        end = datetime(date.year, month, monthrange(date.year, month)[1])
        try:
            data = pdr.get_data_yahoo(symbol, start=start, end=end)
        except ValueError:
            print("ValueError, trying again")
            i += 1
            if i < 5:
                time.sleep(10)
                data = pdr.get_data_yahoo(symbol, start=start, end=end)
            else:
                print("Tried 5 times, Yahoo error. Trying after 2 minutes")
                time.sleep(120)
                data = pdr.get_data_yahoo(symbol, start=start, end=end)
        fig = go.Figure(data=go.Ohlc(x=data.index,
                    open=data.Open,
                    high=data.High,
                    low=data.Low,
                    close=data.Close))
        #fig.show()
        st.plotly_chart(fig)