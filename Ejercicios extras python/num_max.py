'''
def max(num1, num2):
    if num1 > num2:
        print(num1, "Es mayor que", num2)
    elif num2 > num1:
        print(num2, "Es mayor que", num1)
    else:
        print("Ambos numeros son iguales")

max(1 , 2)'''

'''Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos. (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.'''
#Segunda forma de hacerlo
def max():
    num1 = int(input("Ingresa el primer numero: "))
    num2 = int(input("Ingresa el segundo numero: "))

    if num1 > num2:
        print(num1, "Es mayor que", num2)
    elif num2 > num1:
        print(num2, "Es mayor que", num1)
    else:
        print("Ambos numeros son iguales")

max()