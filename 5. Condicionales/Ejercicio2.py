#Escribir un programa que, dado un número entero, muestre su valor absoluto. Nota: para los numeros positivos su valor absoluto es igual al número (el valor absoluto de 52 es 52), mientras que, para los negativos, su valor absoluto es el número multiplicado por -1 (el valor absoluto de -52 es 52).

'''78 --> 78
-96 --> 96'''

#abs se encarga de sacar el valor absoluto de un numero
print(abs(5))

numero = int(input("Ingresa el numero ENTERO: "))

if numero > 0:
    print("El valor absoluto de {} es: {}".format(numero, numero))
else:
    print("El valor absoluto de {} es: {}".format(numero, abs(numero)))