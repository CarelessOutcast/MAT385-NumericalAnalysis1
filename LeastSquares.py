# Numerical Analysis - Least Squares method

import numpy as np
import matplotlib.pyplot as plt


#Inconsistent Systems

A = np.array([[3,-1,2],[4,1,0],[-3,2,1],[1,1,5],[-2,0,3]])
b = np.array([10,10,-5,15,0])

print('Solving Inconsistent System Ax=b\n','A=',A,'\nb=',b)

normalA = np.dot(np.transpose(A),A)
normalb = np.dot(np.transpose(A),b)
print('\nNormal system:')
print('\nTranspose(A)*A\n', normalA)
print('\nTranspose(A)*b\n', normalb)


sol = np.linalg.solve(normalA, normalb)  #solve the least-squares problem
print('\nLeast-Squares Solution:',sol.T)

normerror = np.linalg.norm(np.dot(A,sol)-b,2)
print('\n2-norm error = ', normerror)

rmse = normerror/np.sqrt(len(b))
print('\nRoot mean squared error = ', rmse)



#Least-Squares Method for Data Fitting


data = np.array([[1,2],[3,2],[4,1],[6,3]])  #input data

x , y  = data.T    # build the x, y vectors

#Line of best fit

A1 = np.vstack([np.ones(len(x)),x]).T  #build matrix A1 for line of best fit
print('\n\n Associated Matrix A (line fit):\n',A1)

c1,c2 = np.linalg.lstsq(A1, y, rcond=None)[0]  #solve the least-squares problem
print('\nCoefficients of line of best fit c1+c2*x:\n',c1,c2)

RMSE = np.linalg.norm(c1+c2*x - y,2)/np.sqrt(len(x))  #find the root mean square error
print('\n Root Mean Square Error = ',RMSE)

xvalue=5.0
print('\nEvaluate line at x =', xvalue, ': y =',c1+c2*xvalue)

plt.plot(x, y, 'o', label='Original data', markersize=10) #plot the data points and line of best fit
plt.plot(x, c1+c2*x, 'r', label='Fitted line')
plt.legend()
plt.show()

#Parabola of best fit

A2 = np.vstack([np.ones(len(x)),x,x**2]).T  #build matrix A2 for parabola of best fit
print('\n\n Associated Matrix A (parabola fit):\n',A2)

c1,c2,c3 = np.linalg.lstsq(A2, y, rcond=None)[0]  #solve the least-squares problem
print('\nCoefficients of parabola of best fit c1+c2*x+c3*x^2:\n',c1,c2,c3)

RMSE = np.linalg.norm(c1+c2*x+c3*x**2 - y,2)/np.sqrt(len(x))  #find the root mean square error
print('\n Root Mean Square Error = ',RMSE)

xvalue=5.0
print('\nEvaluate parabola at x =', xvalue, ': y =',c1+c2*xvalue+c3*xvalue**2)

plt.plot(x, y, 'o', label='Original data', markersize=10) #plot the data points and parabola of best fit
x = np.linspace(min(x),max(x),100)
plt.plot(x, c1+c2*x+c3*x**2, 'r', label='Fitted parabola')
plt.legend()
plt.show()


