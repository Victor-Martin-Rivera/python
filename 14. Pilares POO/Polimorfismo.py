class Animales():
    def __init__(self, mensaje):
        self.mensaje = mensaje

    def hablar(self):
        print(self.mensaje)

class Perro(Animales):
    def hablar(self):
        print("Yo hago Guauu!!")

class Pez(Animales):
    def hablar(self):
        print("No hablo, soy un pez")

#Polimorfismo: La modificacion de metodos de clases heredadas y ocupacion de objetos a partir de varios metodos
perro = Perro("Guau!")
perro.hablar()

animal = Animales("Miau")
animal.hablar()

pez = Pez("Glup Glup!")
pez.hablar()