# class FabricaTelefonos():
#     marca = "Samsung"

#     def ElaborarHuawei(self):
#         #Sirve para englobar un atributo a toda una clase(self)
#         self.marca = "Huawei"

# telefono = FabricaTelefonos()
# telefono.ElaborarHuawei()
# print(telefono.marca)

#metodo init(constructor)

class FabricaTelefonos():
    #Sirve para ejecutarse en cuanto se crea el objeto
    def __init__(self, marca, color):
        #Pide marca y color
        self.marca = marca
        self.color = color

telefono = FabricaTelefonos('Huawei', 'Negro')
print(telefono.marca)
print(telefono.color)