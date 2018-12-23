# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 21:57:12 2018

@author: dingxu
"""
import os
import glob
from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.optimize import curve_fit


curentpath = os.getcwd()
#help('os.chdir')
os.chdir('E:\pytest\B6202')
curentpath = os.getcwd()
print(curentpath)


def eachFile(filepath):
    """ 读取文件夹下面的所有文件 的路径"""
    pathDir = os.listdir(filepath)
    file_path_list = list()
    for allDir in pathDir:
        child = os.path.join('%s%s' % (filepath, allDir))
        file_path_list.append(child)
    return file_path_list


path = curentpath
for infile in glob.glob(os.path.join(path, '*.gz')):
     os.remove(infile)
   
for infile in glob.glob(os.path.join(path, '*.fits')):
    print(infile)        
    hdulist = fits.open(infile)
    #hdulist.info()
    
    #print(hdulist[0].header)
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
    a = x[2581:2586]

    b = []
    b = y[2581:2586]


    maxfuc = max(b)

    def gaussian(x,*param):    
        return maxfuc-param[0]*np.exp(-np.power(x - param[1], 2.) / (2 * np.power(param[2], 2.)))
    try:
        popt,pcov = curve_fit(gaussian,a,b,p0=[maxfuc,6707,2]) 
    except RuntimeError:
        pass
    else:
        modc = gaussian(a,*popt)
        w=popt[2]*math.sqrt(2)
        sigma = w/2
        FWHM = sigma*2.355
        print("w=",w)
    
        def R2_fun(y, y_forecast):
            y_mean=np.mean(y)
            return 1 - (np.sum((y_forecast - y) ** 2)) / (np.sum((y - y_mean) ** 2))
    
        R2 = R2_fun(b,modc)
        print("R2=",R2)
    '''   
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
    
       
    
    

