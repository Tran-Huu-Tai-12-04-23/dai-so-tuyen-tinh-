print("Exercise09 :")
import numpy as np
def isOrthogonaSet(a) :
  m = a.shape[0]
  n = a.shape[1]
  if( m != n ) :
    return False 
  for i in range( 0 , n ) :
    for j in range(0 , n ):
      sum = 0 
      for k in range( 0 , n )  :
        sum = sum + ( a[i][k] * a[j][k])
      if( i != j  and sum != 0) :
        return False
  return True
u1 = ( 3 , 1 , 1)
u2 = ( -1 , 2 , 1)
u3 = ( -1/2 , -2 , 7 / 2)
a9 = np.array([u1 , u2 , u3])
print(isOrthogonaSet(a9))