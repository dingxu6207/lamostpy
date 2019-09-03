# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:07:33 2019

@author: dingxu
"""
import numpy as np
import matplotlib.pyplot as plt

matrix0 = [0 for i in range(7)]

#生成模板函数
def fun(x,a,b,c):
    m  = 1 - a*np.exp(-((x-3)**2)/(2*b)) + c
    return m

i = 0
for i in range(0,7):
    matrix0[i] = fun(i,0.03,3.28,-0.2)
    
plt.plot(matrix0)  