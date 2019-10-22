import numpy as np
import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from IO import saveData,readData
from lifeDist import lifeDist, lifeDist2


plt.figure(1)
logArray = readData("newLowerBound")
# normed=1,rwidth=0.95
#n, bins, patches = plt.hist(logArray, 1000, facecolor='red', alpha=0.75,cumulative=True)
#plt.axis([-5, 50,0,25000])
n, bins, patches = plt.hist(logArray, 1000, facecolor='blue', alpha=0.75)

maxi = 0
index =0
for r in range(0,len(n)):
    if n[r]>maxi:
        maxi = n[r]
        index = r

print("max:",bins[index])
#plt.grid(True)
#plt.axis([-5, 100,0,400])
#plt.show()

plt.figure(2)
normArray = [np.power(10,a) for a in logArray]


for i in range(0,4):

    start=0
    end=10**(i)
    plt.subplot(2,2,i+1)
    plt.axis([start, end,0,2000])
    #plt.hist(normArray,np.linspace(start,end,1000),facecolor='red',alpha=0.75,cumulative=True)
    plt.hist(normArray,np.linspace(start,end,100),facecolor='blue',alpha=0.75)
    plt.title(str(start)+' - '+str(end))
    plt.tight_layout()

plt.show()