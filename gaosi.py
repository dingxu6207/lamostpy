# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 20:45:48 2019

@author: dingxu
"""

import numpy as np
import matplotlib.pyplot as plt

#生成数据
x = np.arange(0,6,0.1)
y = 1 - np.exp(-((x-3)**2)/(2*6)) + 0.4

def fun(x):
    m  = 1 - np.exp(-((x-3)**2)/(2*6)) + 0.4
    return m
plt.plot(x,y)

matrix = [0 for i in range(7)]

m0 = fun(0)
i = 0
for i in range(0,7):
    print(fun(i))
    matrix[i] = fun(i)

print(matrix)