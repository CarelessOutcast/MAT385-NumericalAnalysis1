
# Carlos Tapia
# Newtons Method
# Usage: python3 Carlos-Netwons.py 
# Input: Init guess x0, tolerance TOl, max steps N 
# Output: Approximate solution

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 

import numpy as np
from scipy.misc import derivative 

def main():
    ###########
    print("\nProblem 1a")
    x0 = 1.0
    p = 10**(-8)
    tolerance = 0.5*10**(-8)
    answerA=newton(g1,p,x0,tolerance,50)
    ###########
    print("\nProblem 1c")
    x0 = 1.0
    p = 10**(-8)
    tolerance = 0.5*10**(-8)
    answerC=newton(g2,p,x0,tolerance,50)
    ###########
    print("\nProblem 6")
    x0 = 1.0
    p = 10**(-5)
    tolerance = 0.5*10**(-4)
    answer6=newton(g3,p,x0,tolerance,50)
    ###########
    print("\nProblem 7")
    x0 = 2.0
    p = 10**(-5)
    tolerance = 0.5*10**(-6)
    answer7a=newton(g4,p,x0,tolerance,50)

    x0 = -2.0
    p = 10**(-5)
    tolerance = 0.5*10**(-6)
    answer7b=newton(g4,p,x0,tolerance,50)

    x0 = 0.3
    p = 10**(-5)
    tolerance = 0.5*10**(-6)
    answer7c=newton(g4,p,x0,tolerance,50)

    fprime = derivative(g4,answer7a,10**(-5))
    fprime2 = derivative(g4,answer7b,10**(-5))
    print()
    
    print("f1(x) @2.0 = %.8f"%(g4(answer7a)),end="; ")
    print("fprime1(x) @2.0 = %.8f"%(fprime))

    print("f1(x) @-2.0 = %.8f"%(g4(answer7b)),end="; ")
    print("fprime1(x) @-2.0 = %.8f"%(fprime2))

    print("f1(x) @0.3 = %.8f"%(g4(answer7c)),end="; ")
    print("fprime1(x) @0.3 = %.8f"%(derivative(g4,answer7c,10**(-5))),end="; ")
    print("f(prime^2)1(x) @0.3 = %.8f"%(derivative(g4,answer7c,10**(-5), n=2)),end="; ")
    
    print("\n")
    print(f"Hence, f is quadratically convergent to {answer7a:.8f} and {answer7b:.8f}; Linearly convergent to {answer7c:.2f} with a ratio of {3/4}")

    return

def newton(g,p,x0, TOL, N):
    i = 1;
    while i <= N: 
        if derivative(g,x0,p)==0.0:
            print("Div by 0: Error")
            return
        r = x0 - g(x0)/derivative(g,x0,p)
        print(f"iteration: {i}; r = {r}")
        if abs(r-x0)<TOL:
            # Once it's within tolerance
            print("FPI Approx: %.8f\n iterations: %i"%(r,i))
            return r;
        # next iteartion increment
        i=i+1
        x0=r
    print("MAX; Failure")
    return
#1a
def g1(x):
	return x**3 - 2*x - 2
#1c
def g2(x):
    return np.exp(x) + np.sin(x) - 4
#6all
def g3(x):
    return (2*np.pi*x**2*(x+5))-180
#7all
def g4(x):
    return np.exp(np.sin(x)**3)+x**6-2*x**4-x**3-1




if __name__=="__main__":
    main()
