import numpy as np
import mpmath as mp
import random
from mpl_toolkits.mplot3d import Axes3D
import math
from lifeDist import lifeDist, lifeDist2
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from IO import save
from ToyModel import getCDFNIC, normalizePDF
import mpmath as mp
import pylab as p
from ExponentsAlternative import getDistributionOfEks

def getN(Rs=10,Fp=0.3,Ne=0.3,Fl=0.5,Fi=0.03,Fc=0.1,L=10**6):
    return Rs*Fp*Ne*Fl*Fi*Fc*L



size=100
Fl = np.linspace(-150,0,size)
Fc = np.linspace(-3,0,size)

X=10**Fl
Y=10**Fc
N = getN(Fl=1,Fc=1)

X, Y = np.meshgrid(X, Y)

Z=X*Y*N



fig = plt.figure()

ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel("Fl")
ax.set_ylabel("Fc")

ax.plot_surface(X, Y, Z, color='b')

plt.show()