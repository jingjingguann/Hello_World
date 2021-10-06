import turtle
import random

#Initialise Python Turtle
jane = turtle.Turtle()
jane.hideturtle()
jane.speed(20)
window = turtle.Screen()
window.bgcolor("#EEEEEE")

# set the colormode to 255
turtle.colormode(255)

#A function to draw the Canvas
def drawCanvas(x,y,width):
  jane.penup()
  jane.goto(x,y)
  jane.pensize(3)
  jane.color("#563676")
  jane.pendown()
  for x in range(0,4):
    jane.forward(width)
    jane.right(90)

#A function to draw a confetti
def drawConfetti(x,y,radius,color):
  jane.penup()
  jane.goto(x,y-radius)
  jane.pendown()
  jane.fillcolor(color)
  jane.color(color)
  jane.begin_fill()
  jane.circle(radius)
  jane.end_fill()


#Main Program Starts Here
drawCanvas(-150,150,300)

for confetti in range(0,2000):
  radius = random.randint(5,12)
  x = random.randint(-150+radius,150-radius)
  y = random.randint(-150+radius,150-radius)

  #Generate a random purple colour!
  color = (random.randint(100,255),0,random.randint(100,255))
  
  #Draw Confetti
  drawConfetti(x,y,radius,color)

