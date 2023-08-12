import turtle

s = turtle.Screen()
t = turtle.Turtle()

t.forward(100)
t.right(90)
t.forward(100)

#Devuelve la ubicacion en coordenadas del objeto
print(t.pos())

turtle.done()