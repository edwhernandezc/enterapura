# Entera pura

## Integrantes 
- EDWIN HERNÁNDEZ CABRERA 20152020013
- NICOLÁS BERMÚDEZ 2016102004
- HANER AVELLA LEÓN 20161020071
## RESUMEN

Dentro de los métodos para la optimización y solución de problemas está la programación entera. Las variables, en este modelo de decisión, toman valores restringidos a números enteros, ya que por ejemplo en la optimización de una planta eléctrica no se pueden apagar y/o agregar un generador y medio; la programación entera se divide en dos, Entera mixta (PEM) y Entera Pura (PEP), esta última es en la que nos enfocaremos. 

A través de este documento se realizará la conceptualización de la programación entera pura haciendo uso del contexto histórico, las metodologías de desarrollo y los software que implementan estos modelos. Asimismo se hará uso de ejemplos triviales y de aplicación para acoplar y afianzar este modelo matemático de optimización.

## REQUISITOS

El Software para poder usarse se debe acceder a una página web en la que el código se ejecuta, por este método no se debe instalar nada, único requisito es tener conexión a internet ya que el software está en la nube y se ejecuta en los servidores de Google Colab

Si se desea ejecutar en el pc se debe tener python e instalar el “CVXOPT”, para ser instalado se debe abrir el símbolo del sistema usando “pip” con el siguiente comando
	
pip install cvxopt

### CVXOPT
CVXOPT (en español Software de Python para la optimización convexa) es un paquete de software gratuito para optimización convexa basado en el lenguaje de programación Python. Se puede usar con el intérprete interactivo de Python, en la línea de comandos ejecutando scripts de Python, o integrado en otro software a través de módulos de extensión. Su objetivo principal es hacer que el desarrollo de software para aplicaciones de optimización convexa sea sencillo al construir sobre la extensa biblioteca estándar de Python y sobre las fortalezas de Python como lenguaje de programación de alto nivel.
CVXOPT es desarrollado por Martin Andersen desde 2004 y recibe actualizaciones y mejoras continúas haciendo el paquete cada vez mas completo, también es software libre; puede redistribuir y / o modificarlo bajo los términos de la Licencia Pública General de GNU

También se puede seguir los pasos que estan en la pagina de cvxopt
https://cvxopt.org/install/index.html
O se pueden descargar los archivos necesarios para su instalación
https://cvxopt.org/download/index.html

## Uso de software
- Ingresamos en la matriz “c” los valores asociados a la función objetivo, es decir los valores que acompañan a las variables X1, X2, X3, …. Xn, estos valores separados por comas y dentro de unos corchetes, en este caso si la función objetivo es:
Z = 4X1+3X2+4X3
se debe ingresar asi: 
`c = m([-4., -3.,-4.]) #Matriz con los valores de la función objetivo`
- En la matriz “A” Ingresamos los valores de las variables de restricción que acompañan a las variables X1, X2, X3, …. Xn , estas también separadas por comas, los valores de todas las X1 van encerradas en corchetes, si hay mas variables se separa por coma y se agrega otro corchete, por ejemplo si las restricciones fueran
5X1+2X2+1X35
2X1+4X2+7X310
Los valores se deben ingresar asi:
`A = m([[5.,2.], [2.,4.], [1.,7]]) #Valores de las variables de las restricciones`
en donde el primer corchete corresponde a X1, el segundo a X2 y el tercero a X3
- En la matriz “b” Ingresamos  los  valores independientes de las restricciones es decir los que van después del <= o >=, estos valores están separados por comas dependiendo la cantidad de restricciones que hayan
Con las restricciones anteriores seria:
`b = m([5.,10.]) #Valores independientes de las restricciones`
- Especificamos que las variables sean enteras y binarias, reemplazando la “x” por la cantidad de variables que hay, e ste caso hay X1, X2 y X3 entonces son 3  variables: 
`intVars = range(3) #Especificamos que las x variables son enteras`
`binVars = range(3) #Especificamos que las x variables son binarias`
- Damos correr y este ejecutará y mostrará el resultado, lo que sale en valores óptimos de las variables el resultado saldrá dándonos 1 o 0, el primero que sale corresponde a X1 y así sucesivamente, el 1 significa que debe usarse esa variable y su valor asociado si es 0 significa que no debe usarse, al final nos dará el valor óptimo que debe dar : 
~~~
Los valores óptimos de las variables son:
[ 0.00e+00]
[ 0.00e+00]
[ 1.00e+00]

El valor óptimo es:  4.0
~~~
En este caso el resultado nos dice que se debe tomar la variable X3 y que el valor óptimo es Z = 4
