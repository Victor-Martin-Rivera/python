def entero():
    print('Este es un dato entero: ')
    return 10

def decimal():
    print('Este es un dato decimal: ')
    return 90.99

def frase():
    return 'Mi nombre es Victor Rivera'

def asignacion():
    return 1 , 2 , 3 , 4 , 5

#Siempre hay que envolverlo en un print para que se muestre en pantalla
print(entero())
print(decimal())
print(frase())

#a = 1 , b = 2 , c = 3, d = 4 , e = 5
a , b , c , d , e = asignacion()
print(a)
print(b)
print(c)
print(d)
print(e)