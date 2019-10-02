# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 06:03:14 2019

@author: dingxu
"""

RA = 186.705526
DEC = 29.139984

fenzhong = RA*4
xiaoshi = fenzhong/60
print('RA')
hh = int(xiaoshi)
print(hh)
m0 = xiaoshi - hh
m1 = m0*60
m2 = int(m1)
print(m2)

n0 = m1 - m2
n1 = n0 * 60
print(n1)

print('DEC')
dd = int(DEC)
print(dd)
n0 = DEC - dd
n1 = n0 * 60
nn = int(n1)
print(nn)
n2 = n1 -nn
ss = n2*60
print(ss)
