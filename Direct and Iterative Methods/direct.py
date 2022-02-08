from scipy.io import mmread
import numpy as np
from scipy import linalg


def ULFactorization(A):
    
    n = len(A)
          
    P = np.identity(n)

    B = np.matmul(P,A)
    B = np.matmul(B,P)
    
    b_U = B
    
    b_L = np.zeros((n,n),dtype=np.float64)
    
    for i in range(len(b_L)):
        for k in range(len(b_L)):
            if(i==k):
                b_L[i][k]=1
    
      
    for k in range(n):
        for i in range(k+1,n):
            m = b_U[i][k]/b_U[k][k]
            b_U[i][k] = 0
            for j in range(k+1,n):
                b_U[i][j] = b_U[i][j] - (m*b_U[k][j])
            b_L[i][k] = m
    
    P_T = np.transpose(P)
    
    a_L = np.zeros((n,n),dtype=np.float64())
    a_U = np.zeros((n,n),dtype=np.float64())
    
    a_L = np.matmul(P_T,b_L)
    a_L = np.matmul(a_L,P_T)
    
    a_U = np.matmul(P,b_U)
    a_U = np.matmul(a_U,P_T)
    
    A = np.matmul(a_L,a_U)
    
    return a_U,a_L

mat_f = mmread("impcol_b.mtx")

mat = np.array(mat_f.toarray())

A = mat
  
n = len(A)

A_diag_dom = A + A.transpose() + np.identity(n)

b = np.ones(n,dtype=np.float64())

U,L = ULFactorization(A_diag_dom)

y = np.matmul(np.linalg.inv(L),b)
x = np.matmul(np.linalg.inv(U),y)

scipy = linalg.solve(A,b)

print("My Solution: {}\nScipy Calculation: {}".format(x,scipy))