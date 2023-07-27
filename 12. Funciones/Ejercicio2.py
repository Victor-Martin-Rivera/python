# Escribir una función que reciba un número entero positivo y devuelva su factorial.

#Primera forma
'''def factorial():
    num = int(input("Ingresa un numero entero y positivo: "))
    if num > 0:
        factorial = 1
        for i in range(1 , num + 1):
            factorial = factorial * i
        print("El factorial de {} es:".format(num),factorial)
    else:
        print("El numero es negativo y no puede sacar el factorial")

factorial()'''

from math import factorial

#Segunda forma
def factoriales():
    num = int(input("Ingresa un numero entero y positivo: "))
    if num > 0:
        print(factorial(num))
    else:
        print("El numero es negativo y no puede sacar el factorial")

factoriales()