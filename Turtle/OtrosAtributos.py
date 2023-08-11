import turtle

s = turtle.Screen()
t = turtle.Turtle()

#Crea un circulo pero lo rellena de color negro(default)
'''t.begin_fill()
t.circle(100)
t.end_fill()

t.begin_fill()
t.color("white", "white")
t.circle(50)
t.end_fill()'''

#Cambia el icono por una tortuga
t.shape("turtle")

#Deja de pintar con penup y se moviliza 100 pixeles
t.forward(100)
t.penup()
#Vuelve a dibujar con pendown
t.forward(100)
t.pendown()
t.forward(100)

#Es como un ctrl+z
t.undo()
t.clear()

t.reset()

t.forward(100)
#Deja una marca de agua
t.stamp()
t.forward(100)
turtle.done()