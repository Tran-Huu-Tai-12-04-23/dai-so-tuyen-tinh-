import numpy as np
from sympy import * 
from sympy.solvers import linsolve  

#( r , g , b ) = ( x , y ,z ) * ( a) ^ -1

a10 = np.array([[0.61 , 0.29 , 0.15 ] , [0.35 , 0.59 , 0.063 ] , [0.04 , 0.12 , 0.787]])
x , y ,z , r , g ,b = symbols('x , y , z , r , g ,b')
inva10 = np.linalg.inv(a10)
print(inva10)
r = x*(inva10[0])
g = x*(inva10[1])
b = x*(inva10[2])
#pt cau R G B 
print("R = ", r )
print("G = " , g )
print("B = " , b )
