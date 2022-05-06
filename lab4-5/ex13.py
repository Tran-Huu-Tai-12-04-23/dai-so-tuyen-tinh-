import numpy as np
from sympy import * 
from sympy.solvers import linsolve  


x1 ,x2 , x3 , x4 , x5 , x6 , s , t = symbols('x1,x2,x3,x4,x5,x6,s,t')
x5 = s 
x6 = t

result = linsolve( [x1 + x4 - 8 , x2 + x5 - 7 , x3 + x6 - 6 , x1 + x2 + x3 - 15 , x4 + x5 + x6 - 6 ], ( x1 ,x2 , x3 , x4 ,x5 ,x6 ))

print(result)