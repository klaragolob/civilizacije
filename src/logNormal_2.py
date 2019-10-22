import numpy as np
from mpmath import *
import matplotlib.pyplot as plt


mu, sigma = 3., 1. # mean and standard deviation
s = np.random.lognormal(mu, sigma, 1000)
#print(s)
'''
import matplotlib.pyplot as plt
count, bins, ignored = plt.hist(s, 100, normed=True, align='mid')

plt.plot(x, pdf, linewidth=2, color='r')
plt.axis('tight')
plt.show()
'''
xk= np.logspace(10**(-10), 1)
plt.plot(xk)
plt.show()
