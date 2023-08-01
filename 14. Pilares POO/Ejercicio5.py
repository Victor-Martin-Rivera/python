# Crear un programa con tres clases Universidad, con atributos nombre (Donde se almacena el nombre de la Universidad). Otra llamada Carrera, con los atributos especialidad (En donde me guarda la especialidad de un estudiante). Una ultima llamada Estudiante, que tenga como atributos su nombre y edad. El programa debe imprimir la especialidad, edad, nombre y universidad de dicho estudiante con un objeto llamado persona

class Universidad():
    def __init__(self, Nombre):
        #Se cambia la variable a mayuscula porque abajo igual hay otra llamada nombre y no pueden llamarse igual
        self.Nombre = Nombre
        
class Carrera(Universidad):
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Carrera, Universidad):
    def datos(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        print("Mi nombre es {}, tengo {} años, mi especialidad es {}. Estudio en la Universidad {}".format(self.nombre, self.edad, self.especialidad, self.Nombre))

persona = Estudiante("Tecnologico de Ensenada")
persona.carrera("Sistemas")
persona.datos("Victor", 23)