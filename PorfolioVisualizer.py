import pandas_datareader as web
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import colors

# get number of assets
nb_of_assets = int(input("How many assets do you have in your portfolio? "))

# dictionary of ticker: nbofshares
assets_shares = {}

# current prices of stocks
actual_prices = []

# total sum of shares owned
total = []

# building the owned portfolio
for i in range(nb_of_assets):
    ticker = input("Ticker symbol of asset: (capital letters): ")
    assets_shares[ticker] = int(input("Number of shares bought: "))

for ticker in assets_shares.keys():
    df = web.DataReader(ticker, "yahoo", dt.datetime(2022, 9, 28), dt.datetime.now())
    price = df[-1:]["Close"][0]
    actual_prices.append(price)
    total_sum = price * assets_shares[ticker]
    total.append(total_sum)

# print(actual_prices)
# print(total)

# print(assets_shares)

fig = plt.figure(figsize=(9,6))
plt.pie(total, labels=assets_shares.keys(), autopct="%1.2f%%")

#legend
plt.legend(assets_shares.keys(), loc="best")

# percentage

plt.title("Your asset portfolio")
plt.show()
