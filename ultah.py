import turtle
import time


ukuranfont = 18

# sets background
bg = turtle.Screen()
bg.bgcolor("black")

pen = turtle.Turtle()

turtle.hideturtle()
# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color("white")
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color("white")
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color("white")
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color("white")
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color("red")
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color("yellow")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.begin_fill()
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)
    turtle.end_fill()
    

# Happy Birthday message

def tulis(pesan, pos):
    x,y=pos
    pen.penup()
    pen.goto(x,y)
    pen.color('red')
    style=('Stencil Std', ukuranfont, 'italic')
    pen.write(pesan, font=style)
    
def pesan(pesan, pos):
    x,y=pos
    pen.penup()
    pen.goto(x,y)
    pen.color('white')
    style=('Stencil Std', ukuranfont, 'italic')
    pen.write(pesan, font=style)

tulis('H',(-67.9,95))
time.sleep(0.1)
tulis('A',(-55,95))
time.sleep(0.1)
tulis('P',(-42,95))
time.sleep(0.1)
tulis('P',(-30,95))
time.sleep(0.1)
tulis('Y',(-14,95))
time.sleep(0.1)
tulis('B',(10,95))
time.sleep(0.1)
tulis('I',(26,95))
time.sleep(0.1)
tulis('R',(33,95))
time.sleep(0.3)
tulis('T',(48,95))
time.sleep(0.1)
tulis('H',(60,95))
time.sleep(0.1)
tulis('D',(75,95))
time.sleep(0.3)
tulis('A',(88,95))
time.sleep(0.1)
tulis('Y',(100,95))
time.sleep(0.1)
pesan('''To Me :)
I Hope I am Happy,''',(-68,40))
time.sleep(5)