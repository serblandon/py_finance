import datetime as dt
import pandas_datareader as web
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import mplfinance as mpf

# Time frame

start_date = dt.datetime(2022, 9, 1)
finish_date = dt.datetime.now()

# Data
data = web.DataReader("META", "yahoo", start_date, finish_date)

# insert index column first
#data.reset_index(inplace=True)

mpf.plot(data, type="candle", volume=True, show_nontrading=True)

print(data)
