import numpy as np 
a = np.array([[3,4,5] , [1 , 3 ,1 ] , [1 , 1, 2]])
mes1 = "ATTACK"
mes2 = "LINEAR ALGEBRALABORATORY"
apl = list(map(chr , range ( 97 - 32 , 123 - 32)))
apl.append(" ")
def definrange(a , b) :
     for i in range(len(a)):
          if a[i] == b : 
               return i 
               
def encode(mes , str , arr , ) :
     result = []
     for i in range(len(mes)) : 
          result.append( definrange(  str , mes[i]))
     k = round( len(mes)/ 3 ) 

     return ( np.array(result).reshape( k , 3 ) + 3 )@arr

print("ATTACK encode : \n", encode(mes1 , apl , a) )
print("LINEAR ALGEBRA LABORATORY : \n", encode(mes2 , apl , a) )