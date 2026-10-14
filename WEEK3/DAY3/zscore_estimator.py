import numpy as np
import matplotlib.pyplot as plt
import yfinance as y
import pandas as pd
data=y.download(["AAPL","MSFT"], period="6mo")
data.to_csv("data.csv")
prices=data["Close"].dropna()
spread=prices["AAPL"]-prices["MSFT"]
rolling_mean=spread.rolling(30).mean()
rolling_std=spread.rolling(30).std()
z_score=(spread-rolling_mean)/rolling_std

position=0
positions=[]

position = 0
positions = []

for i in range(len(z_score)):
    z = z_score.iloc[i]

    if pd.isna(z):
        position = 0
    elif abs(z) < 0.5:
        position = 0
    elif z > 2:
        position = -1
    elif z < -2:
        position = 1

    positions.append(position)

positions=pd.Series(positions,index=z_score.index)
print(positions.tail(20))

returns = prices.pct_change().fillna(0)

spread_returns = (
    0.5 * returns["AAPL"]
    - 0.5 * returns["MSFT"]
)

strategy_returns = (
    positions.shift(1).fillna(0)
    * spread_returns
)

strategy_growth = ( 
    1 + strategy_returns
).cumprod()

buy_hold_growth = (
    1 + returns["AAPL"]
).cumprod()

print(
    "Strategy return:",
    strategy_growth.iloc[-1] - 1
)

print(
    "AAPL buy-and-hold return:",
    buy_hold_growth.iloc[-1] - 1
)


