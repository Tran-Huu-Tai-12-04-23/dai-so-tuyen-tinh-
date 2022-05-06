import numpy as np
def unitVector(a):
    return a/np.linalg.norm(a)
u1 = np.array([2, 3]).T 
u2 = np.array([1, 2, 3]).T
u3 = np.array([1/2, -1/2, 1/4]).T
u4 = np.array([2 ** ( 1 / 2 ) ,  2, -2 ** ( 1 / 2 ), 2 ** ( 1 / 2 )]).T
print(unitVector(u1))
print(unitVector(u2))
print(unitVector(u3))
print(unitVector(u4))