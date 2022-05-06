import numpy as np
from sympy import * 
from sympy.solvers import linsolve 

x , y, z = symbols('x,y,z')
x6 = linsolve([ x + 2 * y + z - 1 , 2*x + 2*y + 2*z - 1 , 2*x + 4*y + z - 2 ] , ( x , y , z ))

print("(x,y,z) = " , x6)