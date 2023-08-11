nombre_de_la_lista = [] #Primer modo para crear una lista vacia.

nombre_de_la_lista2 = list() #Segundo modo para crear una lista vacia.

nombre_de_la_lista_con_elementos = [1, 2, True, 'Hola', 5.8] #Primer modo para crear una lista con datos

nombre_de_la_lista_con_elementos2 = list([4, 9, False, 'texto']) #Segundo modo para crear una lista con datos

##
# Obtener el valor de un elemento de una lista en Python
##

mi_lista = ['Juan', 'Pedro', 'Laura', 'Carmen', 'Susana']
print(mi_lista[0]) # Muestra Juan (la primera posición es la 0)
print(mi_lista[-1]) # Muestra Susana
print(mi_lista[1]) # Muestra Pedro
print(mi_lista[2]) # Muestra Laura
print(mi_lista[-2]) # Muestra Carmen

##
# Recorrer una lista en Python
##

edades = [20, 41, 6, 18, 23]

# Recorriendo los elementos
for edad in edades:
    print(str(edad) + ' Elementos')

# Recorriendo los índices
for i in range(len(edades)):
    print(str(edades[i]) + ' Índices')

# Con while y los índices
indice = 0

while indice < len(edades):
    print(str(edades[indice]) + ' While')
    indice += 1