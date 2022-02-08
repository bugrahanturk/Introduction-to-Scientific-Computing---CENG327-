# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 02:13:29 2022

@author: bugra
"""

def dydx(x,y):
    return y-x

def myEuler(dydx,h,x,xi,yi):
    
    while(x>=xi):
        yi = yi + dydx(xi,yi) * h #apply formula
        xi = xi + h   #update xi
    return yi

x = 20
xi = 0
h = 0.1
yi = 0
print("Result of given x={} is {}".format(x, myEuler(dydx, h, x, xi, yi)))