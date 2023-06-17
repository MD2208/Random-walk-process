from turtle import Turtle, Screen
import random

timmy=Turtle()
my_screen=Screen()
directions=['left', 'right','forward','backward']
my_screen.colormode(255)
timmy.pensize(10)
timmy.speed(7)
for _ in range(0,100):
  r=random.randint(0,255)
  g=random.randint(0,255)
  b=random.randint(0,255)
  timmy.color((r,g,b))
  
  direction=random.choice(directions)
  if 'left'==direction:
    timmy.left(90)
    timmy.forward(30)
  elif 'right'==direction:
    timmy.right(90)
    timmy.forward(30)
  elif 'backward'==direction:
    timmy.backward(30)
  else:
    timmy.forward(30)





my_screen.exitonclick()