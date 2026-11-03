import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
data=yf.download(["PCJEWELLER.NS","CUPID.NS"],period="6mo")
data.to_csv("data.csv")
prices=data["Close"].dropna()
spread=prices["PCJEWELLER.NS"]-prices["CUPID.NS"]
rolling_mean=spread.rolling(30).mean()
rolling_std=spread.rolling(30).std()
z_score=(spread-rolling_mean)/rolling_std
signals=np.zeros(len(z_score))
signals[z_score>2]=-1
signals[z_score<-2]=1
signals[z_score.abs()<0.5]=0
print("latest spread:", spread.iloc[-1])
print("latest z_score:", z_score.iloc[-1])
print("latest signal:", signals[-1])

# Step 6: Plot spread
plt.figure(figsize=(12, 5))
plt.plot(spread.index, spread, label="Spread")
plt.plot(rolling_mean.index, rolling_mean, label="20-day Mean")
plt.title("PCJEWELLER-CUPID Spread")
plt.xlabel("Date")
plt.ylabel("Price Difference")
plt.legend()
plt.savefig("spread.png")
plt.show()

# Step 7: Plot Z-score
plt.figure(figsize=(12, 5))
plt.plot(z_score.index, z_score, label="Z-score")
plt.axhline(2, linestyle="--", label="Upper Threshold")
plt.axhline(-2, linestyle="--", label="Lower Threshold")
plt.axhline(0, linestyle=":", label="Mean")
plt.title("PCJEWELLER-CUPID Z-score")
plt.xlabel("Date")
plt.ylabel("Z-score")
plt.legend()
plt.savefig("zscore.png")
plt.show()