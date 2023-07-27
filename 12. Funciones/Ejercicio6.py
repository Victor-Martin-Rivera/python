# Escribir una función que reciba una muestra de números en una tupla y devuelva su medida.

def medida(*tupla):
    print(len(tupla))
    for i in tupla:
        print(i)
    return len(tupla)
    
print(medida(10, 20, 30 , 40, 50))