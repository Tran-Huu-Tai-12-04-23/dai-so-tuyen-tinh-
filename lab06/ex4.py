import numpy as np

u = np.array([1,1])
v = np.array([0,1])
uv = u.dot(v)

tu = np.linalg.norm(u , 2)
tv = np.linalg.norm(v , 2)
print(tu)
tvh = tu * tv 

cos_x = uv /( tu * tv )
print("Cos_X2 = " , cos_x)


u2 = np.array([1,0])
v2 = np.array([0,1])
uv2 = u2.dot(v2)

tu2 = np.linalg.norm(u2 , 2)
tv2 = np.linalg.norm(v2 , 2)
print(tu2)
tvh2 = tu2 * tv2 

cos_x2 = uv2 /( tu2 * tv2 )
print("Cos_X2 = " , cos_x2)

u3 = np.array([-2,3])
v3 = np.array([1/2,-1/2])
uv3 = u3.dot(v)

tu3 = np.linalg.norm(u3 , 2)
tv3 = np.linalg.norm(v3 , 2)
print(tu3)
tvh3 = tu3 * tv3 

cos_x3 = uv3 /( tu3 * tv3 )
print("Cos_X3 = " , cos_x3)
