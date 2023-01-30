# Translation to Python/Numpy of Sauer's
# Program 3.1 Newton Divided Difference Interpolation Method
# Computes coefficients of interpolating polynomial
# Input: x and y are vectors containing the x and y coordinates
#        of the n data points
# Output: coefficients c of interpolating polynomial in nested form
#

import matplotlib.pyplot as plt
import numpy as np

def newtdd(x,y):
	n = len(x)
	v = np.zeros((n,n))
	for j in range(n):
		v[j,0] = y[j]			# Fill in y column of Newton triangle

	for i in range(1,n):		# For column i,

		for j in range(n-i):	# 1:n+1-i		# fill in column from top to bottom

			v[j,i] = (v[j+1,i-1]-v[j,i-1])/(x[j+i]-x[j])
	c = v[0,:].copy()			# Read along top of triangle for output coefficients
	return c


def displaypoly(x,y):
        n = len(x)
        final=' '
        for i in range(n):
                maxVal = i
                final += str(y[i])
                for j in range(maxVal):
                    final += '(x-' + str(x[j]) + ')'
                if(i < n - 1):
                    final += ' + '
        print('Newton interpolating polynomial:\n',final)

def nest(c,x,b=[]):    #evaluates an interpolating polynomial in nested form
	d = len(c)-1
	if b==[]:
		b = np.zeros(d) 
	y = c[d]
	for i in range(d-1,-1,-1):
		y *= (x-b[i])
		y += c[i]
	return y


xdata = [1960,1970,1990,2000]
ydata = [3039585530.0,3707475887.0,5281653820.0,6079603571.0]

interpolant = newtdd(xdata,ydata)  #finds the coefficients

displaypoly(xdata,interpolant)     #displays Newton's interpolating polynomial

yvalue=nest(interpolant,1980,xdata)  #evaluates the polynomial for an input

print(f'\n y value at x={1980} is {yvalue:,}')
print(f"Difference is {yvalue:,} - {4452584592:,} = {(yvalue -4452584592):,}")
plt.plot(xdata,ydata,'ro')        #plots the interpolating polynomial

x = np.linspace(-1,4,100,endpoint=True)
y = nest(interpolant,x,xdata)

plt.plot(x,y,'b')
plt.show()
