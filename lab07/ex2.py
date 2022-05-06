import numpy as np
import sympy as sp
from sympy.solvers.solveset import linsolve
a , b ,c , d , e = sp.symbols('a , b , c ,d , e')
x1 = np.array([1 , -2 , 0])
x2 = np.array([0 , -4 , 1])
x3 = np.array([1 , -1 , 1])
def ex2a(a , b , c , x1, x2 , x3 ) :
     j = 0 
     res = []
     for i in x1 :
          res.append(x1[j]*a + x2[j]*b + x3[j]*c)
          j = j + 1 
     if( linsolve( res , ( a , b , c ) ) == {( 0 , 0 , 0)} ) :
          return True
     else :
          return False 

if( ex2a(a , b ,c , x1 , x2 , x3 ) == True ) :
     print(" The vectors are linearly independent !")
else :
     print(" The vectors aren't linearly independent !")
''' cau b  '''
x1 = np.array([1 , 0 , 2])
x2 = np.array([0 , 1 , 4])
x3 = np.array([2 ,2 , 4])

if( ex2a(a , b ,c , x1 , x2 , x3 ) == True ) :
     print(" The vectors are linearly independent !")
else :
     print(" The vectors aren't linearly independent !")