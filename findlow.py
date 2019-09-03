# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:45:23 2019

@author: dingxu
"""
import os
from astropy.io import fits
import glob
import xlwt
import numpy as np
'''
zuoxian = 2582
youxian = 2587
'''
zuoxian = 2578
youxian = 2591

os.chdir('E:\pytest\B6202')
curentpath = os.getcwd()
print(curentpath)
path = curentpath

#归一化代码
guiyidata = np.zeros(13)
def guiyihua(fluxdata):
    maxdata = max(fluxdata)
    mindata = min(fluxdata)
    fenmu = maxdata - mindata
    fenzi = fluxdata - mindata
    if fenmu > 0:
       guiyidata = fenzi/fenmu
    else:
        guiyidata = np.zeros(13)
    return guiyidata

hangcount = 0
#excel表
workbook = xlwt.Workbook(encoding='utf-8')
data_sheet = workbook.add_sheet('demo',cell_overwrite_ok = True)
for infile in glob.glob(os.path.join(path, '*.fits')):
    phdulist = fits.open(infile)
    y = phdulist[0].data[0]
    data = y[zuoxian:youxian]
    y = guiyihua(data)
    #x = phdulist[0].data[2]
    #a = x[zuoxian:youxian]
    #b = y[zuoxian:youxian] 
    b = y
    #b[2] < b[1] b[1] < b[0] b[2] < b[3]  b[3] < b[4] 
    Z = phdulist[0].header['Z']
    if (Z > -0.000184) and (Z < 0.000276):
        if ((b[6] <= b[5]) and (b[5] <= b[4]) and (b[6] <= b[7])and (b[7] <= b[8])):
            hangcount = hangcount + 1    
            RA = phdulist[0].header['RA']
            DEC = phdulist[0].header['DEC']
            SUBCLASS = phdulist[0].header['SUBCLASS']
            data_sheet.write(hangcount, 0, infile)
            data_sheet.write(hangcount, 1, RA)
            data_sheet.write(hangcount, 2, DEC)
            data_sheet.write(hangcount, 3, SUBCLASS)
            data_sheet.write(hangcount, 4, Z) 
            
    if (Z < -0.000184):
        if ((b[5] <= b[4]) and (b[4] <= b[3]) and (b[5] <= b[6])and (b[6] <= b[7])):
            hangcount = hangcount + 1    
            RA = phdulist[0].header['RA']
            DEC = phdulist[0].header['DEC']
            SUBCLASS = phdulist[0].header['SUBCLASS']
            data_sheet.write(hangcount, 0, infile)
            data_sheet.write(hangcount, 1, RA)
            data_sheet.write(hangcount, 2, DEC)
            data_sheet.write(hangcount, 3, SUBCLASS)
            data_sheet.write(hangcount, 4, Z) 
            
    if (Z > 0.000276):
        if ((b[7] <= b[6]) and (b[6] <= b[5]) and (b[7] <= b[8])and (b[8] <= b[9])):
            hangcount = hangcount + 1    
            RA = phdulist[0].header['RA']
            DEC = phdulist[0].header['DEC']
            SUBCLASS = phdulist[0].header['SUBCLASS']
            data_sheet.write(hangcount, 0, infile)
            data_sheet.write(hangcount, 1, RA)
            data_sheet.write(hangcount, 2, DEC)
            data_sheet.write(hangcount, 3, SUBCLASS)
            data_sheet.write(hangcount, 4, Z) 
    
workbook.save('E:/B6.xls')          
            
        

    




