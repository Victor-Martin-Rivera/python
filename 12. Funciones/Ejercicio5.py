# Crear un programa que tenga dos funciones, una que contenga el area de un cuadrado con argumentos de base y altura; y la otra el area de un circulo con argumento de radio

def areacuadrado(lado1, lado2):
    area = lado1 * lado2
    print(area)

def areaCirculo(radio):
    return pow(radio, 2) * 3.14
    
areacuadrado(5, 5)
print(areaCirculo(10))