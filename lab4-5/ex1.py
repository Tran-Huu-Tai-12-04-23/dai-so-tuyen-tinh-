import numpy as np 

a = np.array( [ [1 ,2 ,1] , [2 ,1,1] , [2, 1 , 0] ])
b = np.array([0,0,0])
x1 = np.linalg.solve(a , b)
print("XYX : " , x1)

a2 = np.array([ [2,1,1,1] , [1,2,1,1] , [1,1,2,2] , [1,1,1,2]])
b2 = np.array([1,1,1,1])
x2 = np.linalg.solve(a2,b2)

print("XYZT : " , x2)