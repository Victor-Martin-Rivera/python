# Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Estudiante():
    #Constructor
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    
    #Forma 2 de hacerlo, crear un metodo datos y pasarle el self, nombre y nota
    # def datos(self, nombre, nota):
    #     self.nombre = nombre
    #     self.nota = self.nota
    
    #Como no pide encapsular no se creara el metodo get y set
    @property
    def imprimir(self):
        print("Nombre: {}\nNota: {}".format(self.nombre, self.nota))
    
    @property
    def resultados(self):
        if self.nota < 7:
            print("¡Has REPROBADO!\n")
        else:
            print("¡Has APROBADO!\n")

#Como tenemos el metodo init le pasamos los argumentos
estudiante1 = Estudiante("Daniel", 10)
#Si lo hacemos con el init nos ahorramos 1 linea de codigo y menos consumo de memoria
#estudiante1.datos("Daniel, 10)
estudiante1.imprimir
estudiante1.resultados

estudiante2 = Estudiante("Elizabeth", 5)
estudiante2.imprimir
estudiante2.resultados