#Problema Quemo Chemical Company 
from cvxopt import glpk
from cvxopt.base import matrix as m
 
c = m([-25000., -18000., -31000.]) #Matriz con los valores de la funcion objetivo
A = m([[8000., 7000.], [6000., 4000.], [12000., 8000.]]) #Valores de las variables de las restricciones
b = m([20000., 16000.]) #Valores independientes de las restricciones

intVars = range(3) #Especificamos que las 3 variables son enteras
binVars = range(3) #Especificamos que las 3 variables son binarias

sol = glpk.ilp(c, A, b, I=set(intVars), B=set(binVars))
print('Los valores óptimos de las variables son:\n{0}'.format(sol[1]))  #Si se encuantra valores optimos se muestran
if sol[0]=='optimal':
 
    print('El valor óptimo es:  {0}'.format((-c.T*sol[1])[0]))
# El valor óptimo debemos transponerlo y cambiarle el signo, estamos maximizando.
 
else:
 
    print('El problema no devolvió una solución óptima. El estado del solucionador fue {0}'.format(sol[0]))  #Si no encuentra dice que no se encontro