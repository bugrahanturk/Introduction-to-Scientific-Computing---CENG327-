from scipy.io import mmread
import numpy as np
from scipy import linalg


def jacobi(A,b,numIter): 
    
    n = len(A)
    
    x_n = np.zeros((n,n),dtype=np.float64())
 
    A = A + A.transpose() + np.identity(len(A))
     
    res = 0.0   
    
    x = []
           
    for n in range(numIter):
        for i in range(len(x_n)):
            for k in range(len(x_n)):
                if(i!=k):
                    res += A[i][k]*x_n[k]
                    
            x.append((b[i]-res)/A[i][i])
            res=0.0
        
        x_ncop = np.copy(x) # make copy because of that array point itself and changing itself also
        x_n= x_ncop

        if n != numIter-1:
            x.clear()
        else:
            print(x_n)
    
    return x_n


mat_f = mmread("impcol_b.mtx")

mat = np.array(mat_f.toarray())

A = mat

n = len(A)

b = np.ones(n,dtype=np.float64())

x_solution = jacobi(A,b,4)

x_real = linalg.solve(A,b)

scipy = x_solution - x_real

scipy_result = linalg.norm(scipy, ord = 1)

print("Real value {} Jacobi: {}".format(x_real,scipy_result))

