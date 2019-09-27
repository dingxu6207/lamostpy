# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 10:10:09 2019

@author: dingxu
"""

from astropy.io import fits
import matplotlib.pyplot as plt
from scipy import signal



hdulist = fits.open('I:/dingxuhardware/lamostdr5/dr5-v1/fits/HD064049N515841V01/spec-56972-HD064049N515841V01_sp07-008.fits.gz')
hdulist.info()
print(hdulist[0].header)

flux = hdulist[0].data[0]
wave = hdulist[0].data[2]


zhongzhidata = signal.medfilt(flux,79)

guiyidata = flux/(zhongzhidata+0.000001)

#plt.plot(wavelength[2578:2591],guiyidata[2578:2591])
guiyiflux =  guiyidata[2570:2600]
wavelength = wave[2570:2600]
lenflux = flux[2570:2600]
guiyizhongzhi = zhongzhidata[2570:2600]

plt.figure(0)
plt.plot(wave,flux)
plt.plot(wave,zhongzhidata)
plt.legend()

plt.figure(1)
plt.plot(wavelength,guiyiflux)

plt.show()





