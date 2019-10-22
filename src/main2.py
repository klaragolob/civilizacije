import numpy as np
import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from IO import saveData
from lifeDist import lifeDist, lifeDist2

def getPoint(maxL=10):
    RStarSample = random.uniform(0 , 2)
    fPlanets = random.uniform(-1 , 0)
    nEnvironment = random.uniform(-1 , 0)
    fInteligence = random.uniform(-3 , 0)
    fCivilization = random.uniform(-2 , 0)
    L = random.uniform(2 , maxL)
    
    fLife = lifeDist(vMin=-35, vMax=15, tMin=14, tMax=17, mean=0, sigma=200)
    fLifeEks = float(mp.log(fLife, 10))
    
    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    '''
        # modification
    skip = 0
    mini = -RStarSample - L
    for it in (fPlanets, nEnvironment, fInteligence, fCivilization, fLifeEks):
        if it < np.log10(1/(10**-mini+2)):
            skip = 1
            break
        mini-=it
    # modification
    if skip:
        return getPoint()
    #return np.power(10,resitev)
    if(math.isinf(resitev)):
        return getPoint()
    '''   
    return resitev

def getPointNew(maxL=10):
    RStarSample = random.uniform(0 , 2)
    
    if RStarSample < np.log10(0.0015):
        return 'False'
    
    fPlanets = random.uniform(-1 , 0)
    nEnvironment = random.uniform(-1 , 0)
    fInteligence = random.uniform(-3 , 0)
    
    if fInteligence<-9:
        return 'False'
    fCivilization = random.uniform(-2 , 0)
    
    if fCivilization<np.log10(0.2):
        return 'False'
    L = random.uniform(2 , maxL)
    
    fLife = lifeDist(vMin=-35, vMax=15, tMin=14, tMax=17, mean=0, sigma=200)
    
    
    fLifeEks = float(mp.log(fLife, 10))
        
    if fPlanets+nEnvironment+fLifeEks<-5:
        return 'False'
    
    resitev = RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization + L
    '''
        # modification
    skip = 0
    mini = -RStarSample - L
    for it in (fPlanets, nEnvironment, fInteligence, fCivilization, fLifeEks):
        if it < np.log10(1/(10**-mini+2)):
            skip = 1
            break
        mini-=it
    # modification
    if skip:
        return getPoint()
    #return np.power(10,resitev)
    if(math.isinf(resitev)):
        return getPoint()
    '''   
    if(math.isinf(resitev)):
        return 'False'
    
    if resitev>5 or resitev<np.log10(2/10000):
        return 'False'
    
    return resitev

all = np.linspace(2,10,20)
all = [i*2-2 for i in all]

for N in all:
#n = getPointNew()
#while not isinstance(n,(int,float)):
#    n = getPointNew()

    array=[getPoint(N)]
    startTime = time.time()
    while(1):
        for _ in range(0,1000):
            '''
            n = getPointNew()
            if isinstance(n,(int,float)):
                array.append(n)
            '''
            array.append(getPoint(N))
        if time.time()-startTime>120:
            break

    saveData(array,"Lavg/all"+str(N))
print('done')
    
    