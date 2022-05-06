import numpy as np
import sympy as sp
from sympy.solvers.solveset import linsolve

c = np.array([[1 , 0 , 2 , 3 ] , [4 , -1 , 0 , 2] , [0 , -1 , -8 , -10 ]])

def ex3(c) :
     it = c.T
     #4r1 - r2 --- r2 
     c[1] = c[0] * 4 - c[1] 
     #r3 = r2 + r3 
     c[2] = c[1] + c[2]
     rowSpace = np.array([c[0] , c[1]])
     columnspace = np.array([it[0] , it[2]])
     return  rowSpace , columnspace 
     
print(ex3(c))
          