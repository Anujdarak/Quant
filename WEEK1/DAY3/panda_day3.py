TASK 2:

data = {
    "Day": [1,2,3,4,5],
    "Close": [100,103,101,108,112],
    "Volume": [1200,1500,1100,1800,1700]
}

df = pd.DataFrame(data)
print(df)

cl=df["Close"]
print(cl)
vol=df["Volume"]
print(vol)


pricesabove102=df[df["Close"]>102]
print(pricesabove102)

highestclose=df["Close"].max()
lowestclose=df["Close"].min()
avgclose=df["Close"].mean()



TASK 3:


df["dailyreturn"]=df["Close"].pct_change()
print(df)

TASK 5:

q1:1/6
q2:4/8
q3:1/5


TASK 6:

q1:90
q2:100
q3:32768
q4:31
q5:1200


