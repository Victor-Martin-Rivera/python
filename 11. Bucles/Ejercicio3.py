# Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar el rango de numeros entre ambas cifras

for i in range(1, 11):
    print(i)

numero1 = int(input("Ingresa el primer numero: "))
numero2 = int(input("Ingresa el segundo numero: "))

for j in range(numero1, numero2 + 1):
    if numero1 < numero2:
        print(j)
else:
    print("Ingresa un numero mas pequeño")