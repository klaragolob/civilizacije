import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getStandardTuple, getMaxPDF, getCDFNIC, getCDFPLOSCINA, normalizePDF, getIndexMaxPDF
from ToyModel import getStandardTupleLOGUNIFORM

import random
import time
import matplotlib.pyplot as plt
import numpy as np
from createHistogram import createHistogram
import scipy.ndimage.filters as fl
from IO import save,readFile

timeStart = time.time()
times = 100

noParameters = 7

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

save(xaxis,yaxis,'Toy model 6 parameters')