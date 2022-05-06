import numpy as np

e7 = np.array([[80 ,98 , 99 , 85 , 106 , 94  ] , [71 ,92 , 76 , 95 , 100 ,92 ] , [124 , 163 , 140 , 160 , 176 , 161]])
a7 = np.array([[1 ,2,3] ,[2 , 1,2] , [3 , 2 , 4] ])

a_1 = np.linalg.inv(a7)
print(a_1)
D = a_1@(e7)
D = D.T
print(D)


listChar = list(map(chr , range ( 97 - 32 , 123 - 32 )))
listChar.append(" ")
print(listChar)
s=""

for i in range(0,6) :
     for j in D[i]:
          it = int(round( j , 0))
          s+= listChar[it - 4]
     
print("Message : " , s)