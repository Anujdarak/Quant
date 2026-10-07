import yfinance as yf
import numpy as np
data=yf.download(["AAPL", "MSFT"], period="3mo")
data.to_csv("stock_data.csv")

returns=data["Close"].pct_change().dropna()
variance_aapl=returns["AAPL"].var()
variance_msft=returns["MSFT"].var()
weight_aapl=60
weight_msft=40
covariance=returns["AAPL"].cov(returns["MSFT"])
portfolio_variance=weight_aapl**2*variance_aapl+weight_msft**2*variance_msft+2*covariance*weight_aapl*weight_msft
portfolio_volatility=np.sqrt(portfolio_variance)
print("volatility:", portfolio_volatility)
print("Variance:", portfolio_variance)
volatility_aapl=returns["AAPL"].std()
volatility_msft=returns["MSFT"].std()
print("Volatility AAPL:", volatility_aapl)
print("Volatility MSFT:", volatility_msft)
correlation=returns.corr()
print("Correlation:", correlation)