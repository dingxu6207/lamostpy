# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:25:42 2019

@author: dingxu
"""

import os
from astropy.io import fits
import matplotlib.pyplot as plt
import glob
import math
import xlwt
import numpy as np


zuoxian = 2582
youxian = 2587


matrix0 = [0 for i in range(5)]
matrix1 = [0 for i in range(5)]
matrix2 = [0 for i in range(5)]

#生成模板函数
def fun(x,a,b,c):
    m  = 1 - a*np.exp(-((x-2)**2)/(2*b)) + c
    return m

i = 0
for i in range(0,5):
    matrix0[i] = fun(i,0.0459,14.02,-0.30)
    matrix1[i] = fun(i,0.0459,14.02,-0.30)
    matrix2[i] = fun(i,0.0459,14.02,-0.30)

Liflux0 = matrix0
Liflux1 = matrix1
Liflux2 = matrix2

def plotxy(Liwavelength,Liflux):
    plt.plot(Liwavelength, Liflux)
    plt.show()


#归一化代码
def guiyihua(fluxdata):
    maxdata = max(fluxdata)
    mindata = min(fluxdata)
    fenmu = maxdata - mindata
    fenzi = fluxdata - mindata
    guiyidata = fenzi/fenmu
    return guiyidata

#最近邻居求解
def zuijinlin(b,Liflux):
    cha = b - Liflux
    pingfang = cha**2
    suma = sum(pingfang)
    sqrta = math.sqrt(suma)
    return sqrta

#excel表
workbook = xlwt.Workbook(encoding='utf-8')
data_sheet = workbook.add_sheet('demo',cell_overwrite_ok = True)
    
os.chdir('E:\pytest\B6202')
curentpath = os.getcwd()
print(curentpath)
path = curentpath
hangcount = 0;
sqrtlist = [0 for i in range(3)]
for infile in glob.glob(os.path.join(path, '*.fits')):
    #print(infile) 
    phdulist = fits.open(infile)
    y = phdulist[0].data[0]
    y = guiyihua(y)
    x = phdulist[0].data[2]
    a = x[zuoxian:youxian]
    b = y[zuoxian:youxian]  
    
    sqrt0 = zuijinlin(b,Liflux0)
    sqrt1 = zuijinlin(b,Liflux1)
    sqrt2 = zuijinlin(b,Liflux2)
    sqrtlist = [sqrt0,sqrt1,sqrt2]
    sqrta = min(sqrtlist)
    #print(sqrta)
    hangcount = hangcount + 1
    
    RA = phdulist[0].header['RA']
    DEC = phdulist[0].header['DEC']
    SUBCLASS = phdulist[0].header['SUBCLASS']

    data_sheet.write(hangcount, 0, infile)
    data_sheet.write(hangcount, 1, RA)
    data_sheet.write(hangcount, 2, DEC)
    data_sheet.write(hangcount, 3, SUBCLASS)
    data_sheet.write(hangcount, 4, sqrta)

workbook.save('E:/B6.xls')    