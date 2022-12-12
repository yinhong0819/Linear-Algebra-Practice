from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

if __name__ == '__main__':
  # enter your code here
  A = np.array([[3,2,1], [6,-1,3], [1,10,-2]])
  print("A array = \n",A)

  b = np.array([[-7],[-4],[2]])
  print("b array = \n",b)

  rankA = np.linalg.matrix_rank(A) #計算秩
  print("rankA = \n",rankA)

  Ab = np.hstack((A,b))    #增廣矩陣
  print("array [A,b] = \n",Ab)

  rankAb = np.linalg.matrix_rank(Ab)
  print("rankAb = \n",rankAb)

  if (rankA == rankAb):
    print("consistent") #b在行向量內
    if (rankA == A.shape[1]):
      print("only one solution") #行滿秩

      solution = np.linalg.solve(A,b)
      print(solution)


