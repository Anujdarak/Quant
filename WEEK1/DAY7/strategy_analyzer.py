import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

df = yf.download("NVDA", period="1y")

df.to_csv("nvidia_data.csv")

df["day_change"] = df["Close"].pct_change()

df["MA20"] = df["Close"].rolling(20).mean()

df["MA40"] = df["Close"].rolling(40).mean()

df["signal"] = (df["MA20"] > df["MA40"]).astype(int)

df["strategy_return"] = df["signal"].shift(1) * df["day_change"]

df["strategy_growth"] = (1 + df["strategy_return"]).cumprod()

average_return = df["strategy_return"].mean()

volatility = df["strategy_return"].std()

sharpe_ratio = (average_return / volatility) * (252 ** 0.5)

df["buy_and_hold_growth"] = (1 + df["day_change"]).cumprod()

buy_and_hold_return = df["buy_and_hold_growth"].iloc[-1] - 1

strategy_total_return = df["strategy_growth"].iloc[-1] - 1

print("Average Daily Return:", average_return)

print("Daily Volatility:", volatility)

print("Sharpe Ratio:", sharpe_ratio)

print("Strategy Return:", strategy_total_return)

print("Buy and Hold Return:", buy_and_hold_return)

plt.figure(figsize=(12, 5))

plt.plot(df.index, df["strategy_growth"], label="Strategy")

plt.plot(df.index, df["buy_and_hold_growth"], label="Buy and Hold")

plt.title("Strategy vs Buy and Hold")

plt.xlabel("Date")

plt.ylabel("Growth")

plt.legend()

plt.grid(True)

plt.savefig("charts/strategy_vs_buyhold.png")

plt.show()




