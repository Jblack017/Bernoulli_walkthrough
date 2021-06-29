import numpy as np
# Coin Flip
# Bernoulli_1
#   np.random.binomial(1, 0.5, 1)

# Bernoulli_2
# for i in range(10):
#   np.random.binomial(1, 0.5, 1)

# Bernoulli_3
# for i in range(10):
#   np.random.binomial(1, 0.5, 10)

# Bernoulli_4
# for i in range(10):
#   np.random.binomial(20, 0.5, 10)

# Bernoulli_5
# np.random.binomial(5, 0.5, 20)

# Bernoulli_7
np.random.seed(seed=567) 
n_1000 = np.random.binomial(n=5, p=0.5, size=1000)
n_10000 = np.random.binomial(n=5, p=0.5, size=10000)
n_100000 = np.random.binomial(n=5, p=0.5, size=100000)

print(f"1000 Times:    ",np.sum(n_1000 == 4) /1000)
print(f"10,000 Times:  ",np.sum(n_10000 == 4) /10000)
print(f"100,000 Times: ",np.sum(n_100000 == 4) /100000)

print(np.sum([0.155, 0.1536, 0.15733])/3)

# https://prep.flatironschool.com/library/hotel-booking-optimization/205220/path/step/118827874/