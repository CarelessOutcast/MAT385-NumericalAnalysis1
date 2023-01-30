#
# Secant Method; Numerical Analysis
# Carlos Tapia
# 
# Secant method 
# http://hplgit.github.io/prog4comp/doc/pub/p4c-sphinx-Python/._pylight007.html
#
#

import sys
import numpy as np 

def main():
    x0 = 1 
    x1 = 2

    solution, iterations = secant(a,x0,x1,10**(-5))
    print(f"a. iterations: {iterations}\t solution: {solution}")

    solution, iterations = secant(b,x0,x1,10**(-5))
    print(f"b. iterations: {iterations}\t solution: {solution}")

    solution, iterations = secant(c,x0,x1,10**(-5))
    print(f"c. iterations: {iterations}\t solution: {solution}")
    return


# Equation to input() #CHANGEME
def a(x):
    #a. x^3 = 2x + 2 
    return x**3 -2*x - 2;
def b(x):
    #b. e^x + x = 7
    return np.exp(x) + x - 7;
def c(x):
    #c. e^x + sin(x) = 4
    return np.exp(x) + np.sin(x) - 4;

# Formula for Secant Method:
#
# f(x_i) - f(x_{i-1})
# -------------------
#    x_i - x_{i-1}
def secant(f, x0, x1, eps):
    fx0 = f(x0)
    fx1 = f(x1)
    x = 0
    c = 0
    while abs(fx1) > eps and c < 100:
        try:
            denominator = float((fx1-fx0)/(x1-x0))
            x = x1 - float((fx1)/(denominator))
        except ZeroDivisionError:
            print("Division by Zero")
            sys.exit(1)
        x0 = x1
        x1 = x
        fx0 = fx1
        fx1 = f(x1)
        c+=1
    if abs(fx1) > eps:
        c -= 1;
    return x, c;
        



if __name__ == "__main__":
    main()

