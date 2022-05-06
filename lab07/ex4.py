from sympy import *
import numpy as np
from sympy.solvers.solveset import linsolve 
print("exercise 04 :")
x1 , x2 , x3 , x4 =  symbols('x1 , x2 ,x3 ,x4')
x4x = linsolve([ x1 + 2 *x3 + 3 * x4 , 4*x1 - x2 + 2 * x4 , -x2 -8*x3 - 10*x4 ] , ( x1 , x2 ,x3 , x4))
print(x4x)

v41 = np.array([-2 , -8 , 1 , 0])
v42 = np.array([-3,-10,0,1])