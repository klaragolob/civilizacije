'''
Created on 7 Aug 2018

@author: benos
'''
import random
import numpy as np
import matplotlib.pyplot as plt
from mpmath import mpmathify,mp,mpf
from logHistogramAdd import logHistogramAdd


def lifeDist(vMin=-35,vMax=15,tMin=14,tMax=17,mean=0, sigma=14):
    V = (mpmathify(10 ** (vMin)), mpmathify(10 ** (vMax)))
    t = (mpmathify(10 ** (tMin)), mpmathify(10 ** (tMax)))
    
    mp.dps = 230
    
    val = mpf('1')
    r = np.random.lognormal(mean,sigma)
    #r = np.random.normal(mean,sigma)
    val *= r
    val *= sampleU(V)
    val *= sampleU(t)
    val = 0-val
    expo = mp.exp(val)        
    val = mpf('1') - expo
    mp.dps = 15
    return val

def sample(dist):
    r = random.uniform(mp.log(dist[0]), mp.log(dist[1]))
    return mp.exp(r)

def sampleU(dist):
    return random.uniform(dist[0], dist[1])


def lifeDist2(vMin=-35,vMax=15,tMin=14,tMax=17,lambMin = -188 , lambMax = 15 ):
    V = (mpmathify(10 ** (vMin)), mpmathify(10 ** (vMax)))
    t = (mpmathify(10 ** (tMin)), mpmathify(10 ** (tMax)))
    lamb = (mpmathify(10 ** ( lambMin )), mpmathify(10 ** lambMax))
    mp.dps = 230
    
    val = mpf('1')
    val *= sample( lamb )
    val *= sample(V)
    val *= sample(t)
    val = 0-val
    expo = mp.exp(val)        
    val = mpf('1') - expo
    mp.dps = 15
    return val
