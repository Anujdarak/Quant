import numpy as np
re=np.random.choice([0,1], p=(0.4,0.6), size=500)
print("total_trades:", len(re))
print("Profitable_trades:", (re==1).sum())
print("probability of protability:", re.mean())

market = np.random.choice(
    [0, 1],
    size=10000,
    p=[0.5, 0.5]
)

trade = np.random.choice(
    [0, 1],
    size=10000,
    p=[0.4, 0.6]
)
print("Probability market goes up:", market.mean())
print("Probability trade is profitable:", trade.mean())