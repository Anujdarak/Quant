import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from statsmodels.tsa.stattools import adfuller
data=yf.download(["HFCL.NS","BHEL.NS"],period="6mo")
data.to_csv("data.csv")
prices=data["Close"].dropna()
correlation=prices["HFCL.NS"].corr(prices["BHEL.NS"])
print("Correlation between them:", correlation)
x=prices["HFCL.NS"].values
y=prices["BHEL.NS"].values
alpha,beta=np.polyfit(x,y,1)
spread=prices["BHEL.NS"]-(alpha+beta*prices["HFCL.NS"])
result=adfuller(spread.dropna())
print("adf test result:", result[0])
print("p-value:", result[1])
print("Lags Used:", result[2])
print("Observations:", result[3])
print("Critical Values:", result[4])
print("Best AIC:", result[5])
