import numpy as np
import sympy as sp
from sympy.solvers.solveset import linsolve
a , b ,c ,d = sp.symbols('a , b ,c  ,d')
''' cau a '''
v1= np.array([1 ,2 , 3 , 4])
v2 = np.array([-1 , 0 ,  1 , 3 ])
v3 = np.array([0 , 5 ,-6 , 8 ])
w = np.array([3 , -6 , 17 , 11 ])

def ex1(v1 , v2 , v3 ,w , a , b ,c , d) :
     j = 0 
     res = []
     for i in w :
          res.append(v1[j]*a + v2[j]*b + v3[j]*c -i)
          j = j + 1 
     print(res)
     return linsolve( res , ( a , b , c ) )
print("a  : " , ex1(v1,v2,v3,w,a,b,c,d))
''' cau b  '''
v12 = np.array([1 ,1 ,2 ,2 ])
v22 = np.array([ 2, 3 , 5 ,6 ])
v32 = np.array([ 2, -1 , 3 ,6 ])
w2 = np.array([0 , 5,3,0])

''' cau c '''
''' cau d  '''
def ex1d(v1 , v2 , v3 ,w , a , b ,c , d , v4) :
     j = 0 
     res = []
     for i in w :
          res.append(v1[j]*a + v2[j]*b + v3[j]*c + v4[j]-i)
          j = j + 1 
     print(res)
     return linsolve( res , ( a , b , c ) )