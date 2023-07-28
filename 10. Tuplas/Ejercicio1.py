# Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado, es el mes que debe mostrar en la tupla

#La tupla inicia en 0
tupla = ("Enero" , "Febrero" , "Marzo" , "Abril" , "Mayo" , "Junio" , "Julio" , "Agosto" , "Septiembre" , "Octubre" , "Noviembre" , "Diciembre")

OpcionMes = int(input("Ingresa el numero de tu mes: "))

#Como la tupla inicia en 0 tendremos que ponerle -1 al valor
print("El mes correspondiente es: " , tupla[OpcionMes-1])