import numpy as np

s1 = np.array([1 , 2 ,3 ])
s2 = np.array([7 , 4 , 3 ])
s3 = np.array([2 , 1 ,9])

s12 = s1 - s2 
s13 = s1 - s3 
s23 = s2 - s2 

fs12 = np.linalg.norm(s12 , 2)
fs13 = np.linalg.norm(s13 , 2)
fs23 = np.linalg.norm(s23 , 2)
print(fs12)
print(fs13)
print(fs23)