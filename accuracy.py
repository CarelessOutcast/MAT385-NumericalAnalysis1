
# Section 1.3 Accuracy issues
# Now we look at how much a root changes if the equation changes. We consider the function 
#     f(x) = (x - 1) (x - 2) (x - 3) (x - 4) (x - 5) (x - 6)
# with the obvious roots x = 1, 2, 3, 4, 5, 6
# Let us modify the equation by a term of type -10^(-6)*x^7 
#
# We use the the 'fsolve' command part of the scipy.optimize library
#    and the 'derivative' command from scipy.misc

from  scipy.optimize import fsolve
from  scipy.misc import derivative
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

def f(x): 
	return (x-1.0)*(x-2.0)*(x-3.0)*(x-4.0)

def g(x):
    return x**6

eps = - 10.0**(-6.0)

def fnew(x):
    return f(x)+eps*g(x)

r_new=fsolve(fnew,4.0)

print('New root = ', r_new)

# We estimate the change in the root using the appropriate formula 
delta_r = - (eps*g(4.0)/derivative(f,4.0,10**(-5.0)))

print('Change in root = ', delta_r)

# We estimaste the error magnification factor

emf = g(4.0)/(4.0*derivative(f,4.0,10**(-5.0)))

print('Error magnification factor = ',emf)








