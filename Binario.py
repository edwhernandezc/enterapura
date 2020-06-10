# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 13:23:38 2020

@author: nikob
"""


#Por Binarios
from cvxopt import glpk
from cvxopt.base import matrix as m
 
c = m([-25000., -18000., 31000.])
A = m([[8000., 7000.], [6000., 4000.], [12000., 8000.]])
b = m([20000., 16000.])

intVars = range(3) #Especificamos que las 5 variables son enteras
binVars = range(3) #Especificamos que las 5 variables son binarias

sol = glpk.ilp(c, A, b, I=set(intVars), B=set(binVars))
print('Los valores óptimos de las variables son:\n{0}'.format(sol[1]))
if sol[0]=='optimal':
 
    print('El valor óptimo es:  {0}'.format((-c.T*sol[1])[0]))
# El valor óptimo debemos transponerlo y cambiarle el signo, estamos maximizando.
 
else:
 
    print('El problema no devolvió una solución óptima. El estado del solucionador fue {0}'.format(sol[0]))