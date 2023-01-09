# Program 1.1 Bisection Method
# Computes approximate solution of f(x)=0
# Input: function f; a,b such that f(a)*f(b)<0,
#        tolerance tol, maximum number of steps n
# Output: Approximate solution xc

import numpy as np
import matplotlib.pyplot as plt

def sign(x):    #finding the sign of a real number
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0

def bisect(a,b,tol,n):    #main procedure 
    fa = f(a)
    fb = f(b)
    if sign(fa)*sign(fb) >= 0:
        print("The intermediate value test failed.")
        return
    i=0
    while (b-a)/2.0 > tol:
        i = i+1
        if i == n:
            print("Process failed after max interations.")
            return
        c = (a+b)/2.0
        fc = f(c)
        if fc == 0:                        # c is a solution, done
            print("Found exact solution.")
            return c
        if sign(fc)*sign(fa) < 0:    # a and c make the new interval
            b = c
            fb = fc
        else:                                # c and b make the new interval
            a = c
            fa = fc
    return c, i

# Define the function f(x), plot its graph and approximate the root

def f(x):
    return(np.cos(x)-np.sin(x))

x = np.linspace(-3,2,100)   #generates 100 x values between -3,2
y = f(x)
plt.plot(x,y)   # plots the graph of the function
plt.show()

print("Approximate root & steps:")
print(bisect(0.0,1.0,0.5*10**(-6),100)) #calls the bisect procedure with specific parameters

