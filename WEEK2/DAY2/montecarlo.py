import numpy as np
mean=0.0005
current_price=150
volatility=0.01
simulations=500
daily_return=np.random.normal(mean, volatility, simulations)

future_return=current_price * (1+daily_return)
print("Future price:", future_return)
print("mean of future price:", future_return.mean())
print("maximum price:", future_return.max())
print("minimum price:", future_return.min())
