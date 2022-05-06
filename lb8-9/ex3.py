
import numpy as np
from matplotlib import pyplot as plt
from sympy import *
print("Exercise 3")
A3 = np.array([[0,1],[1,1],[2,2],[3,2]])
sa3 = A3.shape
print(sa3)
n = sa3[0]
x_tb = 0
y_tb = 0
for i in range(n):
    #print(A3[i,0],A3[i,1])
    x_tb = x_tb + A3[i,0]  # 0 + 1 + 2 + 3
    y_tb = y_tb + A3[i,1]  # 1 + 1 + 2 + 2
x_tb =x_tb/n #6/4 = 1.5
y_tb =y_tb/n #6/4 = 1.5
m1 = 0
m2 = 0
for i in range(n):
    m1 = m1 + (A3[i,0] - x_tb)*(A3[i,1] - y_tb)
    m2 = m2 + (A3[i,0] - x_tb)*(A3[i,0] - x_tb)
m = m1/m2
#print("m = ",m)
b = y_tb - m*x_tb
# In duong thang can tim
x = symbols('x')
y = m*x + b
print("y = ",y)
# Ve do thi mo phong
x1 = np.arange(0,4,0.01)
y1 = m*x1 + b
plt.plot(x1, y1, color='red')
plt.plot(0, 1, 'ko',color='green')
plt.plot(1, 1, 'ko',color='green')
plt.plot(2, 2, 'ko',color='green')
plt.plot(3, 2, 'ko',color='green')
  