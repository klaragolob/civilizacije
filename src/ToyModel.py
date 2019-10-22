import numpy as np
import mpmath as mp
import random
from mpmath import mpmathify
import matplotlib.pyplot as plt
from mpLogspace import mpLogspace
import scipy.ndimage.filters as fl
from IO import save


def getStandardTuple(size=100000, pdfSize=10001, low=0 , high=0.2, lowerThan=1, stParametrov=3, start=-5, stop=5, hundredBillions=100000):  # WARNING: PDFSIZE MUST BE 101, 1001, OR 10001, ETC. 
    pdf = [0] * pdfSize
    arrayOfParameters = []
    stevecManjsihOd1 = 0
    x = np.logspace(start, stop , pdfSize)
    
    desetNaStDecimalk = ((pdfSize - 1) / (stop - start))  # =1000
    polOdArraya = start * desetNaStDecimalk  # =5000
    
    for j in range(0, size):
        
        parameters = 1
        for i in range(0, stParametrov):
            r = random.uniform(low, high)
            parameters *= r
            
        parameters = parameters * (hundredBillions)  
        stevecManjsihOd1 += (parameters < lowerThan)
        arrayOfParameters.append(parameters)
        
        indeksPDF = int(round(np.log10(parameters) * desetNaStDecimalk - polOdArraya))
        if indeksPDF < 0:
            indeksPDF = 1
        elif indeksPDF >= pdfSize:
            indeksPDF = pdfSize - 1
        pdf[indeksPDF] += 1
    
    alonePossibility = stevecManjsihOd1 / size

    cdfNIC = getCDFNIC(pdf)
    cdfPLOSCINA = getCDFPLOSCINA(x, pdf)
    pdf = normalizePDF(pdf)
    pdf = fl.gaussian_filter(pdf, 100)
    pdf = normalizePDF(pdf)

    return (arrayOfParameters, alonePossibility, x, pdf, cdfNIC, cdfPLOSCINA, desetNaStDecimalk, polOdArraya)


def getStandardTupleNATURALSCALE(size=100000, pdfSize=10001, low=0 , high=0.2, lowerThan=1, stParametrov=3, start=0, stop=100, hundredBillions=100000):  # WARNING: PDFSIZE MUST BE 101, 1001, OR 10001, ETC. 
    pdf = [0] * pdfSize
    arrayOfParameters = []
    stevecManjsihOd1 = 0
    x = np.linspace(start, stop , pdfSize)
    
    desetNaStDecimalk = ((pdfSize - 1) / (stop - start))  # =1000
    polOdArraya = start * desetNaStDecimalk  # =5000
    
    for j in range(0, size):
        
        parameters = 1
        for i in range(0, stParametrov):
            r = random.uniform(low, high)
            parameters *= r
            
        parameters = parameters * (hundredBillions)  
        stevecManjsihOd1 += (parameters < lowerThan)
        arrayOfParameters.append(parameters)
        
        indeksPDF = int(round(parameters * desetNaStDecimalk - polOdArraya))
        if indeksPDF < 0:
            indeksPDF = 1
        elif indeksPDF >= pdfSize:
            indeksPDF = pdfSize - 1
        pdf[indeksPDF] += 1
    
    alonePossibility = stevecManjsihOd1 / size

    cdfNIC = getCDFNIC(pdf)
    cdfPLOSCINA = getCDFPLOSCINA(x, pdf)
    pdf = normalizePDF(pdf)
    pdf = fl.gaussian_filter(pdf, 100)
    pdf = normalizePDF(pdf)

    return (arrayOfParameters, alonePossibility, x, pdf, cdfNIC, cdfPLOSCINA, desetNaStDecimalk, polOdArraya)


def getStandardTupleLOGUNIFORM(size=100000, pdfSize=10001, low=0.001 , high=0.2, lowerThan=1, stParametrov=9, start=-15, stop=5, hundredBillions=100000000000):  # WARNING: PDFSIZE MUST BE 101, 1001, OR 10001, ETC. 
    pdf = [0] * pdfSize
    arrayOfParameters = []
    stevecManjsihOd1 = 0
    x = np.logspace(start, stop , pdfSize)
    
    desetNaStDecimalk = ((pdfSize - 1) / (stop - start))  # =1000
    polOdArraya = start * desetNaStDecimalk  # =5000
    
    logLow = np.log(low)
    logHigh = np.log(high)
    
    for j in range(0, size):
        
        parameters = 1
        for i in range(0, stParametrov):
            r = random.uniform(logLow, logHigh)
            parameters *= np.exp(r)
            
        parameters = parameters * (hundredBillions)  
        stevecManjsihOd1 += (parameters < lowerThan)
        arrayOfParameters.append(parameters)
        
        indeksPDF = int(round(np.log10(parameters) * desetNaStDecimalk - polOdArraya))
        if indeksPDF < 0:
            indeksPDF = 1
        elif indeksPDF >= pdfSize:
            indeksPDF = pdfSize - 1
        pdf[indeksPDF] += 1
    
    alonePossibility = stevecManjsihOd1 / size

    cdfNIC = getCDFNIC(pdf)
    cdfPLOSCINA = getCDFPLOSCINA(x, pdf)
    pdf = normalizePDF(pdf)
    pdf = fl.gaussian_filter(pdf, 100)
    pdf = normalizePDF(pdf)

    return (arrayOfParameters, alonePossibility, x, pdf, cdfNIC, cdfPLOSCINA, desetNaStDecimalk, polOdArraya)


def getIndexMaxPDF(pdf):
    length = len(pdf)
    maxPDF = 0
    index = 0
    for i in range(0, length):
        if (pdf[i] > maxPDF):
            maxPDF = pdf[i]
            index = i
    return i


def getMaxPDF(pdf):
    maxPDF = 0
    for value in pdf:
        if value > maxPDF:
            maxPDF = value
    return maxPDF 


def getCDFNIC(pdf):
    cdfNIC = []
    sumCDFNIC = 0
    sumPDF = sum(pdf)
    
    for value in pdf:
        sumCDFNIC += value / sumPDF
        cdfNIC.append(sumCDFNIC)
    
    return cdfNIC


def getCDFPLOSCINA(x, pdf):
    cdfPLOSCINA = [0.0]
    sumCDFPLOSCINA = 0
    length = len(pdf)
    
    for i in range(1, length):
        sumCDFPLOSCINA += (x[i] - x[i - 1]) * pdf[i]
        cdfPLOSCINA.append(sumCDFPLOSCINA)
    
    cdfMAX = cdfPLOSCINA[ length - 1 ]
    for i in range(0, length):
        cdfPLOSCINA[i] = cdfPLOSCINA[i] / cdfMAX
    
    return cdfPLOSCINA


def normalizePDF(pdf):
    maxPDF = getMaxPDF(pdf)
    length = len(pdf)
    for i in range(0, length):
        pdf[i] = pdf[i] / maxPDF
    return pdf


def normalizePDFs(pdf, pdf2):
    maxPDF = getMaxPDF(pdf)
    maxPDF2 = getMaxPDF(pdf2)
    #maxPDF2 = 
    length = len(pdf)
    for i in range(0, length):
        pdf[i] = pdf[i] / maxPDF
        pdf2[i] = pdf2[i] / maxPDF
    return (pdf,pdf2)


def fromEpsilonGetLowHigh(epsilon=0, option=1, low=0.0, high=0.2):
    if option == 1:
        low, high = 0, 0.2

    elif option == 2:
        low, high = epsilon, 0.2
        
    elif option == 3:
        low, high = 0.1 - epsilon , 0.1 + epsilon
        
    elif option == 4:
        low, high = epsilon, 0.2 + epsilon
        
    else:
        print("this option is not allowed.")
        
    return (low, high)


def getAlonePossibility(low=0, high=0.2, size=100000, lowerThan=1, stParametrov=9):
    stevecManjsihOd1 = 0
    hundredBillions = int(10 ** (2 + stParametrov))
    
    for j in range(0, size):
        
        parameters = 1
        for i in range(0, stParametrov):
            r = random.uniform(low, high)
            parameters *= r
            
        parameters = parameters * hundredBillions
        stevecManjsihOd1 += (parameters < lowerThan)
    
    alonePossibility = stevecManjsihOd1 / size
    return alonePossibility


def getAlonePossibilityLOGUNIFORM(low=0.001, high=0.2, size=10000, lowerThan=1, stParametrov=9):
    stevecManjsihOd1 = 0
    hundredBillions = int(10 ** (2 + stParametrov))
    
    logLow = np.log(low)
    logHigh = np.log(high)
    
    for j in range(0, size):
        
        parameters = 1
        for i in range(0, stParametrov):
            r = random.uniform(logLow , logHigh)
            parameters *= np.exp(r)
            
        parameters = parameters * hundredBillions
        stevecManjsihOd1 += (parameters < lowerThan)
    
    alonePossibility = stevecManjsihOd1 / size
    return alonePossibility

