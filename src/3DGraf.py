from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from ExponentsAlternative import getDistributionOfEks, getDistributionOfEksKnownFL, getNEksponentSampleKnownFl

#input:
startFLife = -100
stopFLife = 0
sizeFlife = 100

startXOs = -40
stopXOs = 15
sizeXOs = 50

startFInteligence = -3
stopFInteligence = 0
sizeFInteligence = 20

startFCivilization = -2
stopFCivilization = 0
sizeFCivilization = 20



#fLife = np.linspace( startFLife, stopFLife , sizeFlife )
fLife = np.linspace(  startFLife, stopFLife, sizeFlife )
fCivilization = np.linspace(  startFCivilization, stopFCivilization, sizeFCivilization )
fIntelligence = np.linspace(  startFInteligence , stopFInteligence , sizeFInteligence )
#fLife = np.flip(fLife)
xOs = np.linspace( startXOs , stopXOs , sizeXOs )

pdfARRAY = []

for value in fCivilization:
    print(value)
    #pdf = getDistributionOfEksKnownFL(size=10000, pdfSize=sizeXOs, low=startXOs, high=stopXOs, flEks = value)[1]
    pdf = getDistributionOfEks(size=1000, pdfSize=sizeXOs, low=startXOs, high=stopXOs, knownFC = value)[1]
    pdfARRAY.append(pdf)

#print(pdfARRAY)
fig = plt.figure()
ax = fig.gca(projection='3d')


xOs, f = np.meshgrid( xOs, fCivilization)

X = xOs
Y = f
#Z = pdfARRAY
Z= np.array(pdfARRAY)
print(X,"\n")
print(Y,"\n")
print(Z)
     
#print(xOs)


print("x:",np.shape(xOs)," y:",np.shape(fLife)," z:",np.shape(Z))
# Plot the surface.
surf = ax.plot_surface( X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=False)

# Customize the z axis.
#ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

#ax = fig.add_subplot(111, projection='3d')

# Plot the surface
#ax.plot_surface(X, Y, Z, color='b')
#plt.xscale("log")

ax.set_xlabel("log(N)")
ax.set_ylabel("log(FC)")
plt.gca().invert_yaxis()


plt.show()