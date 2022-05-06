import numpy as np 
from sympy import *
from sympy.solvers import linsolve  

#3x1 = x3 
#8x1 = 2x4 
#2x2 = 2x3 + x4 

x1 , x2 , x3 , x4 = symbols('x1,x2,x3,x4')
result = linsolve((3*x1 - x3  , 8 * x1 - 2* x4 , 2 *x2 - 2*x3 + x4 ) , (x1 , x2 ,x3 , x4))
print(result)
