from math import sqrt

a = int(input("Ingresa valor de A: "))
b = int(input("Ingresa valor de B: "))
c = int(input("Ingresa valor de C: "))
x1 = 0
x2 = 0

# Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones, sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”, “b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje: “La solución es: <solucion>”

if((b**2) - (4*a*c)) < 0 :
    print("No se puede realizar porque no se puede sacar raiz a un numero negativo")
else:
    x1 = (-b + sqrt((b**2)-(4*a*c)))/(2*a)
    x2 = (-b - sqrt((b**2)-(4*a*c)))/(2*a)
    print("La solucion es: \nx1=", x1, "\nx2=", x2)