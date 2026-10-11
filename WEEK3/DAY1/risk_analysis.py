
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt


data = yf.download(["AAPL", "MSFT"], period="6mo")
returns = data["Close"].pct_change().dropna()
weight_aapl = 0.6
weight_msft = 0.4

portfolio_returns = (
    weight_aapl * returns["AAPL"]
    + weight_msft * returns["MSFT"]
)
losses=-portfolio_returns
var_95=losses.quantile(0.95)
worst_losses=losses[losses>=var_95]
cvar=worst_losses.mean()
initial_amount=10000
var_rupees=initial_amount*var_95
cvar_rupees=initial_amount*cvar
print("varloss:", var_95)
print("cvarloss:", cvar)
print("moneylostmin:", var_rupees)
print("moneylostmax:", cvar_rupees)

plt.hist(losses,bins=50)
plt.axvline(var_95, linestyle="--", label="95% VaR")
plt.title("Portfolio loss distribution")
plt.xlabel("daily loss")
plt.ylabel("frequency")
plt.legend()
plt.savefig("risk_analysis.png")
plt.show()