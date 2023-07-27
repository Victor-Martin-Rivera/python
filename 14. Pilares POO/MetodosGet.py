class A():
    def __init__(self):
        #Atributos encapsulados
        self._cuenta = 0
        self._contador = 0
    
    #Get de cuenta
    @property 
    #Property ayuda a quitar los parentesis y le dice que puede ser llamado como atributo
    def cuenta(self):
        return self._cuenta

    @property 
    def contador(self):
        return self._contador
    
a = A()
#Mando a llamar el metodo cuenta con valor 0
print(a.cuenta)
print(a.contador)
# a._contador = 10
# print(a._cuenta)