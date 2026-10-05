
import numpy as np
import pandas as pd
stock_a = np.array([
    0.02,
    0.01,
    -0.01,
    0.03,
    0.02,
    -0.02,
    0.01,
    0.03
])

stock_b = np.array([
    0.01,
    0.02,
    -0.02,
    0.02,
    0.01,
    -0.01,
    0.02,
    0.01
])
df=pd.DataFrame()
df["Stock A"]=stock_a
df["Stock B"]=stock_b

print(df.corr())
print(df.cov())