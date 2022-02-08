# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 02:13:27 2022

@author: bugra
"""

def dydx(xi, yi):
    return yi-xi
 
def myRungeKutta(dydx,xi, yi, h,x):

    while(x>=xi):
        k1 = dydx(xi, yi)
        k2 = dydx(xi + 1/2 * h, yi + 1/2 * k1 * h)
        k3 = dydx(xi + 1/2 * h, yi + 1/2 * k2 * h)
        k4 = dydx(xi + h, yi + k3 * h)
 
        y_next = yi + (1 / 6)*(k1 + 2 * k2 + 2 * k3 + k4)*h #update y
        yi = y_next  #update y0
        xi = xi + h #update x0

    return y_next
 
xi = 0
yi = 0
h = 0.1
x = 20
result = myRungeKutta(dydx,xi, yi, h,x)
print ('The value of y at x is:', result)