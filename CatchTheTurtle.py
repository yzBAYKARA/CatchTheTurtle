import turtle
import time
import random

drawing_screen = turtle.Screen()
drawing_screen.bgcolor("Light blue")
drawing_screen.title("CatchTheTurtle")
turtle_table = turtle.Turtle()
turtle_instance = turtle.Turtle()
turtle_instance.shape(name = "turtle")
turtle_instance.shapesize(2,2,2)
turtleTable = turtle.Turtle()
seconds = 20
score = 0
def random_turtle():
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    turtle_instance.hideturtle()
    turtle_instance.penup()
    turtle_instance.goto(x, y)
    turtle_instance.showturtle()

def turtle_click(x,y):
    global score
    global score
    if turtle_instance.distance(x, y) < 20:
        score += 1




while seconds >0:
    turtle_table.clear()
    turtle_table.hideturtle()
    turtle_table.penup()
    turtle_table.goto(-4.0, 380.0)
    turtle_table.write("Seconds: {}".format(seconds), align="center", font=("Arial", 13, "bold"))
    turtleTable.clear()
    turtleTable.hideturtle()
    turtleTable.penup()
    turtleTable.goto(-4.0, 360.0)
    turtleTable.write("Score: {}".format(score), align="center", font=("Arial", 13, "bold"))
    time.sleep(0.5)
    seconds-=1
    if seconds ==0:
        turtle_table.clear()
        turtle_table.write("GAME OVER".format(seconds), align="center", font=("Arial", 13, "bold"))
    random_turtle()
    turtle.onscreenclick(turtle_click)


turtle.mainloop()