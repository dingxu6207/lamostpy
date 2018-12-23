# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit


hdulist = fits.open('E:/pytest/fits/spec-55860-B6001_sp01-002.fits/spec-55860-B6001_sp01-002.fits')
hdulist.info()
print(hdulist[0].header)
print(hdulist[0].header['RA'])
print(hdulist[0].header['DEC'])
#plt.plot(hdulist[0].data[2],hdulist[0].data[0])

y = hdulist[0].data[0]
#print(y)
#print(len(y))
x = hdulist[0].data[2]
#print(x)
#plt.plot(x[2582:2587],y[2582:2587])
a = []
a = x[2579:2589]

b = []
b = y[2579:2589]


maxfuc = max(b)

def gaussian(x,*param):    
    return maxfuc-param[0]*np.exp(-np.power(x - param[1], 2.) / (2 * np.power(param[2], 2.)))

'''
def gaussian(x,*param):
    return -1*param[0]*np.exp(-np.power(x - param[2], 2.) / (2 * np.power(param[4], 2.)))+\
          -1*param[1]*np.exp(-np.power(x - param[3], 2.) / (2 * np.power(param[5], 2.)))
'''

#popt,pcov = curve_fit(gaussian,x,y,p0=[195,6711,8,8,6713,4])
popt,pcov = curve_fit(gaussian,a,b,p0=[maxfuc,6707,2])
#help(curve_fit)
modc = gaussian(a,*popt)
print (popt)
#print (pcov)
fig = plt.figure()
ax0 = fig.add_subplot(3,1,1) 
ax0.plot(a,b,'b',label='data')

ax1 = fig.add_subplot(3,1,2) 
ax1.plot(a,modc,'r',label='fit')

ax2 = fig.add_subplot(3,1,3) 
ax2.plot(a,b,'b+:',label='data')
ax2.plot(a,modc,'ro:',label='fit')
ax2.legend()
'''
ax3 = fig.add_subplot(4,1,4) 
ax3.plot(x,y,'g',label='data')
'''
w = popt[2]*math.sqrt(2)
sigma = w/2
FWHM = sigma*2.355
print("w=",w)

'''variances = list(map(lambda x,y : (x-y)**2, b, modc))
#print(variances)
variance = np.sum(variances)  
RMSE =  np.sqrt(variance/len(a))
print(RMSE)
'''

def R2_fun(y, y_forecast):
    y_mean=np.mean(y)
    return 1 - (np.sum((y_forecast - y) ** 2)) / (np.sum((y - y_mean) ** 2))


R2 = R2_fun(b,modc)
print("R2=",R2)

















