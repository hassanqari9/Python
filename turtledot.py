import turtle as t
import random

tim = t.Turtle()

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim.hideturtle()
tim.pensize(20)
tim.speed("fastest")
tim.setheading(225)
tim.penup()
tim.forward(220)
tim.setheading(0)

dots = 10
for i in range(1,dots+1):
  for j in range(dots):
    tim.pendown()
    tim.pencolor(random.choice(colours))
    tim.forward(1)
    tim.penup()
    tim.forward(50)  
  tim.setheading(90)
  tim.forward(50)
  
  if i % 2 == 0:
    tim.setheading(0)
    tim.forward(50)
  else:
    tim.setheading(180)
    tim.forward(50)
