import numpy as np
from sympy import * 
from sympy.solvers import linsolve  
x , y, z = symbols('x,y,z')
x5 = np.array([[1,3,2] , [1,6,-5] , [2,-5,-3]])
x5 = x5.T
print(x5)
#a
detx5 = np.linalg.det(x5)
print(detx5)

invx5 = np.linalg.inv(x5)
print(invx5)
#b
x5_5 = linsolve( [ invx5[0][0] + invx5[0][1] + invx5[0][2] - 1 , invx5[1][0] + invx5[1][1] + invx5[1][2] + 1 , invx5[2][0] + invx5[2][1] + invx5[2][2] ] , ( x , y , z ))

print("b : " ,x5_5)

