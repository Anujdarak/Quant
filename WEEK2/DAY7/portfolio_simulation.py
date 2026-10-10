import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
data=yf.download(["AAPL","MSFT"], period="7mo")
data.to_csv("data.csv")
returns=data["Close"].pct_change().dropna()
weight_aapl=0.7
weight_msft=0.3
simulated_return=returns.sample(n=10000, replace=True)
portfolio_return=weight_aapl*simulated_return["AAPL"]+weight_msft*simulated_return["MSFT"]
initial_money=10000
final_money=initial_money*(1+portfolio_return)
avg_return=portfolio_return.mean()
negative_probability=(portfolio_return<0).mean()
worst_5_percent=portfolio_return.quantile(0.05)
print("final money:", final_money)
print("average return:", avg_return)
print("probability of negative return:", negative_probability)
print("worst 5 percent return:", worst_5_percent)

plt.hist(portfolio_return, bins=50)
plt.title("Portfolio daily return distribution")
plt.xlabel("Portfolio  daily Return")
plt.ylabel("Frequency")
plt.savefig("portfolio_return.png")
plt.show()


