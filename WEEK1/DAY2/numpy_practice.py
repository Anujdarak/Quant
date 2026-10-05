TASK2:
EXERCISE A:

import numpy as np
arr = np.array([5,10,15,20,25,30,35])
three=arr[:3]
last=arr[-2:]
middle=arr[2:6]
print(three)
print(last)
print(middle)

EXERCISE B:

import numpy as np
prices = np.array([98,102,110,95,120,99])
re=prices[prices>100]
print(re)


EXERCISE C:

import numpy as np
returns = np.array([1.2,-0.5,3.1,0.8])
re=returns/100
print(re)

EXERCISE D:

import numpy as np
prices = np.array([100,103,101,108,112,109])
highest=np.max(prices)
lowest=np.min(prices)
avg=np.mean(prices)
aboveavg=prices[prices>avg]
dailychange=prices[1:]-prices[:-1]
print(highest)
print(lowest)
print(avg)
print(aboveavg)
print(dailychange)


TASK 4:

q1:1/6
q2:3/4
q3:21/6


TASK 5:
q1:36
q2:3
q3:4096
q4:28
q5:2000

