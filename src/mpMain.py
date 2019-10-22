'''
Created on 8 Aug 2018

@author: benos
'''

from mpSampleMultiple import mpSampleMultiple, mpSampleMultipleTime, sampleL
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from lifeDist import lifeDist
from mpmath import mpmathify
import time
from meanMedian import meanMedian
from IO import save, readFile

size = 2151;
# size=500;

timeStart = time.time()
'''
OLD
Rstar = mpUniform(1, 100, size)
Fplanets = mpUniform(0.1, 1, size)
Nhabitable = mpUniform(0.1, 1, size)
# Flife = lognormal(10**(-40),1,size)
# Flife = loguniform(1,1000,size)
# Flife = (0,1,lifeDist(size,size/2))
Flife = mpUniform(mpmathify(10 ** (-156)), 1, size)
Fintelligence = mpUniform(0.001, 1, size)
Fcivilization = mpUniform(0.01, 1, size)
Length = mpUniform(100, 10000000000, size)


LOGUNIFORM
Rstar = mpLogUniform(1, 100, size)
Fplanets = mpLogUniform(0.1, 1, size)
Nhabitable = mpLogUniform(0.1, 1, size)
# Flife = lognormal(10**(-40),1,size)
# Flife = loguniform(1,1000,size)
#Flife = (0,1,lifeDist(size,size/2))
Flife = mpUniform(mpmathify(10**(-156)),1,size)
Fintelligence = mpLogUniform(0.001, 1, size)
Fcivilization = mpLogUniform(0.01, 1, size)
Length = mpLogUniform(100, 10000000000, size)
'''

Rstar = (1, 100)
Fplanets = (0.1, 1)
Nhabitable = (0.1, 1)
# Flife = lognormal(10**(-40),1,size)
# Flife = loguniform(1,1000,size)
# Flife = (0,1,lifeDist(size,size/2))
# Flife = (mpmathify(10 ** (-156)), 1)
Fintelligence = (0.001, 1)
Fcivilization = (0.01, 1)
Length = (100, 10000000000)
'''
Flife = (1, -35, 15, 14, 17, 0, 50)
N = readFile('sigma is 50.csv')
(xaxis, yaxis) = sampleL([Rstar, Fplanets, Nhabitable, Fintelligence, Fcivilization], -100, 100, size, 230000, Flife, (1, N))
save(xaxis, yaxis, 'What is L with N sig50')


Flife = (1,-35,15,14,17,0,100)

(xaxis, yaxis) = mpSampleMultipleTime([Rstar, Fplanets, Nhabitable, Fintelligence, Fcivilization, Length],-120,15, size, 50000,Flife)
save(xaxis, yaxis, 'sigma is 100')
'''


Flife = (1,-35,15,14,17,0,200)

(xaxis, yaxis) = mpSampleMultiple([Rstar, Fplanets, Nhabitable, Fintelligence, Fcivilization, Length],-40,15, size, 10000,Flife)
save(xaxis, yaxis,'sigma is 200 uniform2')
'''
Flife = (1,-35,15,14,17,0,10**50)

(xaxis, yaxis) = mpSampleMultipleTime([Rstar, Fplanets, Nhabitable, Fintelligence, Fcivilization, Length],-100,15, size, 1000,Flife)
save(xaxis, yaxis, 'big sigma')
'''
(mean, median) = meanMedian(xaxis, yaxis)

print("done")
# print("time: ", (time.time() - timeStart))
# print("\nMean: ", mean, "\nMedian: ", median)

# yaxis = fl.gaussian_filter(yaxis, 10)

# plt.plot(xaxis, yaxis)
# plt.xscale("log")
# plt.show()

