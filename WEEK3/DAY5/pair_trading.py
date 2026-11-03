import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

data = yf.download(
    ["CUPID.NS", "RELIANCE.NS"],
    period="6mo"
)

prices = data["Close"].dropna()
x = prices["RELIANCE.NS"].values
y = prices["CUPID.NS"].values

beta, alpha = np.polyfit(x, y, 1)

print("Hedge Ratio:", beta)
print("Intercept:", alpha)

spread = prices["CUPID.NS"] - (
    alpha + beta * prices["RELIANCE.NS"]
)
rolling_mean = spread.rolling(25).mean()
rolling_std = spread.rolling(25).std()

z_score = (spread - rolling_mean) / rolling_std

signals = np.zeros(len(z_score))

signals[z_score > 2] = -1
signals[z_score < -2] = 1

position = np.zeros(len(signals))
current_position = 0

for i in range(1, len(signals)):

    if current_position == 0:

        if z_score.iloc[i] > 2:
            current_position = -1

        elif z_score.iloc[i] < -2:
            current_position = 1

    elif abs(z_score.iloc[i]) < 0.5:
        current_position = 0

    position[i] = current_position

price_changes = prices.diff()

pair_pnl = (
    price_changes["CUPID.NS"]
    - beta * price_changes["RELIANCE.NS"]
)

gross_exposure = (
    prices["CUPID.NS"].shift(1).abs()
    + abs(beta) * prices["RELIANCE.NS"].shift(1).abs()
)

pair_returns = pair_pnl / gross_exposure

# Step 9: Calculate strategy returns
position_series = pd.Series(
    position,
    index=prices.index
)

strategy_returns = (
    position_series.shift(1) * pair_returns
).dropna()

# Step 10: Calculate performance
growth = (1 + strategy_returns).cumprod()

total_return = growth.iloc[-1] - 1

daily_volatility = strategy_returns.std()

annualized_volatility = daily_volatility * np.sqrt(252)

if daily_volatility != 0:
    sharpe = (
        strategy_returns.mean() / daily_volatility
    ) * np.sqrt(252)
else:
    sharpe = 0

print("Total Return:", total_return)
print("Annualized Volatility:", annualized_volatility)
print("Annualized Sharpe Ratio:", sharpe)

plt.figure(figsize=(10, 5))

plt.plot(
    growth.index,
    growth,
    label="Pairs Trading"
)

plt.title("Pairs Trading Backtest")
plt.xlabel("Date")
plt.ylabel("Growth of 1")
plt.legend()
plt.grid(True)

plt.savefig("pairs_backtest.png")
plt.show()