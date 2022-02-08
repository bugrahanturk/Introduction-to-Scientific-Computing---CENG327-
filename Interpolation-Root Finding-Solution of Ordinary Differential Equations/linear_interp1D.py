# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 06:45:52 2022

@author: bugra
"""

import matplotlib.pylab as plt
from scipy.interpolate import interp1d

#Interpolation 
def read_files(f_name):
    
    x = []
    y = []
    
    f = open(f_name, "r")
    lines = f.readlines()
    
    for i in lines:
        l = i.split()
        x.append(float(l[0]))
        y.append(float(l[1]))     

    return x,y

def myInterpolationFunc(xData,yData,interpolationPoint):
    
    for i in range(len(xData)):
        if interpolationPoint >= xData[i]:
            n = i

    b_0 = yData[n]
    b_1 = (yData[n+1] - yData[n]) / (xData[n+1]-xData[n])
    
    y = b_0 + b_1*(interpolationPoint-xData[n])

    return y


xData, yData = read_files("data3.txt")

print("My interpolation function: ",myInterpolationFunc(xData,yData,0.97))
y_interp = interp1d(xData, yData)
print("1d:",y_interp(0.97))

plt.figure(figsize = (12, 8))
plt.xlabel("xData")
plt.ylabel("yData")
plt.plot(xData, yData, 'bo')
plt.plot(xData, yData)