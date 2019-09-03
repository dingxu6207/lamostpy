# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:10:09 2019

@author: dingxu
"""

from astropy.io import fits
import matplotlib.pyplot as plt
from scipy import signal
from scipy.optimize import curve_fit


hdulist = fits.open('E:\pytest\B6202\spec-55862-B6202_sp01-052.fits')
hdulist.info()
print(hdulist[0].header)

flux = hdulist[0].data[0]
wavelength = hdulist[0].data[2]

b, a = signal.butter(8, 0.02, 'lowpass')   #配置滤波器 8 表示滤波器的阶数
filtedData = signal.filtfilt(b, a, flux)  #data为要过滤的信号

zhongzhidata = signal.medfilt(flux,79)

def duoxiangshi(x,a,b,c,d,e):    
    return  a + b*x + c*(x**2)+ d*(x**3)+ e*(x**4)

popt, pcov = curve_fit(duoxiangshi, wavelength, filtedData)

y2 = [duoxiangshi(i, popt[0],popt[1],popt[2],popt[3],popt[4]) for i in wavelength]




print(popt[0])
print(popt[1])
print(popt[2])
print(popt[3])


guiyidata = flux/zhongzhidata
#plt.plot(wavelength,guiyidata)

plt.plot(wavelength,flux)

plt.plot(wavelength,zhongzhidata)



plt.legend()

plt.show()



'''
guiyidata = flux/zhongzhidata

plt.subplot(131)
plt.plot(wavelength,flux)
plt.subplot(132)
plt.plot(wavelength,zhongzhidata)
plt.subplot(133)
plt.plot(wavelength,guiyidata)
'''



