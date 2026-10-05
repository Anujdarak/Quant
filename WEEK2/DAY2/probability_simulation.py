import numpy as np
re=np.random.choice([0,1], size=500, p=[0.5,0.5])
print(re)

print("Number of tails:", np.sum(re==0))
print("Number of heads:", np.sum(re==1))
print("probability of getting Heads:", np.mean(re==1))
print("probability of getting tails:", np.mean(re==0))


re2=np.random.binomial(n=10, p=0.5, size=1000)
print(re2)
tails=10-re2
print("tails:", tails)

normal_date=np.random.normal(loc=0, scale=1, size=500)
print("mean:", np.mean(normal_date))
print("std:", np.std(normal_date))