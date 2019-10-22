import numpy as np
from math import *

"""
Generous estimates made in the article:
""" 
mean = 0.5
median = 0.63

mu = log(median, e)
print(mu)
print(2 * ( mean - mu))
sigma = pow(10,10) 


s = np.random.lognormal(mu, sigma, 100000)
print(s)

import matplotlib.pyplot as plt

"""
count, bins, ignored = plt.hist(s, 100, normed=True, align='mid')
print("bins: ")
print(bins)
print(min(bins))
print(max(bins))
"""

x = np.linspace(0.000000000000000000001, 1 , 1000000)
print(" ")
print("x: ")
print(x)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))
       / (x * sigma * np.sqrt(2 * np.pi)))

plt.plot(x, pdf, linewidth=2, color='r')

plt.xscale('log')
plt.show()









"""
import numpy as np
import matplotlib.pyplot as plt
from math import log

# Generate a thousand samples: each is the product of 100 random
# values, drawn from a normal distribution.
b = []
for i in range(1000):
   a = 10. + np.random.random(100)
   b.append(np.product(a))

b = np.array(b) / np.min(b) # scale values to be positive
count, bins, ignored = plt.hist(b, 100, normed=True, align='mid')
sigma = np.std(np.log(b))
mu = np.mean(np.log(b))

x = np.linspace(min(bins), max(bins), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))

plt.plot(x, pdf, color='r', linewidth = 2)
plt.show()
"""
"""
import numpy as np
import scipy as sp

class log_uniform():        
    def __init__(self, a=-1, b=0, base=10):
        self.loc = a
        self.scale = b - a
        self.base = base

    def rvs(self, size=None, random_state=None):
        uniform = sp.stats.uniform(loc=self.loc, scale=self.scale)
        if size is None:
            return np.power(self.base, uniform.rvs(random_state=random_state))
        else:
            return np.power(self.base, uniform.rvs(size=size, random_state=random_state))
            """
            
