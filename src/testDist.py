'''
Created on 10 Aug 2018

@author: benos
'''

import random
import numpy as np
from mpmath import mp,mpmathify
from mpLogspace import mpLogspace
from logHistogramAdd import logHistogramAdd
import matplotlib.pyplot as plt
from lifeDist import lifeDist



size = 300
times = 500
y = lifeDist(size,times)

start = mpmathify(10**(-220))
end = mpmathify(10**(10))

x = mpLogspace(start, end, size)

plt.plot(x, y)
plt.xscale("log")
#plt.xlim(start , end)
plt.show()