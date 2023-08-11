import turtle

s = turtle.Screen()
t = turtle.Turtle()

#Dibuja el circulo mas rapido
t.speed(10)
t.circle(10)
t.speed(10)
t.circle(50)
#dot es un circulo con relleno
t.dot(30)

#Esconde la tortuga
t.hideturtle()
t.speed(1)
t.circle(40)
t.showturtle()
t.circle(100)

#Mueve a la tortuga en el eje X pero manteniendo el eje Y
t.setx(100)
t.sety(-500)

turtle.done()