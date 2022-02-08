# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 02:13:26 2022

@author: bugra
"""
import matplotlib.pylab as plt
def f1(x):
    return x**3 - x - 1

def f2(x):
    return x**2 - 5

def newtonRaphson(f,x0,numIter):
    mydic = dict()
    
    df1 = lambda x: 3*x**2 - 1
    df2 = lambda x: 2*x
    
    n=1
    while(numIter>=n):
        
        x_next = x0 - (f(x0) / df2(x0))
        
        if f(x_next) == 0:
            print("Found exact solution after",n," iteration!")
            return x_next,mydic
        else:            
            x0 = x_next
                
        mydic[n] = x_next    
        n += 1
    return x_next,mydic
            
numIter = 20
x0 = 1
result,mydict = newtonRaphson(f2, x0, numIter)
print(result)

lists = sorted(mydict.items()) # sorted by key, return a list of tuples
x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.figure(figsize = (12, 8))
plt.plot(x[5:20], y[5:20])
plt.xlabel('Iteration number')
plt.ylabel('Root value')
plt.show()