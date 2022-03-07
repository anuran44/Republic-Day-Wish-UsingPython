import turtle
import winsound
w = turtle.Screen()
w.setup(width=800,height=600)
w.bgcolor('black')

winsound.PlaySound('republic.wav',winsound.SND_ASYNC)


w.addshape('army244.gif')
image = turtle.Turtle()
image.speed(3)
image.shape('army244.gif')
image.goto(-280,0)


s = turtle.Turtle()
s.color('white')
s.penup()
s.setposition(-100,-280)
s.pendown()
s.goto(-100,280)

flag = turtle.Turtle()
flag.color('white')
flag.penup()
flag.setposition(-100,270)
flag.pendown()

l = 400
w = 80

def rectangle(color):
    flag.fillcolor(color)
    flag.begin_fill()
    flag.forward(l)
    flag.right(90)
    flag.forward(w)
    flag.right(90)
    flag.forward(l)
    flag.right(180)
    flag.end_fill()


rectangle('orange')
rectangle('white')
rectangle('green')

wheel = turtle.Turtle()
wheel.color('blue')
wheel.penup()
wheel.width(2)
wheel.goto(100,100)
wheel.pendown()
wheel.circle(50)
wheel.penup()
wheel.goto(100,150)
wheel.pendown()
for i in range(26):
    wheel.forward(48)
    wheel.backward(48)
    wheel.right(13.8)

text = turtle.Turtle()
text.speed(1)
text.hideturtle()

def write(message,pos,color):
    x,y=pos
    text.color(color)
    text.penup()
    text.goto(x,y)
    text.pendown()
    style = ('Courier',40,'italic')
    text.write(message,font=style)


write('Happy',(60,-100),'orange')
write('Rep',(10,-160),'white')
write('ub',(105,-160),'blue')
write('lic',(167,-160),'white')
write('Day',(70,-220),'green')

turtle.done()