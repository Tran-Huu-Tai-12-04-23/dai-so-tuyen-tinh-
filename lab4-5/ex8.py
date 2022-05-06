import numpy as np
from sympy import * 
from sympy.solvers import linsolve 

# x*3 + y*3.2 = 118.4
# 3.5 * x+ 3.6*y = 135.2 
a8 = np.array([[3,3.2] , [3.5 , 3.6]])
b8 = np.array([118.4 , 135.2 ])

result = np.linalg.solve( a8 , b8 )
print(result)

# 16 per child and 22 adults...