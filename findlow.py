# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 20:45:23 2019

@author: dingxu
"""
import os
from astropy.io import fits
import xlwt
from scipy import signal

'''
zuoxian = 2582
youxian = 2587
'''
zuoxian = 2580
youxian = 2589

#I:/dingxuhardware/lamostdr5/dr5-v1/fits
os.chdir('E:/pytest/data')
curentpath = os.getcwd()
print(curentpath)
path = curentpath

hangcount = 0
#excel表
sheet = 0
strsheet =  str(sheet)
workbook = xlwt.Workbook(encoding='utf-8')
data_sheet = workbook.add_sheet(strsheet,cell_overwrite_ok = True)

for root, dirs, files in os.walk(path):
   for file in files:
       strfile = os.path.join(root, file)
       
       if (strfile[-3:] == '.gz'):
           fitstrfile = strfile.replace(".gz", "")
          # phdulist = fits.open(fitstrfile)
           phdulist = fits.open(strfile)
           flux = phdulist[0].data[0]
           Liwave = phdulist[0].data[2]
           zhongzhidata = signal.medfilt(flux,79)
           guiyidata = flux/(zhongzhidata+0.00000001)
           data = guiyidata[zuoxian:youxian]
           Liwavelength = Liwave[zuoxian:youxian]
    
           data_sheet.write(0, 0, 'file')
           data_sheet.write(0, 1, 'RA')
           data_sheet.write(0, 2, 'DEC')
           data_sheet.write(0, 3, 'SUBCLASS')
           data_sheet.write(0, 4, 'Z') 
           data_sheet.write(0, 5, 'sigma') 
           data_sheet.write(0, 6, 'sum')
           data_sheet.write(0, 7, 'zuocha')
           data_sheet.write(0, 8, 'youcha')
           
           b = data
           #b[2] < b[1] b[1] < b[0] b[2] < b[3]  b[3] < b[4] 
           Z = phdulist[0].header['Z']
           if (Z > -0.000184) and (Z < 0.000276):
               if ((b[4] < b[3]) and (b[3] <= b[2]) and (b[4] < b[5])and (b[5] <= b[6])):  
                   qiusum = b[2]+b[3]+b[4]+b[5]+b[6]                               
                   RA = phdulist[0].header['RA']
                   DEC = phdulist[0].header['DEC']
                   SUBCLASS = phdulist[0].header['SUBCLASS']   
                   
                   if (b[4] < 0.8):
                       hangcount = hangcount + 1 
                       data_sheet.write(hangcount, 0, fitstrfile)
                       data_sheet.write(hangcount, 1, RA)
                       data_sheet.write(hangcount, 2, DEC)
                       data_sheet.write(hangcount, 3, SUBCLASS)
                       data_sheet.write(hangcount, 4, Z) 
                       data_sheet.write(hangcount, 5, b[4])
                       data_sheet.write(hangcount, 6, qiusum)
                       data_sheet.write(hangcount, 7, (-1 if(b[2] > b[1]) else 1))
                       data_sheet.write(hangcount, 8, (-1 if(b[6] > b[7]) else 1))
                       print('write'+strfile+' is ok!') 
            
            
           if (Z < -0.000184):
               if ((b[3] < b[2]) and (b[2] <= b[1]) and (b[3] < b[4])and (b[4] <= b[5])):
                   qiusum = b[2]+b[3]+b[4]+b[5]+b[1]
                   RA = phdulist[0].header['RA']
                   DEC = phdulist[0].header['DEC']
                   SUBCLASS = phdulist[0].header['SUBCLASS']
                   
                   if (b[3] < 0.8):
                       hangcount = hangcount + 1 
                       data_sheet.write(hangcount, 0, fitstrfile)
                       data_sheet.write(hangcount, 1, RA)
                       data_sheet.write(hangcount, 2, DEC)
                       data_sheet.write(hangcount, 3, SUBCLASS)
                       data_sheet.write(hangcount, 4, Z)
                       data_sheet.write(hangcount, 5, b[3])
                       data_sheet.write(hangcount, 6, qiusum)
                       data_sheet.write(hangcount, 7, (-1 if(b[1] > b[0]) else 1))
                       data_sheet.write(hangcount, 8, (-1 if(b[5] > b[6]) else 1))
                       print('write'+strfile+' is ok!') 
            
           if (Z > 0.000276):
               if ((b[5] < b[4]) and (b[4] <= b[3]) and (b[5] < b[6])and (b[6] <= b[7])):
                   qiusum = b[7]+b[3]+b[4]+b[5]+b[6]          
                   RA = phdulist[0].header['RA']
                   DEC = phdulist[0].header['DEC']
                   SUBCLASS = phdulist[0].header['SUBCLASS']
                   
                   if (b[5] < 0.8):
                       hangcount = hangcount + 1 
                       data_sheet.write(hangcount, 0, fitstrfile)
                       data_sheet.write(hangcount, 1, RA)
                       data_sheet.write(hangcount, 2, DEC)
                       data_sheet.write(hangcount, 3, SUBCLASS)
                       data_sheet.write(hangcount, 4, Z) 
                       data_sheet.write(hangcount, 5, b[5])
                       data_sheet.write(hangcount, 6, qiusum)
                       data_sheet.write(hangcount, 7, (-1 if(b[3] > b[2]) else 1))
                       data_sheet.write(hangcount, 8, (-1 if(b[7] > b[8]) else 1))
                       print('write'+strfile+' is ok!') 

           if (hangcount == 20):
              hangcount = 0
              sheet = sheet + 1
              strsheet = str(sheet)
              data_sheet = workbook.add_sheet(strsheet,cell_overwrite_ok = True)
  
keepfilename =  'E:/lamost.xls'
workbook.save(keepfilename)          
            
        

    



 
