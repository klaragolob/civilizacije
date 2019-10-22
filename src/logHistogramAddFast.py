'''
Created on 20 Aug 2018

@author: benos
'''



def logHistogramAddFast(start, end, size, dist, value):
    start = start
    end = end
    step = (end - start) / size
    for i in range(1, size):
        current = 10 ** (start + step * i)
        if value < current:
            dist[i - 1] += 1
            return dist
    dist[-1] += 1
    return dist