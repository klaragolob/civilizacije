'''
Created on 13 Aug 2018

@author: benos
'''
import time
from meanMedian import meanMedian
from IO import save,readFile
import scipy.ndimage.filters as fl
import matplotlib.pyplot as plt
from createGraph import createGraph
from StandardizeDistribution import StandardizeDistributionW
import numpy as np

(xaxis,yaxis) = readFile("laplace_new")

'''
xaxis2=[0]*len(xaxis)
xaxis2[0]=np.round(np.log10(xaxis[0]))
yaxis[0]=int(yaxis[0])
for i in range(1,len(xaxis)):
    xaxis2[i]=int(np.round(np.log10(xaxis[i])))
    yaxis[i]=int(yaxis[i])
    
save(xaxis2,yaxis,"sigma is 100 exponents")
'''


avg=0
for i in range(0,len(xaxis)):
    avg+=yaxis[i]*xaxis[i]
avg/=sum(yaxis)
print(sum(yaxis))
#avg=avg-24821395

    
#yaxis = fl.gaussian_filter(yaxis, 5)

(mean,median) = meanMedian(xaxis,yaxis)

print("\nMean: ", mean, "\nMedian: ", median)
print("Average: ",avg)

#createGraph(xaxis,yaxis,start,end,size)
(length, xaxis, yaxis, cdf,cdfW )= StandardizeDistributionW(xaxis,yaxis)

ylimStart=0
ylimEnd=1

plt.figure(1)
multiplier = -10

plt.subplot(4,2,1)
fromN = 10**(0+multiplier)
fromN=0
toN = 10**(2+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.ylim( ylimStart , ylimEnd )
plt.plot(x,y)

plt.subplot(4,2,2)
fromN = 10**(2+multiplier)
fromN=0
toN = 10**(4+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.ylim( ylimStart , ylimEnd )
plt.plot(x,y)

plt.subplot(4,2,3)
fromN = 10**(4+multiplier)
fromN=0
toN = 10**(6+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.ylim( ylimStart , ylimEnd )
plt.plot(x,y)

plt.subplot(4,2,4)
fromN = 10**(6+multiplier)
fromN=0
toN = 10**(8+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.ylim( ylimStart , ylimEnd )
plt.plot(x,y)

plt.subplot(4,2,5)
fromN = 10**(8+multiplier)
fromN=0
toN = 10**(10+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.ylim( ylimStart , ylimEnd )
plt.plot(x,y)

plt.subplot(4,2,6)
fromN = 10**(10+multiplier)
fromN=0
toN = 10**(12+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.ylim( ylimStart , ylimEnd )
plt.plot(x,y)

plt.subplot(4,2,7)
fromN = 10**(12+multiplier)
fromN=0
toN = 10**(14+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.ylim( ylimStart , ylimEnd )
plt.plot(x,y)

plt.subplot(4,2,8)
fromN = 10**(14+multiplier)
fromN=0
toN = 10**(16+multiplier)
plt.title(str(fromN)+' - '+str(toN))
(x,y) = createGraph(xaxis,yaxis,fromN,toN,1000)
plt.ylim( ylimStart , ylimEnd )
plt.plot(x,y)

plt.tight_layout()
plt.ylim( 0 , 1 )
plt.figure(2)

#yaxis = fl.gaussian_filter(yaxis, 15)


plt.plot(xaxis,cdf,'red', label = 'CDF')
#plt.plot(xaxis,cdfW,'green')
#plt.title('5 parameters')


#plt.yscale("log")
#plt.ylim(0,0.0200)

plt.xscale("log")
plt.plot(xaxis, yaxis,'blue',label='PDF')
plt.legend(loc=4)


plt.show()

