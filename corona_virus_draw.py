from turtle import *

hideturtle()

penup()
goto(0,200)
pendown()
bgcolor('black')
color('green')
speed(11)
a = 0
b = 0
while b < 200:
  forward(a)
  right(b)
  a = a + 3
  b = b + 1

done()
