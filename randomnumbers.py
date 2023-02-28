## Numerical Analysis - Random Numbers and Monte Carlo

import numpy as np
import matplotlib.pyplot as plt


#define linear congruential generator

def LCG(m,a,b,x0,N):
    seq=[]
    for i in range(N):
        x = (a * x0 + b) % m
        seq.append(float(x))
        x0 = x
    return (seq)




def f(x):
    return(x**2-x+0.5)

def g(x):
    return(-x**2+x+0.5)


#plot of the functions
x = np.linspace(-0.5,1.5,100)
y1 = f(x)
y2 = g(x)
plt.plot(x,y1)
plt.plot(x,y2)
plt.show()


# We use  Monte Carlo Type I simulation: 
# area equals the average of "g-f" over [0,1] x the size of the interval 

xvalues = np.array(LCG(2**31-1,7**5,0,3,10000))/(2**31-1)

yvalues = g(xvalues)-f(xvalues)

mc1 = sum(yvalues) / len(yvalues) 

print('\nMonte Carto (type I) estimate:',mc1)

# We use  Monte Carlo Type II simulation: 
# count how many land inside the region of interest 

count = 0
for i in range(len(xvalues)-1):
    if xvalues[i+1] >= f(xvalues[i]) and xvalues[i+1] <= g(xvalues[i]):
        count = count + 1

area = 1
mc2 = count/(len(xvalues)-1) * area

print('\nMonte Carto (type II) estimate:',mc2)



#Volume of the unit sphere

print('\nVolume of unit sphere:\n')

# We use now a Monte Carlo Type II simulation to find the volume of the unit sphere: 
#                        
#                       x^2  + y^2  + z^2  <= 1
#
#We enclose the unit sphere in the cube [-1,1]x[-1,1]x[-1,1], sample random points from this unit cube and count how many land inside the spherxval

xvaluesn = 2*xvalues - 1  #we generate points in [-1,1] from the original set in [0,1]
count3d = 0
for i in range(len(xvaluesn)-2):
    x=xvaluesn[i]; y=xvaluesn[i+1]; z=xvaluesn[i+2];
    if x**2 + y**2 + z**2 <= 1:
        count3d = count3d + 1

vol = 8
mc2 = count3d/(len(xvaluesn)-2) * vol

print('Monte Carto (type II) estimate:',mc2)


