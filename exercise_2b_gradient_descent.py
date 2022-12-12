import numpy as np

if __name__ == '__main__':
  b = np.array([[1], [2]])
  A = np.array([[1, -2], [1, -2]])
  # enter your code here
x = np.array([[-2,2]])
x = x.T
alpha = 0.04 
max_iter = 1000
f = np.linalg.norm(A@x-b)**2 #最小平方誤差
for k in range(max_iter):
  print( k, '({:.4f} {:.4f})'.format(x[0][0],x[1][0]), '{:.8f}'.format(f))

  x_prev = x 
  x = x- alpha*2*(A.T@A@x-A.T@b)

  if (np.linalg.norm(x-x_prev) <= 10**-8):
    break
  f = np.linalg.norm(A@x-b)**2

