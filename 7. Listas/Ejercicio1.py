#En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez, debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

#[20, 50, "Curso", "Python", 3.14]

lista = [20, 50 , "Curso", "Python", 3.14]
print("Estos son los valores actuales de la lista {}".format(lista))

palabra1 = input("Ingrese el primer valor para sustituirlo en el espacio 1: ")
palabra2 = input("Ingrese el segundo valor para sustituirlo en el espadio 2: ")

#Modifica el dato del 0 y 1 y los cambio por los valores digitados por el usuario
lista[0] = palabra1
lista[1] = palabra2

'''
lista.insert(0, palabra1)
lista.insert(1, palabra2) '''

print("El nuevo valor de la lista es: {}".format(lista))