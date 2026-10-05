import numpy as np
import yfinance as yf
data=yf.download(["TSLA"], period="6mo")
data.to_csv("tesla_data.csv")

returns=data["Close"].pct_change()
required =returns.dropna()
current_prices=100
mean=required.mean()
volatility=required.std()
daily_return=np.random.normal(mean, volatility,500)
future_prices=current_prices*(1+daily_return)
print("Futureprices:", future_prices)
print("mean of future prices:", future_prices.mean())
print("maximum price:", future_prices.max())
print("minimum price:", future_prices.min())