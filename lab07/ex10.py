#Exercise 10: Let y and u vector.
import numpy as np
#Write a function to find the orthogonal projection of y on u.
#Hint: projuy = (< y · u >/< u · u >)u. For example, y =(7,6) and u =(4,2)
print("Exercise 10")
def proj_uy(y,u):
    print("y = ",y)
    print("u = ",u)
    proj_uy = ((y.dot(u))/(np.linalg.norm(u,2))**2) * u
    return proj_uy
print("------------------------------")
y1 = np.array([7,6])
u1 = np.array([4,2])
k = proj_uy(y1,u1)
print(k)