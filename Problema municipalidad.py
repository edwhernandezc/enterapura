#Problema municipalidad
from cvxopt import glpk
from cvxopt.base import matrix as m
 
c = m([-842628., -421314.,-631971.,-1263943.,-1078564.,-1137548.,-758365.])
A = m([[1., 1.,1.,0.,0.,0.,1.], [0., 1.,0.,1.,0.,0.,0.], [0., 0.,1.,0.,1.,0.,0.],[0.,0.,0.,1.,1.,1.,0.]
       ,[1., 1., 1., 1., 0., 1., 1.], [0., 0., 0., 0., 1., 1., 1.], [1., 1., 0., 0., 0., 0., 1.]])
b = m([1., 1.,1.,1.,1.,1,1.])

intVars = range(7) #Especificamos que las 5 variables son enteras
binVars = range(7) #Especificamos que las 5 variables son binarias

sol = glpk.ilp(c, A, b, I=set(intVars), B=set(binVars))
print('Los valores óptimos de las variables son:\n{0}'.format(sol[1]))
if sol[0]=='optimal':
 
    print('El valor óptimo es:  ${0} COP'.format((-c.T*sol[1])[0]))
# El valor óptimo debemos transponerlo y cambiarle el signo, estamos maximizando.
 
else:
 
    print('El problema no devolvió una solución óptima. El estado del solucionador fue {0}'.format(sol[0]))