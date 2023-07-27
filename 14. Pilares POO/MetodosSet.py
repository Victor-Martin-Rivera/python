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

    @cuenta.setter
    def cuenta(self, cuenta):
        #Valor que va a ser seteado
        self._cuenta = cuenta 

    #Get Contador
    @property 
    def contador(self):
        return self._contador
    
    @contador.setter
    def contador(self, contador):
        self._contador = contador
    
a = A()
#Mando a llamar el metodo cuenta con valor 0 (get)
print(a.cuenta)
#Se modifica el valor del set
a.cuenta = 20
print(a.cuenta)
print(a.contador)
a.contador = 10
print(a.contador)
# a._contador = 10
# print(a._cuenta)
