'''
Created on 9 Aug 2018

@author: benos
'''
from mpmath import mpmathify,mp,mpf
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
from mpLogNormal import mpLogNormal
from mpSampleMultiple import StandardiseDistribution

size = 50
low = 10**(-188)
high = 10**10
mpLow = mpmathify( low )
mpHigh = mpmathify( high )
mpMedian = mpmathify(1)
mpSigma = mpmathify(10**50)

x = mpLogspace(low, high, size)

#lamb = mpLogNormal( mp.log(mpf('10')**(-188)) , mp.log(mpf('1')), size, mpf('1'), mpmathify(10**50) )[2]
lamb = mpLogNormal( mpLow , mpHigh , size, mpMedian, mpSigma )[2]
stdDistribution = StandardiseDistribution((mpLow, mpHigh, lamb) )
lambPDF = stdDistribution[2]
lambCDF = stdDistribution[3]

print(x)
print(lamb)
print(lambPDF)
print(lambCDF)

plt.plot(x, lambPDF, 'ro')
plt.plot(x, lambCDF, 'ro')
plt.xscale('log')
plt.xlim(low, high)
plt.show()
