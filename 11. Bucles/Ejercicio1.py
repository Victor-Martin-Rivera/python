# Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero

numero = int(input("Ingresa un numero para saber su tabla: "))
i = 1
multi = 0

while i <= 10:
    multi = numero * i #Empieza en 1
    print("{} x {} = {}".format(numero, i, multi))
    i += 1