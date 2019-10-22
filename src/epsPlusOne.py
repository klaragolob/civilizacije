'''
Created on 22 Aug 2018

@author: benos
'''
from IO import readFile, save
import numpy as np
from logHistogramAdd import logHistogramAddMult
from mpSampleMultiple import scale

(xaxis, yaxis) = readFile("sigma is 50.csv")

size = len(yaxis)

start = 0
end = np.log(xaxis[-1])

dist = [0] * size

izpis = 0
lastIndex = 1
for i in range(0, size):
    if yaxis[i] == 0:
        continue
    (lastIndex, dist) = logHistogramAddMult(start, end, size, dist, xaxis[i] + 1, yaxis[i], lastIndex)
    if i % (size / 10) == 0:
        print(izpis, "%")
        izpis += 10
    
save(scale(start, end, size), dist, 'Sigma is 50 plus 1')

print('done')
