from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
from exercise_1b_function import get_input_data
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def draw_plane(A, b):
    xx, yy = np.meshgrid(np.arange(-10,10.1,0.1), np.arange(-10,10.1,0.1))
    plt3d = plt.figure().gca(projection='3d')
    for i in range(3):
      # enter your code here to calculate zz
      zz = ( b[i]-A[i][0]*xx-A[i][1]*yy )/A[i][2]
      plt3d.plot_surface(xx, yy, zz, alpha=0.5, cmap=cm.coolwarm)
    ax = plt.gca()
    plt.show()

if __name__ == '__main__':
   input_id = 'case1'
   A, b = get_input_data(input_id)
   draw_plane(A, b)
