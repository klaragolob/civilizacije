'''
from mpmath import mp
from mpLogspace import mplogspace


print(mp.log(100,10))
print(mpLogspace(1,100,10))
print(mpLog10space(1,100,10))
import matplotlib.pyplot as plt   
x = mpLogspace(1, 100, 10)
#y = mpLog10space(1, 100, 10)
plt.plot(x, mpLogUniform(1,100,10), 'ro' , color='red')
#plt.plot(y, y, 'ro' ,color = 'blue')
plt.xscale('log')
plt.show()
'''


'''
from mpLogspace import mpLogspace
from mpLogUniform import mpLogUniform
import numpy as np
from mpmath import mpmathify
mu, sigma = 3., 1. # mean and standard deviation

import matplotlib.pyplot as plt

x = np.logspace(-3, 4, 10000)
#pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))

low = mpmathify(10**(-3))
high = mpmathify(10**4)
pdf = mpLogUniform(mpmathify(low), mpmathify(high) , 10000)[2]

plt.plot(pdf , linewidth=2, color='red')
plt.xscale('log')
plt.xlim(10**(-3), 10**4)
plt.show()
'''



