'''
Created on 13 Aug 2018

@author: benos
'''
import numpy as np

def createGraph1(xaxis,yaxis,start,end,size):
    
    graph = [0]*size
    newLocations = np.linspace(start,end,size)
    index = 0
    
    for i in range(0,len(xaxis)-1):
        #print(xaxis[i]," - ", newLocations[index]," - ",xaxis[i+1])
        while xaxis[i]<=newLocations[index] and newLocations[index]<xaxis[i+1]:
            y1 = yaxis[i]
            x1 = xaxis[i]
            y2 = yaxis[i+1]
            x2 = xaxis[i+1]
            k = (y2-y1)/(x2-x1)
            graph[index] = k*newLocations[index]+(y1-k*x1)
            index+=1
            if index >= len(newLocations)-1:
                return (newLocations[0:-1],graph[0:-1])
    return (newLocations[0:-1],graph[0:-1])

def createGraph(xaxis,yaxis,start,end,size):
    
    graph = [0]*size
    newLocations = np.linspace(start,end,size)
    index = 0
    
    for i in range(1,len(xaxis)-1):
        temp1 = xaxis[i]
        temp2 = newLocations[index]
        temp3 = newLocations[index+1]
        if(xaxis[i]<=newLocations[index+1] and xaxis[i]>newLocations[index]):
            graph[index]+=yaxis[i]
        else:
            index+=1
            if index+1==size:
                break            
            graph[index]+=yaxis[i]
    return (newLocations,graph)
            
            
            
    