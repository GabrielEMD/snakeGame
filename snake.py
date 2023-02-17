import turtle
import time
import random


def run():
    # timeloop
    posponer = 0.23
    blue = 255


    # fondo
    worm = turtle.Screen()
    worm.bgcolor("black")
    worm.title("Juegito de la serpiente >:3")
    worm.setup(width = 600, height = 600)
    worm.tracer(0)


    # gusanito(head) o jugador xd
    head = turtle.Turtle()
    head.speed(0)
    head.shape("square")
    head.color("#BAC7CB")
    head.penup()
    head.goto(0,0)
    head.direction = "stop"


    # comidita 7w7 fruta
    foodbool = 1
    food = turtle.Turtle()
    food.speed(0)
    food.shape("turtle")
    food.color("#9EE1C4")
    food.penup()
    food.goto(0,100)


    # partesitas del worm
    segment = []
    bandera = True


    # funciones (movimientos :v)
    def up():
        head.direction = "up"
    def down():
        head.direction = "down"
    def left():
        head.direction = "left"
    def right():
        head.direction = "right"
    def pause():
        head.direction = "stop"


    def mov():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)

        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)

        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)

        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)


    # tecladito
    worm.listen()
    worm.onkeypress(up, "Up")
    worm.onkeypress(up, "w")
    worm.onkeypress(down, "Down")
    worm.onkeypress(down, "s")
    worm.onkeypress(left, "Left")
    worm.onkeypress(left, "a")
    worm.onkeypress(right, "Right")
    worm.onkeypress(right, "d")
    worm.onkeypress(pause, "x")


    while True:
        worm.update()
        mov()


        # distancia head food
        if head.distance(food) < 20:
            x = random.randint(-14,14)
            y = random.randint(-14,14)
            food.goto((x*20),(y*20))
            segm = turtle.Turtle()
            segm.speed(0)
            segm.shape("square")
            segm.penup()
            segment.append(segm)
        elif bandera == True:
            segm = turtle.Turtle()
            segm.speed(0)
            segm.shape("square")
            segm.penup()
            segment.append(segm)
            bandera = False


        # movimiento cositos
        totalSeg = len(segment)
        for index in range(totalSeg -1, 0, -1):
            x = segment[index - 1].xcor()
            y = segment[index - 1].ycor()
            segment[index].goto(x,y)
            segment[index].color("#BAC7CB")
        if totalSeg > 0:
            x = head.xcor()
            y = head.ycor()
            segment[0].goto(x,y)
            segment[0].color("#BAC7CB")



        # foodsito()
        if foodbool >= 0:
            food.shapesize(0.8,0.8,1)
            foodbool -= 1
        else:
            food.shapesize(0.5,0.5,1)
            foodbool += 1
        time.sleep(posponer)


if __name__ == "__main__":
    run()