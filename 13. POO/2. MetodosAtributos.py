class FabricaTelefonos():
    #Atributos
    marca = "Huawei"
    color = "Negro"
    memoriaRam = 32
    almacenamiento = 128
    
    #Los metodos son cosas que puede hacer un objeto(en este caso telefono)
    def llamar(self, mensaje):
        return mensaje
    
    def escucharMusica(self):
        print("Estas escuchando Musica")

telefono = FabricaTelefonos()
#Acceder mediante variables a los atributos
telefono.marca
telefono.color
telefono.memoriaRam

print(telefono.llamar("Hola, ¿Con quien hablo?"))
telefono.escucharMusica()