import numpy as np
import mpmath as mp
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from IO import saveData,readData
from lifeDist import lifeDist, lifeDist2

def getPoint(N):
    RStarSample = random.uniform(0 , 2)
    fPlanets = random.uniform(-1 , 0)
    nEnvironment = random.uniform(-1 , 0)
    fInteligence = random.uniform(-3 , 0)
    fCivilization = random.uniform(-2 , 0)
    #L = random.uniform(2 , 10)
    
    fLife = lifeDist(vMin=-35, vMax=15, tMin=14, tMax=17, mean=0, sigma=200)
    fLifeEks = float(mp.log(fLife, 10))
    
    #resitev = random.choice(N)-(RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization)
    resitev = N-(RStarSample + fPlanets + nEnvironment + fLifeEks + fInteligence + fCivilization)

    if(math.isinf(resitev)):
        return getPoint(N)
    
    return resitev

#N = readData("laplace_cutoff_correction")
N = [1,2,3,4,5,6,7,8,10,100,1000,10000,100000]

for n in N:
    array=[]
    startTime = time.time()
    while(1):
        for _ in range(0,1000):
            array.append(getPoint(np.log(n)))
        if time.time()-startTime>2000:
            break
    
    saveData(array,"multL/Longevity"+str(n))


print('done')



