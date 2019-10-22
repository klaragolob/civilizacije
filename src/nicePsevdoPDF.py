import mpmath as mp
from mpmath import mpmathify

def getPDFNice( xOs , pdf ):
    pdfNice = []
    length = len(pdf)
    sum = mpmathify(0)
    for i in range(0, length ):
        sum+=  pdf[i] * xOs[i]
        pdfNice.append( sum )
    
    for i in range(0, length ):
        pdfNice[i] = pdfNice[i] / sum
    
    return pdfNice
