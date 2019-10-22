'''
Created on 27 Aug 2018

@author: benos
'''
import random
import time
import matplotlib.pyplot as plt
import numpy as np
from createHistogram import createHistogram
import scipy.ndimage.filters as fl
from IO import save,readFile

timeStart = time.time()
times = 100

noParameters = 4

noStars = 10**(noParameters+2)

elements = [0]*(times+1)
izpis = 0
for t in range(0,times+1):
    
    summ = 0
    '''
    if t % (times / 10) == 0:
            print("[","|"*int(t/times*10)," "*int(10-t/times*10),"]",izpis, "% time: ",time.time()-timeStart)
            print()
            izpis += 10
            
    
         
    for s in range(0,noStars):
        all1 = 1
        for i in range(0,noParameters):
            if random.random()>random.uniform(0,0.2):
                all1 = 0
        if(all1==1):
            summ+=1
    elements[t]=summ
    '''
    for s in range(0,noStars):
        if random.random()<=0.1**noParameters:
            summ+=1
    elements[t]=summ


(xaxis,yaxis) = createHistogram(elements,range(0,200))

save(xaxis,yaxis,'Toy model 4 parameters brez')

#yaxis = fl.gaussian_filter(yaxis, 10)


#hist1 = np.histogram(elements,range(0,100))
#plt.hist(elements,bins=range(0,400))
#plt.plot(hist1)
#plt.show()
