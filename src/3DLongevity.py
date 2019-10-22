from IO import  readData
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import scipy.ndimage.filters as fl
from StandardizeDistribution import StandardizeDistributionW
size= 20


no = np.linspace(2,10,20)

no = [i*2-2 for i in no]
arrayL = [None]*size
Z = [None]*size

bins = np.linspace(-13,20,21)

for i in range(0,size):
    #arrayL[i] = [10**a for a in readData("Laplace/L"+str(no[i]))]
    arrayL[i] = readData("Lavg/all"+str(no[i]))
    Z[i],_ = np.histogram(arrayL[i], bins)
    
no = np.linspace(2,10,20)
X, Y = np.meshgrid(bins[0:-1],no)
   
     
print("x:",np.shape(X)," y:",np.shape(Y)," z:",np.shape(Z))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

#print(X,"\n")
#print(Y,"\n")
'''
x1=31
print("X:",X[0][x1])
xaxis = [Y[i][x1] for i in range(0,20)]
yaxis=[0]*20
for p in range(0,20):
    print(Z[p][x1])
    yaxis[p]=Z[p][x1]
    
yaxis = fl.gaussian_filter(yaxis, 1)
(length, xaxis1, yaxis, cdf,cdfW ) = StandardizeDistributionW(xaxis,yaxis)

plt.plot(xaxis,cdf,'red', label = 'CDF')
'''
#plt.plot(xaxis,cdfW,'green')
#plt.title('5 parameters')


#plt.yscale("log")
#plt.ylim(0,0.0200)

#plt.xscale("log")
'''
plt.plot(xaxis, yaxis,'blue',label='PDF')
s="N="+str(10**X[0][x1])
plt.title(s)
plt.ylabel("relative frequency")
plt.xlabel("log(maxL)")
'''
#plt.figure(1)

# Plot the surface
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,shade=True,color='b',alpha=0.8)

ax.set_xlabel("log(N)")
ax.set_ylabel("log(maxL)")
#plt.xscale("log")
plt.show()

