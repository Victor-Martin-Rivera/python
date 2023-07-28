class A():
    #Metodo(metodo de instancia lleva self)
    def primera(self):
        return "Esta es la clase A"

class B():
    def segunda(self):
        return "Esta es la clase B"
    
class C(A, B):
    def tercera(self):
        return "Esta es la clase C"

c = C()
print(c.primera())
print(c.segunda())
print(c.tercera())