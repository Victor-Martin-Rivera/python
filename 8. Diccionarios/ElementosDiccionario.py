diccionario = {'Nombre' : "Victor" , 'Apellido' : "Rivera" , "Estatura" : 1.89}

print(diccionario)
#Devuelve las llaves
print(diccionario.keys())
#Devuelve los valores
print(diccionario.values())

#Imprime el valor de la clave Estatura
print(diccionario["Estatura"])

#Nuevo valor al diccionario
diccionario["Peso"] = "58 kg"
print(diccionario)

#Modificando un valor
diccionario["Nombre"] = "victor"
print(diccionario)