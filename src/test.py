'''
Created on 6 Aug 2018

@author: benos
'''

# test.py
import random
import numpy as np
from mpmath import *
from mpLogspace import mpLogspace
from logHistogramAdd import logHistogramAdd
import time
from mpSampleMultiple import StandardiseDistribution
from mpLogUniform import mpLogUniform
from mpLogNormal import mpLogNormal
from mpSampleMultiple import mpSampleMultiple,mpSampleMultipleTime
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from lifeDist import lifeDist
from meanMedian import meanMedian
from IO import save,readFile

mp.dps=7


size = 100
Rstar = mpLogUniform(1, 100, size)
(xaxis, final) = mpSampleMultipleTime([Rstar], size, 10)

final = fl.gaussian_filter(final, 5)
(mean, median) = meanMedian(final, xaxis)
stand = StandardiseDistribution(Rstar)
length = stand[0]
xArray = stand[1]
pdf = stand[2]
cdf = stand[3]
print(xaxis)
print(length)
print(xArray)
print(pdf)
print(sum(pdf))
print(cdf)


print("\nMean: ", mean, "\nMedian: ", median)
plt.plot(xArray, mpLogUniform(1,100, size)[2] )
plt.plot(xArray, pdf , 'ro')
plt.xscale("log")
plt.xlim(1, 10**2)
plt.show()

