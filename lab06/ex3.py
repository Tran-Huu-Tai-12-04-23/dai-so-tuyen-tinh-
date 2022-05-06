import numpy as np

a3_a = np.array([[5 , -4 , 2 ] , [-1 , 2 , 3 ] , [-2 , 1 , 0 ]])
a3_b = np.array([[1 , 7 , 3 ] , [4 , -2 , -2 ] ,[ -2 , -1 , 1 ]])

a3_c = np.array([[2 , 3 ] , [1 , -1 ]])

f_boun_a = np.linalg.norm(a3_a ,'fro' )
print(f_boun_a)
f_boun_b = np.linalg.norm(a3_b ,'fro' )
print(f_boun_b)
f_boun_c = np.linalg.norm(a3_c ,'fro' )
print(f_boun_c)
