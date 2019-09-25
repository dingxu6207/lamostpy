# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:10:09 2019

@author: dingxu
"""

from astropy.io import fits
import matplotlib.pyplot as plt
from scipy import signal



hdulist = fits.open('E:/pytest/spec-55918-B5591804_sp02-030.fits.gz')
hdulist.info()
print(hdulist[0].header)

flux = hdulist[0].data[0]
wave = hdulist[0].data[2]


zhongzhidata = signal.medfilt(flux,79)

guiyidata = flux/(zhongzhidata+0.000001)

#plt.plot(wavelength[2578:2591],guiyidata[2578:2591])
guiyiflux =  guiyidata[2576:2593]
wavelength = wave[2576:2593]
lenflux = flux[2576:2593]

plt.plot(wavelength,guiyiflux)

plt.legend()

plt.show()





