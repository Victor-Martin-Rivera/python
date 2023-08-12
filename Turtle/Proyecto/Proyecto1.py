import turtle
import random

#Creamos el lienzo
s = turtle.Screen()
s.title("Primer Proyecto")
s.bgcolor("gray")

jugador1 = turtle.Turtle()
jugador2 = turtle.Turtle()

#Esconde la tortuga
jugador1.hideturtle()
#Cambiamos la forma a una tortuga
jugador1.shape("turtle")
#Color de la tinta y figura verde
jugador1.color("green", "green")
#Modifica el tamaño de la tortuga(ancho, largo y borde)
jugador1.shapesize(2,2,2)
#Hacer la tinta mas gruesa
jugador1.pensize(3)

#Esconde la tortuga
jugador2.hideturtle()
#Cambiamos la forma a una tortuga
jugador2.shape("turtle")
#Color de la tinta y figura azul
jugador2.color("blue", "blue")
jugador2.shapesize(2,2,2)
#Hacer la tinta mas gruesa
jugador2.pensize(3)

#No dibujara el trazo
jugador1.penup()
jugador1.goto(200,200)
#Ya dibujaria de nuevo
jugador1.pendown()
jugador1.circle(40)

#Regresara al punto de inicio
jugador1.penup()
jugador1.goto(-250,225)
#Muestra la tortuga 1
jugador1.showturtle()

#No dibujara el trazo
jugador2.penup()
jugador2.goto(200,-200)
#Ya dibujaria de nuevo
jugador2.pendown()
jugador2.circle(40)

#Regresara al punto de inicio
jugador2.penup()
jugador2.goto(-250,-170)
#Muestra la tortuga 2
jugador2.showturtle()

#Lista
dado = [1,2,3,4,5,6]

#La tortuga llegara a la meta en al menos 20 pasos y si la tortuga azul llega a la coordenada(200,200) se detiene el juego y si llega antes la tortuga azul gana
for i in range(20):
    if jugador1.pos() >= (200,200):
        print("La tortuga verde ha ganado")
        break
    elif jugador2.pos() >= (200,-200):
        print("La tortuga azul ha ganado")
        break
    else:
        turno1 = input("Presiona la tecla enter para avanzar.")
        turno1 = random.choice(dado)
        #Ya que avanza por pixeles se requiere multiplicar el valor del dado por 20 para que avance
        print("Tu numero es: ",turno1, "\nAvanzas: ",turno1*20, "Pixeles")
        jugador1.pendown()
        jugador1.forward(20*turno1)

        turno2 = input("Presiona la tecla enter para avanzar la tortuga azul.")
        turno2 = random.choice(dado)
        #Ya que avanza por pixeles se requiere multiplicar el valor del dado por 20 para que avance mas
        print("Tu numero es: ",turno2, "\nAvanzas: ",turno2*20, "Pixeles")
        jugador2.pendown()
        jugador2.forward(20*turno2)


#Mantiene la pestaña abierta
turtle.done()