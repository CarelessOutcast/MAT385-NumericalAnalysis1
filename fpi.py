# Translation to Python of Sauer's
# Program 1.2 Fixed-Point Iteration
# Computes approximate solution of g(x)=x
# Input: inline function g, starting guess x0, tolerance TOL
#        max number of steps N
# Output: Approximate solution

def fpi(g,x0,TOL,N):
	r=x0; i=1
	while i<=N:
		r = g(x0)
		print("\n Iteration", i,":", r,)
		if abs(r-x0)<TOL:
			print("\n Fixed point approximation:",r)
			print("\n Number of iterations needed:",i)
			return r
		i=i+1;x0=r;
	print("\n The method failed after max iterations")
	return r


def g1(x): 
	return 1.0 - x**3.0
def g2(x): 
	return (1.0 - x)**(1.0/3.0)
def g3(x):
	return (2.0*x**3.0 + 1.0)/(3.0*x**2.0 + 1.0);

#fpi(g1,0.5,0.5*10**(-5),50);

fpi(g2,0.5,0.5*10**(-5),50);

#fpi(g3,0.5,0.5*10**(-5),50);

