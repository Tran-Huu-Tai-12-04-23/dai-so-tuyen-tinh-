import numpy as np

b1 = np.array([[1 , -7 ] , [ 2 , 3  ] ])
b2 = np.array([[5 , -4 , 2 ] , [1 , 2 ,3 ] ,[ -2 , 1 , 0 ]])

b3 = np.array([[-3 , 0 , 0] , [0 , 4 , 0 ] , [0 , 0 , 2]])
b4 = np.array([[3 , 6] , [1 , 0]])
b5 = np.array([[3 , 6 , -1 ] , [3 , 1 , 0 ] , [2 , 4 , -7]])

fb1 = np.linalg.norm(b1 ,np.Infinity)
print(fb1)
fb2 = np.linalg.norm(b2 ,np.Infinity)
print(fb2)
fb3 = np.linalg.norm(b3 ,np.Infinity)
print(fb3)
fb4 = np.linalg.norm(b4 ,np.Infinity)
print(fb4)
fb5 = np.linalg.norm(b5 ,np.Infinity)
print(fb5)
