import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download 1 year of NVIDIA stock data
df = yf.download("NVDA", period="1y")

# Save raw data
df.to_csv("NVDA_processed.csv")

# Daily returns
df["daily_change"] = df["Close"].pct_change()

# Moving averages
df["MA20"] = df["Close"].rolling(20).mean()
df["MA40"] = df["Close"].rolling(40).mean()

# Trading signal
df["signal"] = (df["MA20"] > df["MA40"]).astype(int)

# Strategy return (avoids look-ahead bias)
df["strategy_return"] = df["signal"].shift(1) * df["daily_change"]

# Strategy growth
df["strategy_growth"] = (1 + df["strategy_return"]).cumprod()

# Maximum Drawdown
df["peak"] = df["strategy_growth"].cummax()
df["drawdown"] = (df["strategy_growth"] - df["peak"]) / df["peak"]

max_drawdown = df["drawdown"].min()
print("Maximum Drawdown:", max_drawdown)

# Drawdown Graph
plt.figure(figsize=(12, 5))
plt.plot(df.index, df["drawdown"], color="red")
plt.title("Maximum Drawdown")
plt.xlabel("Date")
plt.ylabel("Drawdown")
plt.grid(True)
plt.savefig("charts/drawdown.png")
plt.show()

# Win Rate
winning_days = (df["strategy_return"] > 0).sum()
trading_days = (df["signal"] == 1).sum()

if trading_days > 0:
    win_rate = winning_days / trading_days
else:
    win_rate = 0

print("Winning Days:", winning_days)
print("Trading Days:", trading_days)
print("Win Rate:", win_rate)