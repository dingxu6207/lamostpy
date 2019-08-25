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

hdulist = fits.open('E:/pytest/B6202/spec-55862-B6202_sp01-001.fits')
hdulist.info()
#print(hdulist[0].header)

flux = hdulist[0].data[0]
wavelength = hdulist[0].data[2]

maxflux = max(flux)
minflux = min(flux)
fenmu = maxflux - minflux
fenzi = flux - minflux
lastflux = fenzi/fenmu

zuoxian = 2581
youxian = 2586
Liwavelength = wavelength[zuoxian:youxian]
Liflux = lastflux[zuoxian:youxian]

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

#excel表
workbook = xlwt.Workbook(encoding='utf-8')
data_sheet = workbook.add_sheet('demo',cell_overwrite_ok = True)
    
os.chdir('E:\pytest\B6202')
curentpath = os.getcwd()
print(curentpath)
path = curentpath
hangcount = 0;
for infile in glob.glob(os.path.join(path, '*.fits')):
    #print(infile) 
    phdulist = fits.open(infile)
    y = phdulist[0].data[0]
    y = guiyihua(y)
    x = phdulist[0].data[2]
    a = x[zuoxian:youxian]
    b = y[zuoxian:youxian]  
    cha = b - Liflux
    pingfang = cha**2
    type(pingfang)
    suma = sum(pingfang)
    sqrta = math.sqrt(suma)
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