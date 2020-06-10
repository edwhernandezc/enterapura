# -*- coding: utf-8 -*-
"""
Editor de Spyder
"""

from cvxopt.modeling import *

x = variable()
y = variable()
v = variable()

r1 = 8000*x + 6000*y + 12000*v <= 20000
r2 = 7000*x + 4000*y + 8000*v <= 16000 

r3 = x >= 0
r4 = y >= 0
r5 = v >= 0

lp1 = op(25000*x + 18000*y + 31000*v,[r1,r2,r3,r4,r5])

lp1.solve()
lp1.status
print("Valor de la funcion objetivo es : ", lp1.objective.value())
print("Valor de x: ",x.value)
print("Valor de y: ",y.value)
print("Valor de v: ",v.value)