'''Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.'''

def max_de_tres():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))
    num3 = int(input("Ingresa el tercer numero: "))

    if num1 > num2 and num1 > num3:
        print("El numero {} es mayor que el numero {} y {}".format(num1, num2, num3))
    elif num2 > num1 and num2 > num3:
        print("El numero {} es mayor que el numero {} y {}".format(num2, num1, num3))
    elif num3 > num1 and num3 > num2:
        print("El numero {} es mayor que el numero {} y {}".format(num3, num1, num2))
    else:
        print("Los 3 numeros son iguales")

max_de_tres()