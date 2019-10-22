from ToyModel import getAlonePossibility, getAlonePossibilityLOGUNIFORM 
import numpy as np
import matplotlib.pyplot as plt


#DEL PROGRAMA KI JE ZA ODVISNOST OD PARAMETROV! :
stParMAX = 9

x = np.linspace(1, stParMAX , stParMAX )

y1 = []
for stPar in range( 1, stParMAX + 1 ):
    vrednost = getAlonePossibility(low=0, high=0.2, size=100000, lowerThan=1, stParametrov=stPar )
    y1.append(vrednost)
    print("stParametrov="+ str(stPar) + " : "+ str(vrednost))
'''
y2 = []
for stPar in range( 1, stParMAX + 1 ):
    vrednost = getAlonePossibilityLOGUNIFORM(low=0.001, high=10, size=1000, lowerThan=1, stParametrov=stPar )
    y2.append(vrednost)
    print("stParametrov="+ str(stPar) + " : "+ str(vrednost))
    
y3 = []
for stPar in range( 1, stParMAX + 1 ):
    vrednost = getAlonePossibilityLOGUNIFORM(low=0.0001, high=100, size=1000, lowerThan=1, stParametrov=stPar )
    y3.append(vrednost)
    print("stParametrov="+ str(stPar) + " : "+ str(vrednost))

y4 = []
for stPar in range( 1, stParMAX + 1 ):
    vrednost = getAlonePossibilityLOGUNIFORM(low=0.00001, high=1000, size=1000, lowerThan=1, stParametrov=stPar )
    y4.append(vrednost)
    print("stParametrov="+ str(stPar) + " : "+ str(vrednost))
'''
#plt.title('Probability of there being no civilizations depending on the number of parameters (1-9)')
plt.ylabel('Probability of being alone')
plt.xlabel('number of parameters')
x = [ u'1', u'2', u'3', u'4', u'5', u'6', u'7', u'8' , u'9' ]
z = plt.bar( x, height= y1 )


#plt.plot(x, y1, 'brown' , label = 'range(0.01 , 1)')

'''
plt.plot(x, y2, 'red' , label = 'range(0.001 , 10 )')
plt.plot(x, y3, 'orange' , label = 'range(0.0001 , 100 )')
plt.plot(x, y4, 'yellow' , label = 'range(0.00001 , 1000 )')
'''
#plt.legend( loc=4 )
plt.show()

#HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
'''
#DEL PROGRAMA KI JE ZA ODVISNOST OD PARAMETROV! -LOGSCALE :
stParMAX = 20
x = np.linspace(1, stParMAX , stParMAX )

y1 = []
for stPar in range( 1, stParMAX + 1 ):
    vrednost = getAlonePossibilityLOGUNIFORM(low=0.000000001, high=0.2, size=10000, lowerThan=1, stParametrov=stPar )
    y1.append(vrednost)
    print("stParametrov="+ str(stPar) + " : "+ str(vrednost))

y2 = []
for stPar in range( 1, stParMAX + 1 ):
    vrednost = getAlonePossibilityLOGUNIFORM(low=0.01, high=0.19, size=10000, lowerThan=1, stParametrov=stPar )
    y2.append(vrednost)
    print("stParametrov="+ str(stPar) + " : "+ str(vrednost))
    
y3 = []
for stPar in range( 1, stParMAX + 1 ):
    vrednost = getAlonePossibilityLOGUNIFORM(low=0.02, high=0.18, size=10000, lowerThan=1, stParametrov=stPar )
    y3.append(vrednost)
    print("stParametrov="+ str(stPar) + " : "+ str(vrednost))

plt.title('Probability of there being no civilizations depending on the number of parameters (1-20)')
plt.ylabel('Probability of there being no civilizations')
plt.xlabel('number of parameters')
plt.plot(x, y1, 'brown' , label = 'range(0.00 , 0.2)')
plt.plot(x, y2, 'red' , label = 'range(0.01 , 0.19)')
plt.plot(x, y3, 'orange' , label = 'range(0.02 , 0.18)')
plt.legend( loc=4 )
plt.show()
'''



