# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 02:13:25 2022

@author: bugra
"""

import matplotlib.pylab as plt

def f2(x):
    return x**3 + 5*x**2 + 7*x + 5

def f1(x):
    return (0.5*x) - (x+1)**(1/3)

def bisection(f,a,b,iterNum):
    
    mydict = dict()
    
    if f(a)*f(b) > 0:
        print("Failed because can not find root that interval!")
        return None
    
    n = 1
    while(iterNum >= n):
        
        m = (a+b)/2 
        
        if f(m)*f(b) < 0:
            a = m
        elif f(m)*f(a) < 0:
            b = m
        elif f(m) == 0: #if root comes func then we know that solved
            print("Found exact solution after ",n," iteration!")
            mydict[n] = m
            return m,mydict
        
        mydict[n] = (a+b)/2       
        n += 1
        
    return (a+b)/2, mydict

a = -4
b = 0
iterNum = 50
result , dic= bisection(f2, a, b, iterNum)
print(result)
lists = sorted(dic.items()) # sorted by key, return a list of tuples
x, y = zip(*lists) # unpack a list of pairs into two tuples
plt.figure(figsize = (12, 8))
plt.plot(x[10:50], y[10:50])
plt.xlabel('Iteration number')
plt.ylabel('Root value')
plt.show()