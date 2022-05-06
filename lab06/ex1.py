import numpy as np
a1 = np.array([[1 , -7 ],[ 3 , -8]])
a2 = np.array([[2 , -8 ] , [ 3 , 1 ] ])
a3 = np.array([[-2 , 8 ] , [3 , 1]])
a4 = np.array([[2,3  ] , [1 , -1 ]])
a5 = np.array([[5 , -4 , 2 ] , [-1 , 2 , 3] , [-2 , 1 , 0]])

norm_a1 = np.linalg.norm(a1 , 1)
norm_a2 = np.linalg.norm(a2 , 1)
norm_a3 = np.linalg.norm(a3 , 1)
norm_a4 = np.linalg.norm(a4 , 1)
norm_a5 = np.linalg.norm(a5 , 1)

print(norm_a1)
print(norm_a2)
print(norm_a3)
print(norm_a4)
print(norm_a5)