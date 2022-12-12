from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pickle

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
  Q = data['Q']
  draw_landmarks(P, Q)

  # enter your code here
  nP = np.array(P)
  nQ = np.array(Q)

  a = 0
  b = 0
  for i in range(49):
    Pi = nP[:,[i]]
    Qi = nQ[:,[i]]
    a += Pi.T @ Qi
    b += Qi.T @ Qi
  b = np.linalg.inv(b)
  s = a * b
  print(s)
  draw_landmarks(P,s*nQ)

  # (a) Using the for loop
  d = 0
  for i in range(49):
    Pi = nP[:,[i]]
    Qi = nQ[:,[i]]
    d += np.sqrt((Pi-s*Qi).T @ (Pi-s*Qi))
  d *= 1/49
  print(d)

  # (b) Without using for loop
  E = nP - s*nQ
  ds = np.sum(np.sqrt(np.sum(E*E, axis=0)))/49
  print(ds)
  
  