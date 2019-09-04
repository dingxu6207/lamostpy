# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:10:09 2019

@author: dingxu
"""

from astropy.io import fits
import matplotlib.pyplot as plt
from scipy import signal



hdulist = fits.open('E:\pytest\B6202\spec-55862-B6202_sp16-043.fits')
hdulist.info()
print(hdulist[0].header)

flux = hdulist[0].data[0]
wavelength = hdulist[0].data[2]


zhongzhidata = signal.medfilt(flux,79)

guiyidata = flux/(zhongzhidata+0.000001)

#plt.plot(wavelength[2578:2591],guiyidata[2578:2591])
flux =  guiyidata[2580:2589]
wavelength = wavelength[2580:2589]



plt.plot(wavelength,flux)

plt.legend()

plt.show()





