import numpy as np
import pandas as pd
import yfinance as yf
data=yf.download(["NFLX", "005930.KS"], period="1y")
print(data)
print(data.columns)
data.to_csv("samsung_and_netflix.csv")
prices=data["Close"]
print(prices)

mean_return=prices.pct_change().mean()
print(mean_return)

volatility=prices.pct_change().std()
print(volatility)

covariance=prices.pct_change().cov()
print(covariance)

correlation=prices.pct_change().corr()
print(correlation)




