import openturns as ot
import numpy as np
import matplotlib.pyplot as plt
import math


distribution = ot.LogUniform(-1.0, 1.0)
sample = distribution.getSample(5)

#print(distribution.drawLogPDF(-1.0, 1.0, 10000 ))

Graph.viewer.View(distribution.drawLogPDF(-1.0, 1.0, 10000 ))


"""
plt.xscale("log")
plt.plot(distribution)
plt.show()
"""