import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF, getIndexMaxPDF
from ToyModel import getAlonePossibility, getAlonePossibilityLOGUNIFORM 


lowEpsilon = 0.0
highEpsilon = 0.04
sizeOfEpsilonRange = 100

lowEpsilonLOG = -8
highEpsilonLOG = np.log10(0.19)

xEpsilon = np.linspace(lowEpsilon, highEpsilon, sizeOfEpsilonRange)
xEpsilonLOG = np.logspace( lowEpsilonLOG , highEpsilonLOG , sizeOfEpsilonRange )

pdf1 = []
for epsilon in xEpsilonLOG:
    value = getAlonePossibilityLOGUNIFORM( epsilon, high = 0.2 - epsilon, lowerThan=1)
    pdf1.append(value)
'''
pdf2 = []
for epsilon in xEpsilonLOG:
    value = getAlonePossibilityLOGUNIFORM(low=0.001 + epsilon, high = 0.2 - epsilon, lowerThan=1)
    pdf2.append(value)
'''
'''
pdf3 = []
for epsilon in xEpsilon:
    value = getAlonePossibility(low=epsilon, high = 0.2, lowerThan=0.5)
    pdf3.append(value)
'''

plt.plot(xEpsilonLOG, pdf1, label = 'range( e , 0.2-e )')
#plt.plot(xEpsilonLOG, pdf2, label = 'range(0.001+e , 0.2-e )')
#plt.plot(xEpsilon, pdf3, label = 'cutoff = 0.5')
plt.title('logUniform , cutoff is 1')
plt.ylabel('probability of being alone')
plt.xlabel('epsilon')
plt.legend( loc=3)
plt.xscale('log')
plt.xlim(lowEpsilon, highEpsilon)
plt.show()

