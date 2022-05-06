import numpy as np
from sympy import * 
from sympy.solvers import linsolve  

g , k ,h = symbols('g,k,h')

x2 = np.array([[1 , -4 , 7 , g ] , [ 0 , 3 , -5 , h ] , [ -2  , 5 , -9 , k ]])
print("MatrixA : \n" , x2  )
j = 0
for i in x2[2]:
     it = i + 2*x2[0][j]
     x2[2][j] = it
     j = j +1 
j = 0 
for i in x2[2]:
     it = x2[1][j] + i
     x2[2][j] = it
     j = j + 1 
print("Equation involving g, h, and k that makes this augmented matrix correspond to con-persistent system : " , x2[2][3])