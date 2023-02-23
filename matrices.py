# Matrix operations


import numpy as np

import scipy.linalg as la

A=[[1,2,-1],[0,3,-1],[5,-1,1]]

print('A=',A)

print('Norm 1 of A: ',np.linalg.norm(A,1))

print('Norm inf of A: ',np.linalg.norm(A,np.inf))

print('Condition number: ',np.linalg.cond(A,np.inf))

(P, L, U) = la.lu(A)

print('P=',P)
print('L=',L)
print('U=',U)
