class FabricaTelefonos():
    #Constructor
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color
        print("El objeto {} ha sido creado".format(self.marca))
    
    #Mando a llamar al objeto(una descripcion mas detallada)
    def __str__(self):
        return "El objeto es {}".format(self.marca)
    
    #Destructor(se encarga de eliminar los objetos)
    def __del__(self):
        print("El objeto {} ha sido destruido".format(self.marca))

telefono = FabricaTelefonos("Nokia", "Negro")
print(telefono.marca)
print(telefono)