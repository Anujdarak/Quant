import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

df = yf.download("AAPL", period="1y")

print(df.head())
df.to_csv("Apple_processed.csv")

df["daily_change"]=df["Close"].pct_change()

df["cumulative_return"]=(1+df["daily_change"]).cumprod()


plt.figure(figsize=(12,5))

plt.plot(df.index, df["cumulative_return"])

plt.title("Growth of ₹1 Invested in Apple")
plt.xlabel("Date")
plt.ylabel("Growth")
plt.grid(True)

plt.savefig("charts/cumulative_return.png")
plt.show()

df["avg_of_10"]=df["Close"].rolling(10).mean()
df["avg_of_50"]=df["Close"].rolling(50).mean()

df["signal"]=(df["avg_of_10"]>df["avg_of_50"]).astype(int)

print(df[["Close", "daily_change", "cumulative_return", "avg_of_10", "avg_of_50", "signal"]].tail(10))

plt.figure(figsize=(12,6))

plt.plot(df.index, df["Close"], label="Close")
plt.plot(df.index, df["avg_of_10"], label="MA10")
plt.plot(df.index, df["avg_of_50"], label="MA50")

plt.title("Moving Average Crossover")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)

plt.savefig("charts/ma_crossover.png")
plt.show()
