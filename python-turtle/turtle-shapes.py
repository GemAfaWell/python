import turtle

timmy = turtle.Turtle()
timmy.color('black', 'purple')
timmy.pensize(8)
timmy.shape('turtle')
timmy.speed(5)


def triangle(edge=100):
    timmy.begin_fill()
    timmy.forward(edge)
    timmy.right(120)
    timmy.forward(edge)
    timmy.right(120)
    timmy.forward(edge)
    timmy.left(120)
    timmy.end_fill()


timmy.penup()
timmy.setpos(-100, 0)
timmy.pendown()

triangle()
triangle()
triangle()
timmy.left(60)
triangle()
triangle()
triangle()

timmy.color('purple', 'turquoise')

timmy.right(60)
timmy.penup()
timmy.forward(200)
timmy.pendown()


def rectangle():
    timmy.forward(150)
    timmy.right(90)
    timmy.forward(150)
    timmy.right(90)
    timmy.forward(150)
    timmy.right(90)
    timmy.forward(150)
    timmy.right(90)


def paint_cir():
    timmy.begin_fill()
    timmy.circle(35)
    timmy.circle(50)
    timmy.end_fill()
    timmy.color('purple', 'turquoise')


rectangle()
paint_cir()
timmy.forward(150)
paint_cir()

timmy.penup()
timmy.left(180)
timmy.forward(50)
timmy.left(90)
timmy.forward(50)
timmy.pendown()


def eyes():
    timmy.circle(12.5)


eyes()
timmy.penup()
timmy.goto(125, -50)
timmy.pendown()
eyes()


def nose():
    timmy.forward(25)
    timmy.left(120)
    timmy.forward(25)
    timmy.left(120)
    timmy.forward(25)
    timmy.left(120)


timmy.penup()
timmy.goto(175, -62.5)
timmy.right(30)
timmy.pendown()
nose()


def smiley():
    timmy.circle(25, 180)


timmy.penup()
timmy.goto(150, -112.5)
timmy.setheading(270)
timmy.pendown()
smiley()


def arrow():
    timmy.forward(75)
    timmy.begin_fill()
    timmy.left(90)
    timmy.forward(15)
    timmy.right(180)
    timmy.forward(30)
    timmy.left(120)
    timmy.forward(30)
    timmy.left(120)
    timmy.forward(30)
    timmy.left(120)
    timmy.end_fill()


timmy.penup()
timmy.goto(-300, -250)
timmy.setheading(45)
timmy.pendown()
arrow()


def bow():
    timmy.setheading(90)
    timmy.forward(60)
    timmy.right(90)
    timmy.circle(-60, 90)
    timmy.right(90)
    timmy.forward(60)


timmy.penup()
timmy.goto(-300, -250)
timmy.pendown()
bow()
timmy.penup()
