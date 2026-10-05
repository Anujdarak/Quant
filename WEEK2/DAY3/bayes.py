import numpy as np
p_a=0.1
p_b=0.02
p_a_given_b=0.9

p_b_given_a=(p_a_given_b*p_b)/p_a
print("probability of B given A:", p_b_given_a)