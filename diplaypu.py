# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:11:10 2019

@author: dingxu
"""


from astropy.io import fits
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

hdulist = fits.open('E:\pytest\B6202\spec-55862-B6202_sp01-052.fits')
hdulist.info()
print(hdulist[0].header)

flux = hdulist[0].data[0]
wavelength = hdulist[0].data[2]

wavelengthduan = wavelength[2578:2591]
fluxduan = flux[2578:2591]
#plt.plot(wavelengthduan,fluxduan)


def duoxiangshi(x,a,b,c,d,e):    
    return  a + b*x + c*(x**2)+ d*(x**3)+ e*(x**4)

popt, pcov = curve_fit(duoxiangshi, wavelengthduan, fluxduan)

y2 = [duoxiangshi(i, popt[0],popt[1],popt[2],popt[3],popt[4]) for i in wavelengthduan]


print(popt[0])
print(popt[1])
print(popt[2])
print(popt[3])

plt.plot(wavelengthduan,y2)
plt.plot(wavelengthduan,fluxduan)
plt.legend()
