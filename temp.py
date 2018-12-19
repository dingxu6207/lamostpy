# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from astropy.io import fits
import matplotlib.pyplot as plt
#import numpy as np


hdulist = fits.open('E:/pytest/fits/spec-57733-EG000006N255311B01_sp01-001.fits')
hdulist.info()
print(hdulist[0].header)
print(hdulist[0].header['RA'])
print(hdulist[0].header['DEC'])
#plt.plot(hdulist[0].data[2],hdulist[0].data[0])

y = hdulist[0].data[0]
#print(y)
print(len(y))
x = hdulist[0].data[2]
print(x)
plt.plot(x[2580:2587],y[2580:2587])
