import turtle
import math
import random

class SolarSystem:
    # Sets up the solar system
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width/2.0,-height/2.0,width/2.0,height/2.0,)
        self.ssscreen.tracer(50)

    # Creates the Sun
    def addSun(self, asun):
        self.thesun = asun

    # Creates the planets
    def addPlanets(self, aplanet):
        self.planets.append(aplanet)

    # Creates physics
    def movePlanets(self):
        G = .1 # Establish universal gravitational constant
        dt = .001 # Establish change in time 

        # Go through all planets
        for p in self.planets:
            # Moves the planet based on the velocity and position
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())
            # Calculates the position in relation to the sun (X & Y distance matters
            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()
            r = math.sqrt (rx**2 + ry**2)
            # Calculates the gravitation pull of the sun
            gravityx = G * self.thesun.getMass()*rx/r**3
            gravityy = G * self.thesun.getMass()*ry/r**3
            # Sets the new X & Y Velocity in relation to the gravitation pull
            p.setXVel(p.getXVel() + dt * gravityx)
            p.setYVel(p.getYVel() + dt * gravityy)

class Sun:
    # Sets up the Sun
    def __init__(self, sname, srad, smass):
        self.name = sname
        self.radius = srad
        self.mass = smass
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    # Returns radius
    def getRadius(self):
        return self.radius
    # Returns mass
    def getMass(self):
        return self.mass
    # Returns x position
    def getXPos(self):
        return self.x
    # Returns y position
    def getYPos(self):
        return self.y


class Planet:
    # Sets up the planets
    def __init__(self, pname, prad, pmass, pdist, pvx, pvy, pcolor):
        self.name =  pname
        self.radius = prad
        self.mass = pmass
        self.distance = pdist
        self.x = pdist
        self.y = 0
        self.velocityx = pvx
        self.velocityy = pvy
        self.color = pcolor

        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.goto(self.x, self.y)
        self.pturtle.down()

    # Returns the name of the planet
    def getName(self):
        return self.name
    # Returns radius
    def getRadius(self):
        return self.radius
    # Returns mass
    def getMass(self):
        return self.mass
    # Returns distance
    def getDistance(self):
        return self.distance
    # Returns x position
    def getXPos(self):
        return self.x
    # Returns y position
    def getYPos(self):
        return self.y
    # Returns velocity in the x direction
    def getXVel(self):
        return self.velocityx
    # Returns velocity in the y direction
    def getYVel(self):
        return self.velocityy
    # Moves the planet
    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)
    # Changes the planet's velocity in the x direction
    def setXVel(self, newvelx):
        self.velocityx = newvelx
    # Changes the planet's velocity in the y direction
    def setYVel(self, newvely):
        self.velocityy = newvely

# Create space back ground
def addSpace():
    for i in range(100):
        turtle.Screen().bgcolor("Black")
        turtle.speed(100)
        turtle.penup()
        turtle.goto(random.randint(-300, 300), random.randint(-300, 300))
        turtle.pendown()
        turtle.dot(4, "White")

# Create the solar system and run the "movePlanets()" function
def createSSandAnimate():
    ss = SolarSystem(2,2)

    # Add Sun
    sun = Sun("SUN", 5000, 10)
    ss.addSun(sun)
    # Add each planet
    e = Planet("EARTH", 47.5, 5000, 0.3, 0, 2.0, "green")
    me = Planet("MERCURY", 18.2, 330, 0.11, 0, 2.0, "Grey")
    v = Planet("VENUS", 45.1, 4670, 0.27, 0, 2.0, "Orange")
    m = Planet("MARS", 25.3, 642, 0.41, 0, 2.0, "Red")

    ss.addPlanets(e)
    ss.addPlanets(me)
    ss.addPlanets(v)
    ss.addPlanets(m)

    # Set the time intervals
    nunTimePeriods = 20000
    # Move planets with each completion of the time interval
    for amove in range(nunTimePeriods):
        ss.movePlanets()

addSpace()
createSSandAnimate()
turtle.mainloop()
