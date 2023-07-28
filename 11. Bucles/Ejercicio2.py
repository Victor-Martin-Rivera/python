# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad = int(input("Ingresa un numero para saber la edad de la persona: ")) #Pide un numero al usuario
i = 1

while i != edad: #Mientras i sea diferente de edad sigue contando pero cuando sean iguales se detiene e imprime
    print("Has cumplido: {} anios".format(i))
    i+= 1