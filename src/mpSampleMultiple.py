'''
Created on 8 Aug 2018

@author: benos
'''
import random
from mpmath import mpf,mp
from mpLogspace import mpLogspace
from logHistogramAdd import logHistogramAdd
import time
from lifeDist import lifeDist
from StandardizeDistribution import StandardizeDistribution

def mpSampleMultiple(parameters, minExp, maxExp, size, times,life):
    dist = [0] * size
    izpis = 0
    for t in range(0, times):
        sampleMultiple(parameters, minExp, maxExp, size, dist,life)
        if t % (times / 10) == 0:
            print(izpis, "%")
            izpis += 10
    return (scale(minExp, maxExp, size), dist)


def mpSampleMultipleTime(parameters, minExp, maxExp, size, timeLimit,life):
    dist = [0] * size
    timeStart = time.time()
    while True:
        sampleMultiple(parameters, minExp, maxExp, size, dist,life)
        if time.time() - timeStart > timeLimit:
            break  
    return (scale(minExp, maxExp, size), dist)

def sampleMultiple(parameters, minExp, maxExp, size,dist,life):
    val = mpf('1.0')
    for p in parameters:
        newVal = sampleU(p)
        val *= newVal
    if(life[0]):
        newVal = lifeDist(life[1],life[2],life[3],life[4],life[5],life[6])
        val *= newVal
    dist = logHistogramAdd(minExp, maxExp, size, dist, val)
    return dist

def sampleL(parameters,minExp,maxExp,size,timeLimit,life,N):
    dist = [0] * size
    timeStart = time.time()
    while True:
        val = mpf('1.0')
        for p in parameters:
            newVal = sample(p)
            val *= newVal
        if(life[0]):
            val *= lifeDist(life[1],life[2],life[3],life[4],life[5],life[6])
        val = 1/val
        if(N[0]):
            val *= sampleByBisection(StandardizeDistribution(N[1][0],N[1][1]))
        dist = logHistogramAdd(minExp, maxExp, size, dist, val)
        if time.time() - timeStart > timeLimit:
                break  
    return (scale(minExp, maxExp, size), dist)

def sample(dist):
    r = random.uniform(mp.log(dist[0]), mp.log(dist[1]))
    return mp.exp(r)

def sampleU(dist):
    return random.uniform(dist[0], dist[1])


def normalize(xaxis, dist):
    surface = mpf('0')
    for i in range(1, len(xaxis) - 1):
        surface += (xaxis[i] - xaxis[i - 1]) * dist[i]
    print("\n\nSURFACE", surface)
    newDist = [i / surface for i in dist]
    return (xaxis, newDist)
    
        
def scale(minExp, maxExp, size):
    scale = [0] * size
    step = (maxExp - minExp) / size
    start = minExp
    for i in range(1, size):
        scale[i] = 10 ** (start + step * i)
    return scale

'''
def add(dist,size, value):
    step = mpf(55/size)
    start = mpf('-40')
    for i in range(1,size):
        current = 10**(start+step*i)
        if value<current:
            dist[i-1]+=1
            return dist
'''

'''
def sample(distribution):
    rand = random.random()
    length = distribution[0]
    #lin = mpLogspace(distribution[0], distribution[1], length)
    cumulSum = mpf('0')
    for i in range(0,length-1):
        cumulSum += distribution[2][i]
        if cumulSum > rand:
            return distribution[1][i]
    return distribution[2][-1]
'''


def getSurface(distribution):  # "Ce bo kdo rabu" - Jurij
    length = len(distribution[2])                                       
    logXarray = mpLogspace(distribution[0], distribution[1], length)    
    
    surface = mpf('0')
    for i in range(1, length - 1):
        surface += (logXarray[i] - logXarray[i - 1]) * distribution[2][i]
    
    return surface
    

def sampleByBisection(stdDistribution):
    randFloat = random.random()

    a = 0
    b = stdDistribution[0] - 1  # length - 1
    c = int(round((a + b) / 2))  # rounding to the next int.
    while (b != a):
        if (stdDistribution[3][c] <= randFloat and stdDistribution[3][c + 1] > randFloat):
            return stdDistribution[1][c]
        elif stdDistribution[3][c] <= randFloat :
            a = c
        else :
            b = c
        c = int(round((a + b) / 2))
        
    return stdDistribution[1][b]


def sampleUniform(dist):
    return dist[1][random.randint(0, dist[0] - 1)]
    
    
