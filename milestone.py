# -*- coding: utf-8 -*-
"""
Data Incubator milestone project: stock chart
"""

import datetime
from pandas import DataFrame
from pandas_datareader import data as pdr
import yfinance as yf
from math import pi

import streamlit as st
from bokeh.plotting import figure, show, output_file

yf.pdr_override()
#symbol = "TSLA"

TOOLS = "pan,wheel_zoom,box_zoom,reset,save"
w = 12*60*60*1000/2000
#show(p)

st.title("Shahar's milestone project")

with st.form("my_form"):
    symbol = st.text_input("Ticker?")
    date = st.date_input('Date input')
    year = date.year
    #last_day = datetime.datetime(year, month+1, 1)-1
    month = st.number_input("Month", min_value=1, max_value=12)
    year = st.number_input("Year", min_value=1990, value=2021)
    #month = date.month
    submitted = st.form_submit_button("Submit")
    if submitted:
        start = datetime.datetime(year, month, 1, 1)
        end = datetime.datetime(year, month+1, 1)
        
        
        
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
            
            
            
        #data = pdr.get_data_yahoo(symbol, start=start, end=end)
        p = figure(x_axis_type="datetime", tools=TOOLS, title = symbol)
        p.xaxis.major_label_orientation = pi/4
        p.segment(data.index, data.High, data.index, data.Low, color="black")
        p.vbar(data.index, w, data.Open, data.Close, fill_color="#D5E1DD", line_color="black")
        st.bokeh_chart(p)
        #show(p)


#adjusted = st.checkbox("Display adjusted prices")


# With a little help from https://stackoverflow.com/questions/43150211/python-bokeh-ohlc-plot-from-pandas-df


#st.bokeh_chart(p) does not seem to work
#st.write(p)