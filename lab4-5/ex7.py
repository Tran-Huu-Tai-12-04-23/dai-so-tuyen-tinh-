import numpy as np
from sympy import * 
from sympy.solvers import linsolve 

a = np.array([[1,1,1] , [1,2,4] , [1,3,9] ] )
b = np.array([6,15,28])

x7 = np.linalg.solve(a , b.T)
print("(x,y,z) = " , x7)