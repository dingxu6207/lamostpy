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

'''
4 0.3  (0.9753475326416503, 0.6934693402873666, 0.41750309741540453, 0.3, 0.41750309741540453, 0.6934693402873666, 0.9753475326416503)
5 0.4  [0.9934303402594009, 0.7296799539643607, 0.4951625819640405, 0.4, 0.4951625819640405, 0.7296799539643607, 0.9934303402594009]
7 0.5  [0.9742119755742202, 0.748522706924714, 0.5689372202959773, 0.5, 0.5689372202959773, 0.748522706924714, 0.9742119755742202]
'''