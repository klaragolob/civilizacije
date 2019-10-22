'''
Created on 28 Aug 2018

@author: benos
'''

def createHistogram(elements,bins):
    
    size = len(bins)
    yaxis = [0]*size
    for e in elements:
        for i in range(0,size):
            if e == bins[i]:
                yaxis[i]+=1
    
    return (bins,yaxis)
        
        
        
    