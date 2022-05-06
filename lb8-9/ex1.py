import numpy as np

a = np.array([[2 ,2 ] , [2 , 3 ]])
b = np.array([4 , 6])
at = a.T
at_a = at@a
at_a_1 = np.linalg.inv(at_a)
at_b = at@b
u = at_a_1@at_b
print(u)