import numpy as np
import yfinance as yf
data=yf.download(["TSLA"], period="2mo")
data.to_csv("tesla_data.csv")
returns=data["Close"].pct_change().dropna()
positive_returns=returns[returns>0]
negative_returns=returns[returns<0]
print("probability of positive returns:", (returns>0).mean())
print("probability of negative returns:", (returns<0).mean())