diccionario = {1 : 2 , 2 : 3 , 3 : 4}
diccionario2 = {4 : 5 , 6 : 7}

#print(diccionario)

#Eliminara la clave 3 del diccionario
'''diccionario.pop(3)
print(diccionario)'''

#Limpia el diccionario
'''diccionario.clear()
print(diccionario)'''

#Recibra la clave 2 del diccionario y lo muestra
print(diccionario.get(2))

#Agrega el valor de la llave y su valor al final del diccionario
diccionario.setdefault(4 , 5)
print(diccionario)

#AAgrega un segundo diccionario al principal
diccionario.update(diccionario2)
print(diccionario)

#Copy saca una copia del diccionario
diccionario.copy()
print(diccionario)