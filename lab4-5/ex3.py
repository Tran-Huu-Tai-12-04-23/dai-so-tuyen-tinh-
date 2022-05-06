import matplotlib.pyplot as plt 
import numpy as np

x = np.arange(-5 , 0 , 0.01)
y1 = -x - 1 
y2 = (-5/8) * x + 1 / 8
y3 = (-4/3 ) * x - 2 
plt.plot(x , y1 )
plt.plot(x , y2 )
plt.plot(x , y3 )
plt.show()

y4 = -x - 1
y5 = -x + 1 
plt.plot(x , y4 )
plt.plot(x , y5 )
plt.show()