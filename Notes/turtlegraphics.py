import turtle

Name1 = turtle.textinput("Title", "Name of first player")
Name2 = turtle.textinput("Title", "Name of second player")

print(Name1)
print(Name2)
turtle.shape("turtle")

turtle.speed(5)

#turtle.forward(25)
#turtle.right(45)

print(turtle.heading())

turtle.backward(25)
turtle.left(45)

print(turtle.position)

turtle.setpos(100,100)
print(turtle.position)

turtle.color("black", "green")
turtle.begin_fill()
turtle.circle(100)
turtle.circle(50, 180)
turtle.circle(-50, 180)
turtle.right(90)

turtle.penup(); turtle.fd(50); turtle.pendown(); turtle.dot(20, "blue"); turtle.penup(); turtle.fd(50); turtle.pendown()
turtle.penup(); turtle.fd(50); turtle.pendown(); turtle.dot(20, "blue"); turtle.penup(); turtle.fd(50); turtle.pendown()

turtle.width(10)
turtle.color("red")
turtle.fillcolor("blue")
turtle.forward(200)

turtle.write("String", move=False, align='left', font=('Arial', 24, 'normal'))

turtle.shape("circle")
turtle.shapesize(5,2,12)
turtle.tilt(90)

def turn(x,y):
    turtle.left(180)
turtle.onclick(turn)

def glow(x,y):
    turtle.fillcolor("red")
def unglow(x,y):
    turtle.fillcolor("")

turtle.onclick(glow)
turtle.onrelease(unglow)

def f():
    turtle.fd(50)
turtle.onkey(f, "up")
turtle.listen()

turtle.mainloop()