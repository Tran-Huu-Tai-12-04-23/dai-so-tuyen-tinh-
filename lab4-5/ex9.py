import numpy as np
from sympy import * 
from sympy.solvers import linsolve  

x , y, z, t = symbols('x ,y,z,t')
result8 = linsolve([2*x - 4*y + 4*z + 0.777*t - 3.86 , -2*y + 2*z - 0.056*t +3.47 , 2 *x -2*y] , ( x , y , z ,t))
print(result8)

