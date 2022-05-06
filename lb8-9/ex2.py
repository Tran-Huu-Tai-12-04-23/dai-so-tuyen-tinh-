import numpy as np

a = np.array([[0 , 0 , 1  ] , [ 0 , 1 ,1  ] , [1, 2, 1] , [1, 0, 1],[4 , 1 ,1 ] , [4 , 2 ,1]])
b = np.array([ 0.5 , 1.6 , 2.8 , 0.8 , 5.1 , 5.9])
at = a.T
at_a = at@a
at_a_1 = np.linalg.inv(at_a)
at_b = at@b
u = at_a_1@at_b
print(u)

u2 = np.linalg.solve( at_a , at_b)
print(u)