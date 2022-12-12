import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy import linalg

def draw_surface(A, b):
  xx, yy = np.meshgrid(np.arange(-2,2.1,0.1), np.arange(-2,2.1,0.1))
  F1 = A[0][0]*xx + A[0][1]*yy - b[0];
  F2 = A[1][0]*xx + A[1][1]*yy - b[1];
  zz = F1*F1 + F2*F2;
  plt3d = plt.figure().gca(projection='3d')
  plt3d.plot_surface(xx, yy, zz, alpha=0.7, cmap=cm.coolwarm)

if __name__ == '__main__':
  b = np.array([[1], [2]])
  A = np.array([[1, -2], [1, -2]])

  draw_surface(A, b)

  # enter your code here
sol = np.array([[],[],[]]) #創造一個3*n的矩陣來得到點上的值
x = np.array([[-2,2]])
x = x.T
alpha = 0.02 
max_iter = 1000
f = np.linalg.norm(A@x-b)**2
for k in range(max_iter):
  temp = np.array([ x[0], x[1], [f] ]) 
  sol = np.hstack((sol,temp))
  x_prev = x 
  x = x- alpha*2*(A.T@A@x-A.T@b)

  if (np.linalg.norm(x-x_prev) <= 10**-8):
    break
  f = np.linalg.norm(A@x-b)**2

  
print(sol)
ax = plt.gca()
ax.scatter(sol[0],sol[1],sol[2])

plt.show()
