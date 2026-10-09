import numpy as np
import yfinance as yf
data=yf.download(["AAPL","MSFT"], period="6mo")
data.to_csv("data.csv")
returns=data["Close"].pct_change().dropna()

weight=[[0.4,0.6],[0.7,0.3],[0.8,0.2]]
covariance=returns.cov()

for w in weight:
    portfolio_return=w[1]*returns["AAPL"]+w[0]*returns["MSFT"]
    print(portfolio_return)

portfolio_variance=w[1]**2*covariance.loc["AAPL","AAPL"]+w[0]**2*covariance.loc["MSFT","MSFT"]+2*w[1]*w[0]*covariance.loc["AAPL","MSFT"]
portfolio_volatility=np.sqrt(portfolio_variance)

print("volatility:", portfolio_volatility)
sharpe_ratio=portfolio_return.mean()/ portfolio_volatility
print("sharpe ratio:", sharpe_ratio)