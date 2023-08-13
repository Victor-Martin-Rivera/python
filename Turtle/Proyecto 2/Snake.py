import turtle
import time
import random

retraso = 0.1
marcador = 0
marcador_alto = 0

s = turtle.Screen()
#La pantalla es de 650 x 650
s.setup(650, 650)
s.bgcolor('gray')
s.title('Proyecto 2')

serpiente = turtle.Turtle()
serpiente.speed(1)
#Figura de un cuadrado
serpiente.shape('square')
#Sin dibujar(que solo siga un rastro)
serpiente.penup()
serpiente.goto(0,0)
serpiente.direction = 'stop'
serpiente.color('green')

comida = turtle.Turtle()
comida.shape('circle')
comida.color('orange')
comida.penup()
comida.goto(0,100)
comida.speed(0)

#Lista
cuerpo = []

texto = turtle.Turtle()
texto.speed(0)
texto.color('black')
texto.penup()
texto.hideturtle()
texto.goto(0, -260)
texto.write("Marcador: 0\tMarcador más alto: 0", align="center", font=("verdana", 24, "normal"))

def arriba():
    serpiente.direction = 'up'

def abajo():
    serpiente.direction = 'down'

def derecha():
    serpiente.direction = 'right'

def izquierda():
    serpiente.direction = 'left'

'''Agrega movimiento a la serpiente'''
def movimiento():
    if serpiente.direction == 'up':
        y = serpiente.ycor()
        serpiente.sety(y + 20)
    elif serpiente.direction ==  'down':
        y = serpiente.ycor()
        serpiente.sety(y - 20)
    elif serpiente.direction == 'right':
        x = serpiente.xcor()
        serpiente.setx(x + 20)
    elif serpiente.direction == 'left':
        x = serpiente.xcor()
        serpiente.setx(x - 20)

#Cuando presione una tecla la pantalla escuchara y lo replicara
s.listen()
s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(izquierda, "Left")
s.onkeypress(derecha, "Right")

while True:
    s.update()
    #Si pasa los 300 pixeles del plano cartesiano pierdes
    if serpiente.xcor() > 300 or serpiente.xcor() < -300 or serpiente.ycor() > 300 or serpiente.ycor() < -300:
        time.sleep(2)
        #Se elimina la lista si se pierde
        for i in cuerpo:
            i.clear()
            i.hideturtle()
        #Se manda al inicio
        serpiente.home()
        serpiente.direction = 'stop'
        #La lista se limpia
        cuerpo.clear()

        marcador = 0
        texto.clear()
        texto.write("Marcador: {}\tMarcador mas alto: {}".format(marcador, marcador_alto, align= "center", font=("verdana", 24, "normal")))
    #La comida spawnea e
    # n un punto de -250, 250 (X,Y)
    if serpiente.distance(comida) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x,y)

        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape('square')
        nuevo_cuerpo.color('green')
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerpo.append(nuevo_cuerpo)

        marcador += 1
        if marcador > marcador_alto:
            marcador_alto = marcador
            texto.clear()
            texto.write("Marcador: {}\tMarcador mas alto: {}".format(marcador, marcador_alto,align= "center",font=("verdana", 24, "normal")))
            

    total = len(cuerpo)
    #Recorrera la lista a la inversa(-1), el 0 es la cabeza de la serpiente y 1 es porque ira la cuenta de -1 en -1
    for i in range(total -1, 0 , -1):
        #Devuelve la coordenada en x
        x = cuerpo[i-1].xcor()
        y = cuerpo[i-1].ycor()
        cuerpo[i].goto(x, y)

    #Si en la lista hay mas de un elemento(un cuerpo) envia el cuerpo
    if total > 0:
        x = serpiente.xcor()
        y = serpiente.ycor()
        cuerpo[0].goto(x, y)

    movimiento()

    #Verifica si se ha tocado el cuerpo
    for i in cuerpo:
        if i.distance(serpiente) < 20:
            for i in cuerpo:
                i.clear()
                i.hideturtle()
            serpiente.home()
            cuerpo.clear()
            serpiente.direction = 'stop'
    time.sleep(retraso)

turtle.done()