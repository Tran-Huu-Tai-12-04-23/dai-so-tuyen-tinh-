
import numpy as np
import sympy as sp
from sympy.solvers.solveset import linsolve

w = np.array([1 , 1 ,-1 , -3 ]).T
a = np.array([[7 , 6 , -4 , 1 ] , [-5 , -1 , 0 , -2] , [9 , -11 , 7 , 3 ] , [ 19 , -9 , 7 , 1 ] , [w]])
ranka = np.linalg.matrix_rank(a)
print("a.shape = " , a.shape[0])
print(ranka)
k = a.shape[0]

if k > ranka :
     print(w , " is column space of A")

w2 = np.array([1,2,1,0])
b = np.array([[-8 , 5 , -2 , 0] , [-5 , 2 , 1 , -2 ] , [10 , -8 , 6 , -3 ] , [3 , -2 , 1 , 0]])

rankb = np.linalg.matrix_rank(b)
print("b.shape = " , b.shape[0])
print(rankb)
k = b.shape[0]

if k > rankb :
     print(w2 , " is column space of A")

