'''
Created on 21 Aug 2018

@author: benos
'''

# from ToyModel import getStandardTuple
import random
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
import numpy as np
from ToyModel import getStandardTuple
# def getStandardTuple(size=100000, pdfSize=10001, low=0 , high=0.2, lowerThan = 1, stParametrov = 9, start = -5, stop=5 ):
#    return (arrayOfParameters, alonePossibility, x, pdf, cdfNIC, cdfPLOSCINA)


def getSampleMult(start, end, no, times):
    dist = [0] * times
    avg = 0
    for t in range(0, times):
        r = 1
        for _ in range(0, no):
            r *= random.uniform(start, end)
        dist[t] = r
        avg += r
    avg /= times
    return avg

    
size = 10000
distE1 = [0] * size
distE2 = [0] * size
distE3 = [0] * size
low = 0
high = 0.2
no = 9
times = 10000
goal = (0.1) ** no *10**11   
epsMax = (1 / 6) ** 3
epsX = [0] * size

hBil = 100000

goalGraphY = [goal] * size
goalGraphX = range(0, size)
eps = 0.05

(arrayOfParameters, alonePossibility, x, pdf, cdfNIC, cdfPLOSCINA) = getStandardTuple(size, 10001, low+eps, high-eps, 1, no, -5, 5,10**11)
#pdf = fl.gaussian_filter(pdf, 10)

plt.plot(x,pdf)
plt.plot([goal,goal],[1,0],'r-')
#plt.xscale('log')
plt.xlim(0,200)
plt.show()

'''
# Case 1: e->
# Case 2: e-> <-e
# Case3: e-> e->
izpis = 0
for i in range(0, size):
    eps = epsMax*(i/size)
    epsX[i] = eps
    distE1[i] = getSampleMult(start + eps, end, no, times)
    distE2[i] = getSampleMult(start + eps, end - eps, no, times)
    distE3[i] = getSampleMult(start + eps, end + eps, no, times)
    if i % (size / 10) == 0:
        print(izpis, "%")
        izpis += 10
        
sigma = 15
distE1 = fl.gaussian_filter(distE1, sigma)
distE2 = fl.gaussian_filter(distE2, sigma)
distE3 = fl.gaussian_filter(distE3, sigma)

plt.figure(1)    
plt.plot(epsX, goalGraphY, 'red')
plt.plot(epsX,distE1,'green')
plt.plot(epsX,distE2,'blue')
plt.plot(epsX,distE3,'yellow')
#plt.xscale('log')
plt.show()

plt.figure(2)
H1 = np.histogram(distE1,size)
print(H1)
#H2 = np.histogram(distE2,size)
#H3 = np.histogram(distE3,size)
plt.hist(H1,bins='auto')
plt.show()
'''

