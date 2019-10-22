import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage.filters as fl
from IO import readFile, readData,save
from ToyModel import getCDFNIC, normalizePDF, normalizePDFs
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from logHistogramAdd import logHistogramAdd

def normalize1(pdf):
    summ = sum(pdf)
    for a in range(0, len(pdf)):
        pdf[a] /= summ
    return pdf


(xaxis, yaxisL) = readFile("What is L with N sig50")
#(_,yaxisLcdf) = readFile("cdf-sigma-200")

(xaxis, yaxisU) = readFile("L with laplace")
#(_,yaxisUcdf) = readFile("L with laplace cdf")
'''
dat = readData("laplace_cutoff_correction")
yaxisU = [0]*2151
for value in dat:
    yaxisU = logHistogramAdd(-40, 15, 2151, yaxisU, value)    
save(xaxis,yaxisU,"laplace_cutoff_correction")

print("done")
'''
#cdf = getCDFNIC(yaxisU)
yaxisU[0] = yaxisU[1]


yaxisL = normalize1(yaxisL)
yaxisU = normalize1(yaxisU)

yaxisL = fl.gaussian_filter(yaxisL, 5)
yaxisU = fl.gaussian_filter(yaxisU, 20)

yaxisU,yaxisL = normalizePDFs(yaxisU,yaxisL)
#yaxisL,yaxisU = normalizePDFs(yaxisL,yaxisU)

plt.figure(2)
plt.plot(xaxis, yaxisU, 'blue',label="L with Laplace correction")
plt.xscale("log")
plt.plot(xaxis, yaxisL, 'red',label="L with Sandberg")
plt.xlabel("L")
plt.ylabel("relative frequency")

#plt.plot(xaxis,yaxisLcdf,"orange",linestyle='--',label="CDF Sandberg")
#plt.plot(xaxis,yaxisUcdf,"c",linestyle='--',label="CDF Laplace")




plt.legend( loc=2 )
plt.show()

transition = np.linspace(0, 1, 200)
revTransition = np.flip(transition)

X = np.log(xaxis)
Y = transition

#X = np.linspace(1,10,10)
#yaxisL=[0,0.5,0.6,0.7,0.8,0.9,1,1,1,1]
#yaxisU=[1,1,1,1,0.9,0.8,0.5,0.4,0.3,0.2]

X, Y = np.meshgrid(X, transition)

x1,y1= np.meshgrid(yaxisL,transition)
x2,y2=np.meshgrid(yaxisU,revTransition)

x1 *=y1 
x2 *=y2
Z=x1+x2

#Z = [[0] * len(yaxisL)] * len(transition)
#for i in range(0, len(transition)):
#    for j in range(0, len(yaxisL)):
#        Z[i][j] = yaxisL[j] * transition[i] + yaxisU[j] * (1 - transition[i])
print(x1)
print(x2,"\n")

print(X,"\n")
print(Y,"\n")
print(Z)   
     
     
print("x:",np.shape(X)," y:",np.shape(Y)," z:",np.shape(Z))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, ccount=100,rcount=100,shade=True,color='b',alpha=1)

ax.set_xlabel("log(L)")
ax.set_ylabel("laplace <-> sandberg")

#plt.xscale("log")
plt.show()

