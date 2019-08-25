# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 17:11:10 2019

@author: dingxu
"""


from astropy.io import fits
import matplotlib.pyplot as plt


hdulist = fits.open('E:\pytest\B6202\spec-55862-B6202_sp13-215.fits')
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
    plt.show()

plotxy(Liwavelength,Liflux)

print(Liflux)