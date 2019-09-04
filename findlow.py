# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:45:23 2019

@author: dingxu
"""
import os
from astropy.io import fits
import glob
import xlwt
from scipy import signal
from scipy.optimize import curve_fit
import numpy as np

'''
zuoxian = 2582
youxian = 2587
'''
zuoxian = 2580
youxian = 2589

os.chdir('E:\pytest\B6202')
curentpath = os.getcwd()
print(curentpath)
path = curentpath

def gaussian(x,a,b,c):    
    return  c - a*np.exp(-((x-2)**2)/(2*b)) 

hangcount = 0
#excel表
workbook = xlwt.Workbook(encoding='utf-8')
data_sheet = workbook.add_sheet('demo',cell_overwrite_ok = True)
for infile in glob.glob(os.path.join(path, '*.fits')):
    phdulist = fits.open(infile)
    flux = phdulist[0].data[0]
    Liwave = phdulist[0].data[2]
    zhongzhidata = signal.medfilt(flux,79)
    guiyidata = flux/(zhongzhidata+0.00000001)
    data = guiyidata[zuoxian:youxian]
    Liwavelength = Liwave[zuoxian:youxian]
    
    data_sheet.write(0, 0, 'file')
    data_sheet.write(0, 1, 'RA')
    data_sheet.write(0, 2, 'DEC')
    data_sheet.write(0, 3, 'SUBCLASS')
    data_sheet.write(0, 4, 'Z') 
    data_sheet.write(0, 5, 'sigma') 
    data_sheet.write(0, 6, 'minb')
    
    a = [0,1,2,3,4]
    b = data
    #b[2] < b[1] b[1] < b[0] b[2] < b[3]  b[3] < b[4] 
    Z = phdulist[0].header['Z']
    if (Z > -0.000184) and (Z < 0.000276):
        if ((b[4] <= b[3]) and (b[3] <= b[2]) and (b[4] <= b[5])and (b[5] <= b[6])):           
            hangcount = hangcount + 1 
            xuanb = (b[2],b[3],b[4],b[5],b[6])            
            popt, pcov = curve_fit(gaussian, a, xuanb)
            RA = phdulist[0].header['RA']
            DEC = phdulist[0].header['DEC']
            SUBCLASS = phdulist[0].header['SUBCLASS']
            data_sheet.write(hangcount, 0, infile)
            data_sheet.write(hangcount, 1, RA)
            data_sheet.write(hangcount, 2, DEC)
            data_sheet.write(hangcount, 3, SUBCLASS)
            data_sheet.write(hangcount, 4, Z) 
            data_sheet.write(hangcount, 5, popt[1]) 
            data_sheet.write(hangcount, 6, b[4])
            
    if (Z < -0.000184):
        if ((b[3] <= b[2]) and (b[2] <= b[1]) and (b[3] <= b[4])and (b[4] <= b[5])):
            hangcount = hangcount + 1  
            xuanb = (b[1],b[2],b[3],b[4],b[5])
            popt, pcov = curve_fit(gaussian, a, xuanb)
            RA = phdulist[0].header['RA']
            DEC = phdulist[0].header['DEC']
            SUBCLASS = phdulist[0].header['SUBCLASS']
            data_sheet.write(hangcount, 0, infile)
            data_sheet.write(hangcount, 1, RA)
            data_sheet.write(hangcount, 2, DEC)
            data_sheet.write(hangcount, 3, SUBCLASS)
            data_sheet.write(hangcount, 4, Z)
            data_sheet.write(hangcount, 5, popt[1])
            data_sheet.write(hangcount, 6, b[3])
            
    if (Z > 0.000276):
        if ((b[5] <= b[4]) and (b[4] <= b[3]) and (b[5] <= b[6])and (b[6] <= b[7])):
            hangcount = hangcount + 1
            xuanb = (b[3],b[4],b[5],b[6],b[7])
            popt, pcov = curve_fit(gaussian, a, xuanb)
            RA = phdulist[0].header['RA']
            DEC = phdulist[0].header['DEC']
            SUBCLASS = phdulist[0].header['SUBCLASS']
            data_sheet.write(hangcount, 0, infile)
            data_sheet.write(hangcount, 1, RA)
            data_sheet.write(hangcount, 2, DEC)
            data_sheet.write(hangcount, 3, SUBCLASS)
            data_sheet.write(hangcount, 4, Z) 
            data_sheet.write(hangcount, 5, popt[1])
            data_sheet.write(hangcount, 6, b[5])
keepfilename =  'E:/' + path[-5:] + '.xls'
workbook.save(keepfilename)          
            
        

    




