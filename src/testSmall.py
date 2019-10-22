import numpy as np
from mpmath import mp
import matplotlib.pyplot as plt
from logHistogramAdd import logHistogramAdd
from mpSampleMultiple import scale
import scipy.ndimage.filters as fl
size = 500
dist = [0]*size

times = 1000
izpis = 0

start = -40
end = 40

for i in range(0,times):
    r = np.random.lognormal(0,14)
    dist = logHistogramAdd(start, end, size, dist, r)
    if i % (times / 10) == 0:
        print(izpis, "%")
        izpis += 10
    
(xaxis,yaxis) = (scale(start, end, size), [float(x) for x in dist])


yaxis = fl.gaussian_filter(yaxis, 5)
print(yaxis)
plt.plot(xaxis, yaxis)
plt.xscale("log")
plt.show()

#print(dist)
    