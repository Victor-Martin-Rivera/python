# Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares e impares dentro de dos listas nueva

lista = []
num = 0

def pedir():
    #Contador
    i = 0
    while i <= 5:
        num = float(input("Ingresa un numero: "))
        lista.append(num)
        i += 1

def ordenar():
    #Ordena la lista
    lista.sort()
    pares = []
    impares = []
    for i in lista:
        #Ordena si son pares
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    print(pares)
    print(impares)

pedir()
ordenar()