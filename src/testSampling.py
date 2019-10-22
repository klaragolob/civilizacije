'''
Created on 14 Aug 2018

@author: benos
'''
import matplotlib.pyplot as plt
from mpLogUniform import mpLogUniform
from mpSampleMultiple import sampleByBisection,StandardiseDistribution,sample
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl

size = 10

dist = mpLogUniform(0.1,1,size)
x = mpLogspace(dist[0],dist[1],size)
# plt.subplot(2,1,1)

#size = 10

#x = mpLogspace(1, 10, size)
#dist = (1, 10, [0, 0, 1/5, 1/5, 2/5, 1/5, 0, 0, 0, 0])

#dist=[x/5 for x in dist]

plt.plot(x, dist[2],'bx')

times = 3000

yS = [0] * size
std = StandardiseDistribution(dist)
for i in range(0, times):
    val = sampleByBisection(std)
    #val = sample(dist)
    
    for p in range(0, size-1):
        if x[p] == val:
            yS[p] += 1
            break
            
yS = [x / sum(yS) for x in yS]

yS = fl.gaussian_filter(yS, 10)

# plt.subplot(2,1,2)
plt.plot(x, yS,'ro')
#plt.xscale('log')
plt.show()

