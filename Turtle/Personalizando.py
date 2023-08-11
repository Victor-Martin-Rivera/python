import turtle

s = turtle.Screen()
t = turtle.Turtle()

#Cambiar el color del lienzo
s.bgcolor("red")
#Cambiar el nombre del titulo
s.title("Proyecto 1")
#Personalizar tortuga(ancho = 3, largo = 3 y el borde = 3)
t.shapesize(3,3,3)
#Cambia el color de la tortuga
t.fillcolor("orange")
t.forward(100)

#Cambia el color del borde de la tortuga
t.pencolor("white")
t.forward(100)

#Cambia la direccion y color de la tinta y de la tortuga
t.color("green", "blue")
t.right(90)
t.forward(100)

#Modifica el grosor de la tinta
t.pensize(5)
t.forward(100)

#Mantiene la pantalla abierta
turtle.done()