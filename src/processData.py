import numpy as np
import mpmath as mp
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
import time
from IO import saveData,readData,save
from lifeDist import lifeDist, lifeDist2
from logHistogramAdd import logHistogramAddMult
from mpLogspace import mpLogspace

data = readData("laplace_cutoff_correction")

siz = len(data)

formatted = [0] * siz


sortedData = np.sort(data)

saveData(sortedData, "laplace_cutoff_correction_sorted")

lastIndex = 0

dist = [0]*siz
start = -40
end = 15
size = siz

for value in sortedData:
    (lastIndex,dist) = logHistogramAddMult(start, end, size, dist, value, 1, lastIndex)
    
xaxis = mpLogspace(10**-40,10**15,siz)

save(xaxis,dist,"laplace_cutoff_correction_sorted")

print("done")







