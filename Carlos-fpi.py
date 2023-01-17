
# Carlos Tapia
# fpi Method
# Usage: python3 Carlos-fpi.py 
# Input: Init guess x0, tolerance TOl, max steps N 
# Output: Approximate solution


import numpy as np 

def main():
    print("Starting\n")
    ###########
    print("\nProblem 1a")
    x0 = 1.0 
    tolerance = 0.5*10**(-8)
    fpi(g1,x0,tolerance,50)
    ###########
    print("\nProblem 1c")
    x0 = 0.5
    tolerance = 0.5*10**(-8)
    fpi(g2,x0,tolerance,50)
    ###########
    print("\nProblem 4c")
    x0 = 0.5
    tolerance = 0.5*10**(-8)
    fpi(g3,x0,tolerance,50)

    return

def fpi(g,x0, TOL, N):
    r=x0;
    i = 1;
    while i <= N: 
        r = g(x0)
        print(f"iteration: {i}; r = {r}")
        if abs(r-x0)<TOL:
            # Once it's within tolerance
            print("FPI Approx: %.8f\n iterations: %i"%(r,i))
            return r;
        # next iteartion increment
        i=i+1
        x0 = r
    print("MAX is; Failure")
    return

def g1(x):
	return (2*x+2)**(1/3)
def g2(x):
    return np.log(4-np.sin(x))
def g3(x):
    return (2*x+(5/(x**2)))/3




if __name__=="__main__":
    main()
