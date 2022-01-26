import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
    
tim.speed("fastest")
change = 0
for i in range(100):
  change += 10
  tim.pencolor(random_color())
  tim.circle(50)
  tim.setheading(change)
  
