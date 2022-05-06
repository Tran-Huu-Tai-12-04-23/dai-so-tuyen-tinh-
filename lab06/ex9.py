import numpy as np 
doc1 = np.array([ 0,4,0,0,0,2,1,3])
doc2 = np.array([3,1,4,3,1,2,0,1])
doc3 = np.array([3,0,0,0,3,0,3,0])
doc4 = np.array([0,1,0,3,0,0,2,0])
doc5 = np.array([2,2,2,3,1,4,0,2])
e = np.array([doc1 , doc2 , doc3 , doc4 , doc5 ])
nrank = np.linalg.matrix_rank(e)
print(nrank)
for i in range(nrank) :
     print("E[i] = " ,e[i])
     for j in range(nrank) :
          cosSim = np.dot(e[i] , e[j] ) / ( np.linalg.norm(e[i]) * np.linalg.norm(e[j]))
          print("Cosin Similarity : " , round(cosSim, 2 ) )