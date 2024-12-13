import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

food = turtle.Turtle()
colors = random.choice(['red', 'blue', 'yellow'])
shapes = random.choice(['square', 'circle', 'triangle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

segments = []

pen = turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write(f"Score : {score} High Score: {high_score}", align="center", font=("arial", 24, "bold"))

def goup():
    if head.direction != "down":
        head.direction = "up"
        
def godown():
    if head.direction != "up":
        head.direction = "down"
        
def goleft():
    if head.direction != "right":
        head.direction = "left"
        
def goright():
    if head.direction != "left":
        head.direction = "right"

def move():
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

wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

# Loop principal del juego
while True:
    wn.update()

    # Verificar si la cabeza de la serpiente colisiona con los límites
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(0.3)
        head.goto(0, 0)
        head.direction = "Stop"
        score = 0
        for segment in segments:
            segment.goto(1203132, 38123218)  # Mover los segmentos fuera de la pantalla
        segments.clear()
        pen.clear()
        pen.write(f"Score : {score} High Score: {high_score}", align="center", font=("arial", 24, "bold"))

    # Verificar si la serpiente come la comida
    if head.distance(food) < 20:
        food.goto(random.randint(-270, 270), random.randint(-270, 270))
        score += 10

        # Crear un nuevo segmento para la serpiente
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("gray")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001  # Acelerar el juego cada vez que se come la comida

        # Actualizar el highscore si es necesario
        if score > high_score:
            high_score = score
            pen.clear()
            pen.write(f"Score : {score} High Score: {high_score}", align="center", font=("arial", 24, "bold"))

    # Mover los segmentos de la serpiente
    for i in range(len(segments) - 1, 0, -1):
        x = segments[i - 1].xcor()
        y = segments[i - 1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Mover la cabeza de la serpiente
    move()

    # Verificar si la serpiente colisiona consigo misma
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "Stop"
            score = 0
            delay = 0.1
            for segment in segments:
                segment.goto(1203132, 38123218)  # Mover los segmentos fuera de la pantalla
            segments.clear()
            pen.clear()
            pen.write(f"Score : {score} High Score: {high_score}", align="center", font=("arial", 24, "bold"))

    time.sleep(delay)

wn.mainloop()