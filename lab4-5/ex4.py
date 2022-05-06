from matplotlib import projections
import matplotlib.pyplot as plt 
import math
import numpy as np

x = np.arange(-10 , 10 , 0.01)
y = np.arange(-10 , 10 , 0.01)
z = np.arange(-10 , 10 , 0.01)
d1 = x + 2 * y + 5
d1_2 = 2*x + 3 * y - 7 * z - 4
d2 = x - 2 * y + z - 3 
d2_2 = 2*x - 4 *y + 2 * z - 6 
d3 = x + y + z - 1 
d3_3 = 2*x + 2 * y + 3 

x1 , y1  = np.meshgrid( x , y  )
mpd1 = plt.axes(projection = "3d")
mpd1.plot_surface( x1 , y1 ,d1 ,cmap ='hot' ,  linewidth = 0)
mpd1.plot_surface( x1 , y1,d2 )
plt.show()


