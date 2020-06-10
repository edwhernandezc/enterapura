# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:54:12 2020

@author: nikob
"""

from scipy.optimize import linprog

fobj=[25000,18000,31000]

A = [[8000,6000,12000],[7000,4000,8000]]
B = [20000,16000]

res = linprog(fobj, A,B, bounds = (0, None), method='interior-point')

print ("Valor Optimo: ", res.fun, "\nX: ",res.x)
print(res)