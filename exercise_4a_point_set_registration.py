from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pickle

from numpy.typing import _128Bit

def draw_landmarks(P, Q):
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')
  ax.scatter(Q[0,:], Q[1,:], Q[2,:], c='r')
  ax.scatter(P[0,:], P[1,:], P[2,:], c='b')
  plt.show()

if __name__ == '__main__':

  pkl_path = 'Module3-1.pkl'
  with open(pkl_path, 'rb') as fp:
    data = pickle.load(fp)
  P = data['P']
  Q = data['R']
  draw_landmarks(P, Q)

  # enter your code here
  nP = np.array(P)
  nQ = np.array(Q)
  I = np.eye(3)
  R = np.column_stack((Q,I))
  
  a=0 
  b=0
  for i in range(49):
    Pi = P[:,[i]]
    Ri = R[:,[i]]
    Qi = Q[:,[i]]
    Ri = np.column_stack((Qi,I))
    a += Ri.T@Ri
    b += Ri.T@Pi
  u = np.linalg.inv(a)@b
  
  s = u.T[:,[0]]
  t = u.T[:,[1,2,3]].T
  R = s*Q + np.tile(t,49) #在每一行都加上t
  draw_landmarks(P,R)

  #(a) s = 1 , t = [0,0,0].T
  s = 1
  t = np.array([[0,0,0]]).T
  ds = np.sum(np.sqrt((P-s*Q-t)*(P-s*Q-t)))
  print(ds)

  # (b) s = u[0] , t = u[1]
  s = u[0]
  t = u[1:]
  ds = np.sum(np.sqrt((P-s*Q-t)*(P-s*Q-t)))
  print(ds)
  

