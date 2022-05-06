import numpy as np
q=[0,0,0.7,0.5,0,0.3]
d1=[1,0.5,0.3,0,0,0]
d2=[0.5,1,0,0,0,0]
d3=[0,1,0.8,0.7,0,0]
d4=[0,0.9,1,0.5,0,0]
d5=[0,0,0,0,0.7,0]
d6=[0,0.6,0,1.0,0.3,0.2]
A=np.vstack((np.vstack((np.vstack((np.vstack((d1,d2)),d3)),d4)),d5))
d=[]
for i in range(A.shape[0]):
  c=sum(q*A[i,:])/(np.linalg.norm(q,2)*np.linalg.norm(A[i,:],2))
  d.append(c)

print(np.argmax(d))