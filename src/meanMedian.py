'''
Created on 10 Aug 2018

@author: benos
'''

def meanMedian(xaxis, yaxis):
    mean = 0
    summ = 0
    median = [0]*len(yaxis)
    sumNo = 0
    for p in range(1,len(yaxis)):
        #print(xaxis[p]," - ",yaxis[p])
        #mean += p*final[p]*(xaxis[p]-xaxis[p-1])
        summ += yaxis[p]*(xaxis[p]-xaxis[p-1])
        if yaxis[p-1]!=0 :
            median[sumNo]=xaxis[p-1]
            sumNo+=1
    half = summ/2
    tempSum = 0
    for p in range(1,len(yaxis)):
        tempSum+=yaxis[p]*(xaxis[p]-xaxis[p-1])
        if tempSum>half:
            mean = xaxis[p]
            break

    return (mean,median[int(sumNo/2)])


#(mean,median) = meanMedian([1,2,3,4,5,6,7],[0.1,0.2,0.4,0.8,1.6,3.2,6.4])
#print(mean)
#print(median)
