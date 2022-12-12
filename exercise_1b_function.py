from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np

def solve_linear_equation(A, b):
  # enter your code here, and remove the following line
  rankA = np.linalg.matrix_rank(A)
  Ab = np.hstack((A,b))
  rankAb = np.linalg.matrix_rank(Ab)
  if(rankA == rankAb == 3):    #b在行空間內
     #print('The linear system Ax=b has only one solution.')
     return 1

  if(rankA == rankAb <3):
      #print('The linear system Ax=b has infinitely many solutions.')
      return 0

  if(rankA != rankAb ):
      #print('The linear system Ax=b has no solutions.')
      return -1
  
  return 0

def flag_to_message(flag):
   if flag == 1:
     print('The linear system Ax=b has only one solution.')
   elif flag == 0:
     print('The linear system Ax=b has infinitely many solutions.')
   elif flag == -1:
     print('The linear system Ax=b has no solutions.')
   else:
     print('Unknown flag!')

def get_input_data(input_id):
   if input_id == 'case1': 
     A = np.array([[3, 2, -1], [6, -1, 3], [1, 10, -2]])
     b = np.array([[-7], [-4], [2]])
   elif input_id == 'case2':
     A = np.array([[4, -1, 3], [21, -4, 18], [-9, 1, -9]])
     b = np.array([[5], [7], [-8]])
   elif input_id == 'case3':
     A = np.array([[7, -4, 1], [3, 2, -1], [5, 12, -5]])
     b = np.array([[-15], [-5], [-5]])
   return A, b

if __name__ == '__main__':
   input_id = 'case3'
   A, b = get_input_data(input_id)
   
   flag = solve_linear_equation(A, b)
   flag_to_message(flag)
   if flag == 1:
     print('The solution is ', np.linalg.solve(A, b))
