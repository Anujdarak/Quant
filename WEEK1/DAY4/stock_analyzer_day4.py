
import yfinance as yf
import pandas as pd

df = yf.download("AAPL", period="1y")

print(df.head())

h=df.head()
print(h)
t=df.tail()
print(t)
i=df.info()
print(i)

closing_prices=df["Close"].max()
print(closing_prices)
lowest_price=df["Close"].min()
print(lowest_price)
avg=df["Close"].mean()
print(avg)
avg_vol=df["Volume"].mean()
print(avg_vol)
df["Daily return"]=df["Close"].pct_change()
first_ten=df.head(10)
print(first_ten)

Green_day=df["Close"]>df["Open"]
count=Green_day.sum()
print(count)
days=df["Volume"]>df["Volume"].mean()
print(days)

df.to_csv("Apple_stock_data.csv")



TASK 6:
