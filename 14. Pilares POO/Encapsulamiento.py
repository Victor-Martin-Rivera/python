class A():
    def __init__(self):
        self.contador = 0
    
    def incrementar(self):
        self.contador += 1

    def cuenta(self):
        #Atributo
        return self.contador

class B():
    def __init__(self):
        self.__contador = 0
    
    def incrementar(self):
        self.__contador += 1

    def cuenta(self):
        return self.__contador
    
a = A()
print("Objeto uno")
#Llama al metodo cuenta
print(a.cuenta())
a.incrementar()
print(a.cuenta())
#Llama al atributo contador
print(a.contador)

print("Objeto 2")
b = B()
print(b.cuenta())
b.incrementar()
print(b.cuenta())
#Encapsulamiento (ponemos en privado un atributo y solo puede ser accedido desde la misma clase)
print(b.__contador)