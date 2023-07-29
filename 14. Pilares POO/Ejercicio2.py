# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    def __init__(self):
        #Si el usuario digita los numeros no se necesita poner parametros como el self X(num1, num2)X
            self.num1 = int(input("Ingrese el primer valor: "))
            self.num2 =  int(input("Ingrese el segundo valor: "))

    #Suma
    def suma(self):
            self.suma = self.num1 + self.num2
            print("La suma da como resultado: ",self.suma)

    #Resta
    def resta(self):
        #Esta parte fue modificada por mi
        if self.num2 < self.num1:
            self.resta = self.num1 - self.num2
            print("La resta da como resultado: ",self.resta)
        else:
            print("La resta no puede dar valores negativos")

    #Multiplicacion
    def multi(self):
        self.multi = self.num1 * self.num2
        print("La multiplicación da como resultado: ",self.multi)
        
    #Division
    def division(self):
        #Division entre 0
        try:
            self.division = self.num1 / self.num2
            print("La division da como resultado: ",self.division)
        except ZeroDivisionError:
            print("No se puede dividir entre 0")

#Si no tiene parametros en el init no lleva argumentos
calcular = Calculadora()
#Va en un print porque lleva un return en cada metodo
calcular.suma()
calcular.resta()
calcular.multi()
calcular.division()