#Problema Proyectos a invertir
from cvxopt import glpk
from cvxopt.base import matrix as m
 
c = m([-46356337., -37927912.,-4214212.]) #Matriz con los valores de la funcion objetivo
A = m([[42134625.], [25280775.], [16853850.]]) #Valores de las variables de las restricciones
b = m([42134625.]) #Valores independientes de las restricciones

intVars = range(3) #Especificamos que las 3 variables son enteras
binVars = range(3) #Especificamos que las 3 variables son binarias

sol = glpk.ilp(c, A, b, I=set(intVars), B=set(binVars))
print('Los valores óptimos de las variables son:\n{0}'.format(sol[1]))  #Si se encuantra valores optimos se muestran
if sol[0]=='optimal':
 
    print('El valor óptimo es:  ${0} COP'.format((-c.T*sol[1])[0]))
# El valor óptimo debemos transponerlo y cambiarle el signo, estamos maximizando.
 
else:
 
    print('El problema no devolvió una solución óptima. El estado del solucionador fue {0}'.format(sol[0])) #Si no encuentra dice que no se encontro