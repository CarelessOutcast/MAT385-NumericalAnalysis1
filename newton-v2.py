
# Newton's method
# Computes approximate solution of f(x)=0
# Input: starting guess x0, tolerance TOL, max number of steps N
# Output: Approximate solution
#
# We use the derivative command from scipy.misc to avoid calculating it by hand

from  scipy.misc import derivative
import numpy as np

def newton(x0,TOL,N):
	i=1
	while i<=N:
		if derivative(f,x0,10**(-5))==0.0:
			print("\n Division by 0. Method failed")
			return
		r = x0-f(x0)/derivative(f,x0,10**(-5))
		print("\n Iteration", i,":", r)
		if abs(r-x0)<TOL:
			print("\n Newton's approximation:",r)
			print("\n Number of iterations needed:",i)
			return r
		i=i+1;x0=r;
	print("\n The method failed after max iterations")
	return


def f(x): 
	return x**3+x**2-1;

newton(1.0,0.5*10**(-5),50)
