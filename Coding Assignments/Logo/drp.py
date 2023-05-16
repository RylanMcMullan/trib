import turtle

def draw(rad): # draw half of an oval one pixel at a time
    for i in range(53): # wide side of oval
        turtle.width(i/3) # weight = 1/3 the length of the first half of the oval
        turtle.circle(rad,1.8)
    

    for j in range(53): # short side of oval
        turtle.width((53-j)/3) # weight = 1/3 the length of the second half of the oval
        turtle.circle(rad/2,2)

turtle.speed(100)
turtle.color("#711f25")

# Dr
turtle.penup()
turtle.setpos(-50, 0) # Move to Dr

turtle.pendown()
turtle.write(" Dr ", move=False, align='left', font=('Dr.Peppers', 120))
turtle.penup()

# Pepper
turtle.goto(-280.00, -100.00) # Move to P
turtle.pendown()
turtle.write(" P  ", move=False, align='left', font=('Dr.Peppers', 210))
turtle.penup()

turtle.goto(-165.00, -80.00) # Move to finish pepper
turtle.pendown()
turtle.write(" epper ", move=False, align='left', font=('Dr.Peppers', 130))
turtle.penup()

# Est
turtle.goto(50, -90) # Move to Est
turtle.pendown()
turtle.write(" Est. 1885 ", move=False, align='left', font=('Dr.Peppers', 30))
turtle.penup()

# oval
turtle.goto(-180, -90)
turtle.pendown()
turtle.seth(-50)
draw(280)

turtle.hideturtle()
turtle.mainloop()