# Jacobi Method
# Inputs: full or bandmatrix A, vector b, tolerance, maxsteps
#         number of Jacobi iterations k
# Output: solution x


import numpy as np

def bandmatrix(l,n):
        A = np.zeros((n,n))
        for i in range(n-1):
                A[i,i]=l[1]; A[i+1,i]=l[0]; A[i,i+1]=l[2]
        A[n-1,n-1]=l[1]
        return A


def jacobi(a,b,tol,maxN):
        n = len(b)
        step = 0
        d = [a[i,i] for i in range(n)]
        r = a - np.diag(d)
        x = np.zeros((n,1))
        bb = np.reshape(b,(n,1))
        dd = np.reshape(d,(n,1))
        while step<=maxN:
                berror = np.linalg.norm(np.dot(a,x)-bb,np.inf)
                if berror<tol:
                        print("Number of iterations needed:",step)
                        print("Solution is:\n",x)
                        print("Backward error:",berror)
                        break
                step = step + 1
                x = (bb-np.dot(r,x))/dd
        if step == maxN:
                print("process failed after max interations")
                quit()


###
                
# n=10
# n=100000
n=10000

A=bandmatrix([-1,3,-1],n)       #initialize band matrix A

print("Matrix A:\n",A)

b=np.ones(n)
b[0]=2
b[n-1]=2    #initialize vector b

print("Vector b:\n",b)

jacobi(A,b,0.5*10**(-6),100)    #call jacobi procedure   
