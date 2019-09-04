# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:36:40 2019

@author: dingxu
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy import signal

hdulist = fits.open('E:\pytest\B6202\spec-55862-B6202_sp09-153.fits')
hdulist.info()
print(hdulist[0].header)

flux = hdulist[0].data[0]
wavelength = hdulist[0].data[2]
Z = hdulist[0].header['Z']

zhongzhidata = signal.medfilt(flux,79)

guiyidata = flux/(zhongzhidata+0.000001)

Liwavelength = wavelength[2580:2589]
Liflux = guiyidata[2580:2589]



def plotxy(Liwavelength,Liflux):
    plt.plot(Liwavelength, Liflux)
    

a = [0,1,2,3,4]

def gaussian(x,a,b,c): 
    return  c - a*np.exp(-((x-2)**2)/(2*b))  

b =  Liflux



if (Z > -0.000184) and (Z < 0.000276):
        if ((b[4] <= b[3]) and (b[3] <= b[2]) and (b[4] <= b[5])and (b[5] <= b[6])):
            xuanb = (b[2],b[3],b[4],b[5],b[6])
            popt, pcov = curve_fit(gaussian, a, xuanb)
            
if (Z < -0.000184):
        if ((b[3] <= b[2]) and (b[2] <= b[1]) and (b[3] <= b[4])and (b[4] <= b[5])): 
            xuanb = (b[1],b[2],b[3],b[4],b[5])
            popt, pcov = curve_fit(gaussian, a, xuanb)    
            
if (Z > 0.000276):
    if ((b[5] <= b[4]) and (b[4] <= b[3]) and (b[5] <= b[6])and (b[6] <= b[7])):
        xuanb = (b[3],b[4],b[5],b[6],b[7])
        popt, pcov = curve_fit(gaussian, a, xuanb)             

y2 = [gaussian(i, popt[0],popt[1],popt[2]) for i in a]


print (popt)

plotxy(a,xuanb)
#plotxy(Liwavelength,pinghuaflux)
plotxy(a,y2)
plt.legend()
plt.show()