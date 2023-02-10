# Program 3.5 Calculation of spline coefficients
# Calculates coefficients of cubic spline
# Input: x,y vectors of data points
#   plus two optional extra data v1, vn
# Output: matrix of coefficients b1,c1,d1;b2,c2,d2;...

import numpy as np
import matplotlib.pyplot as plt

def splinecoeff(xin,yin,option=1,v1=0,vn=0):
	x = np.array(xin,dtype=float)	# in case inputs are integer lists
	y = np.array(yin,dtype=float) 
	n = len(x); 
	A = np.zeros((n,n))			# matrix A is nxn
	r = np.zeros(n)
	dx = x[1:] - x[:-1]			# define the deltas
	dy = y[1:] - y[:-1]
	for i in range(1,n-1):			# load the A matrix
		A[i,i-1:i+2] = np.hstack( (dx[i-1], 2*(dx[i-1]+dx[i]), dx[i]) )
		r[i] = 3*(dy[i]/dx[i] - dy[i-1]/dx[i-1]) # right-hand side

# Set endpoint conditions
	if   option==1:					# natural spline conditions
		A[ 0, 0]  =  1.
		A[-1,-1]  =  1.
	elif option==2:					# curvature-adj conditions
		A[ 0, 0] = 2; r[ 0] = v1
		A[-1,-1] = 2; r[-1] = vn
	elif option==3:					# clamped
		A[ 0, :2] = [2*dx[  0],  dx[  0]]; r[ 0] = 3*(dy[  0]/dx[  0]-v1) 
		A[-1,-2:] = [  dx[n-2],2*dx[n-2]]; r[-1] = 3*(vn-dy[n-2]/dx[n-2])
	elif option==4:					# parabol-term conditions, for n> = 3
		A[ 0, :2] = [1,-1]
		A[-1,-2:] = [1,-1]
	elif option==5: 				# not-a-knot for n> = 4
		A[ 0, :3] = [dx[  1], -(dx[  0]+dx[  1]), dx[  0]]
		A[-1,-3:] = [dx[n-2], -(dx[n-3]+dx[n-2]), dx[n-3]]

	coeff = np.zeros((n,3))
	coeff[:,1] = np.linalg.solve(A,r)	# solve for c coefficients
	for i in range(n-1):			# solve for b and d
		coeff[i,2] = (coeff[i+1,1]-coeff[i,1])/(3.*dx[i])
		coeff[i,0] = dy[i]/dx[i]-dx[i]*(2.*coeff[i,1]+coeff[i+1,1])/3.
	coeff = coeff[0:n-1,:]
	print('Coefficients b,c,d:\n', coeff)
	return coeff



def splineplot(x,y,k,option=1,v1=0,vn=0):
	n = len(x)
	coeff = splinecoeff(x,y,option,v1,vn)
	x1 = np.empty((n-1)*k+1)
	y1 = np.empty((n-1)*k+1)
	for i in range(n-1):
		xs = np.linspace(x[i],x[i+1],k+1)
		dx = xs - x[i]
		ys = coeff[i,2]*dx	# evaluate using nested multiplication
		ys = (ys+coeff[i,1])*dx
		ys = (ys+coeff[i,0])*dx + y[i]
		#plot([x[i],x[i+1]],[y[i],y[i+1]],'o',xs,ys)
		plt.plot(xs,ys)
		x1[i*k:(i+1)*k] = xs[:-1]
		y1[i*k:(i+1)*k] = ys[:-1]
	x1[-1] = x[-1]; y1[-1] = y[-1]
	plt.plot(x,y,'o')#,x1,y1)

	return x1,y1

def special_splineplot(x,y,k,option=1,v1=0,vn=0):
	n = len(x)
	coeff = splinecoeff(x,y,option,v1,vn)
	x1 = np.empty((n-1)*k+1)
	y1 = np.empty((n-1)*k+1)

	for i in range(n-1):
		xs = np.linspace(x[i],x[i+1],k+1)
		dx = xs - x[i]
		ys = coeff[i,2]*dx
		ys = (ys+coeff[i,1])*dx
		ys = (ys+coeff[i,0])*dx + y[i]

		plt.plot(xs,ys)

		x1[i*k:(i+1)*k] = xs[:-1]
		y1[i*k:(i+1)*k] = ys[:-1]

	x1[-1] = x[-1]; y1[-1] = y[-1]
	plt.plot(x,y,'o')

	return x1,y1
#splineplot([1,2,4,7],[3,4,1,2],100)		    # natural spline conditions
#splineplot([1,2,4,7],[3,4,1,2],100,2,0.5,2)   # curvature-adj conditions
#splineplot( [1,2,4,7],[3,4,1,2],100,3,0,0)	    # clamped
#splineplot([1,2,4,7],[3,4,1,2],100,4)		    # parabol-term conditions, for n> = 3
#splineplot([1,2,4,7],[3,4,1,2],100,5)		    # not-a-knot for n> = 4

#1b
#splineplot([-1,0,3,4,5],[3,5,1,1,1],100,3,0,0) 

#5T
#splineplot([0,1,2,3,4],[1,3,3,4,2],100,3,0,4) 

#7T
#splineplot([0,1*np.pi/8,2*np.pi/8,3*np.pi/8,4*np.pi/8],[1,((2**(.5)+2)**(.5))/2,(2**(.5))/2,((2-(2**(.5)))**(.5))/2,0],100,3,0,0) 

#11T
special_splineplot([1960,1970,1990,2000],[3039585530,3707475887,5281653820,6079603571],100) 



plt.show()






