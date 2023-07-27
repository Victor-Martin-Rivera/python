#Escribir un programa que solicite al usuario una vocal en minuscula, y luego una letra en mayusculas. El programa debe convertir la letra en minuscula y la vocal en mayuscula, y al final, deben ser concatenadas ambas

vocal = input("Ingresa una vocal en MINUSCULA: ")
letra = input("Ingresa una letra en MAYUSCULA: ")

vocal = vocal.upper() #La transforma en mayuscula
letra = letra.lower() #La transforma en minuscula

print("La letra fue: {}\n La vocal fue {}".format(letra, vocal))