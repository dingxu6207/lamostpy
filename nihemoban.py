# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 20:36:40 2019

@author: dingxu
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

hdulist = fits.open('E:\pytest\B6202\spec-55862-B6202_sp01-052.fits')
hdulist.info()
print(hdulist[0].header)

flux = hdulist[0].data[0]
wavelength = hdulist[0].data[2]

maxflux = max(flux)
minflux = min(flux)
fenmu = maxflux - minflux
fenzi = flux - minflux
lastflux = fenzi/fenmu


Liwavelength = wavelength[2580:2587]
Liflux = lastflux[2580:2587]

def plotxy(Liwavelength,Liflux):
    plt.plot(Liwavelength, Liflux)
    
plotxy(Liwavelength,Liflux)

def gaussian(x,a,b,c):    
    return  1 - a*np.exp(-((x-6707)**2)/(2*b)) + c

popt, pcov = curve_fit(gaussian, Liwavelength, Liflux)

y2 = [gaussian(i, popt[0],popt[1],popt[2]) for i in Liwavelength]

print(popt[0])
print(popt[1])
print(popt[2])

plotxy(Liwavelength,y2)
