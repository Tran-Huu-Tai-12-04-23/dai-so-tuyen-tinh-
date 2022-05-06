import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(-6 , 6 , 0.1)
y = x.copy()

def cau2a(x , y ):
    f = lambda x , y: np.cos(x)*np.cos(y)*np.exp(-(np.sqrt(x**2 + y**2)/4))
    x1 , y1 = np.meshgrid(x , y, d)
    print(x1)
    print(y1)
    z = f(x1, y1)
    
    pr_xy = plt.axes(projection = '3d') 
    
    pr_xy.plot_surface(x1 , y1 , z , cmap = 'hot' , linewidth = 0)
    pr_xy.set_title("S")
    plt.show()
    
def cau2b(x , y):
    f = lambda x , y : - (x*y**2) / ( x**2 + y**2)
    
    x1 , y1 = np.meshgrid(x , y)
    
    z = f(x1 , y1)
    
    dtx_y = plt.axes(projection = "3d")
    dtx_y.plot_surface(x1 , y1 , z , cmap = 'cool' , linewidth = 0)
    plt.show()

def cau2c(x , y):
    f = lambda x , y : ( x*y*(x**2-y**2) ) / ( x**2 + y**2)
    
    x1 , y1 = np.meshgrid(x , y)
    
    z = f(x1 , y1)
    dtx_y = plt.axes(projection = "3d")
    
    dtx_y.plot_surface(x1 , y1 , z , cmap = 'gray' , linewidth = 0)
    plt.show()
    
def cau2d(x , y):
    f = lambda x , y : y**2 - y**4 - x**2
    
    x1 , y1 = np.meshgrid(x , y)
    
    z = f(x1 , y1)
    
    dtx_y = plt.axes(projection = "3d")
    dtx_y.plot_surface(x1 , y1 , z , cmap = 'spring' , linewidth = 0)
    plt.show()
    
cau2a(x ,y)
cau2b(x,y)
cau2c(x , y)
cau2d( x , y)