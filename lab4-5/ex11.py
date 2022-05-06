import numpy as np 
a11 = np.array([[0.25,0.15 , 0.1 ] , [0.4 , 0.15 , 0.2 ] , [0.15 , 0.2 , 0.2 ]])
i11 = np.array([[1,0,0] , [0,1,0] , [0,0,1]])
i11_a11 = i11 - a11
print("I11- A11 = " , i11_a11)

inva11 = np.linalg.inv(i11_a11)
print("A11^-1 = " , inva11)
d11 = np.array([100 , 100 , 100 ])
d11t =  d11.T
p11 = inva11.dot(d11t)
print("P11 = " , p11)