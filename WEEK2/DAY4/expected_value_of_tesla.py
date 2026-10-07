import numpy as np
import yfinance as yf
data=yf.download(["TSLA"], period="3mo")
data.to_csv("tesla_data.csv")
returns=data["Close"].pct_change().dropna()
positive_return=(returns>0).mean()
negative_return=(returns<0).mean()
avg_positive_return=returns[returns>0].mean()
avg_negative_return=returns[returns<0].mean()
expected_value=positive_return*avg_positive_return+negative_return*avg_negative_return
print("Expected value of tesla stocks:", expected_value)



import numpy as np

results = np.random.choice(
    [0.03, -0.02],
    size=10000,
    p=[0.55, 0.45]
)

print("Average simulated return:", results.mean())
