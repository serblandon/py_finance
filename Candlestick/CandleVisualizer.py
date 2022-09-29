import yfinance as yf
import pandas as pd
import mplfinance as mpl

df = yf.Ticker("META").history(period="max")

df = df.loc["2021-09-30":]

mpl.plot(df, type="candle", volume=True)
