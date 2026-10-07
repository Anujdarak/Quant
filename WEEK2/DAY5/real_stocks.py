import yfinance as yf
data=yf.download(["AAPL","TSLA"], period="3mo")
data.to_csv("stock_data.csv")

returns=data["Close"].pct_change().dropna()
mean_return=returns.mean()
weight_aapl=75
weight_tsla=25
portfolio_return=weight_aapl*mean_return["AAPL"]+weight_tsla*mean_return["TSLA"]
print("portfolio return:", portfolio_return)