import numpy as np
import matplotlib.pyplot as plt
import yfinance as y
data=y.download(["AAPL","MSFT"], period="6mo")
data.to_csv("data.csv")
prices=data["Close"].dropna()
spread=prices["AAPL"]-prices["MSFT"]
rolling_mean=spread.rolling(30).mean()
rolling_std=spread.rolling(30).std()
z_score=(spread-rolling_mean)/rolling_std

plt.figure(figsize=(12, 6))
plt.plot(z_score.index, z_score, label="Spread Z-score")
plt.axhline(2, linestyle="--", label="Upper threshold")
plt.axhline(-2, linestyle="--", label="Lower threshold")
plt.axhline(0, linestyle=":")
plt.legend()
plt.grid(True)
plt.savefig("pairs_trading.png")
plt.show()
