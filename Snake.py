
from ursina import *
app = Ursina()

snake = Entity(model='cube', texture = 'assets\snake', scale=0.4, z=-1, collider='box')
ground = Entity(model='cube', texture='grass',rotation=(90,0,0),scale=(5,1,5), z=1)
apple = Entity(model='cube', texture='assets\\apple', scale=0.4, position=(1,-1,-1), collider='mesh')
body = [Entity(model='cube', scale =0.2, texture='assets\\body') for i in range(14)]

camera.orthographic = True
camera.fov = 8

from random import randint
dx = dy = 0
def update():
  info = snake.intersects()
  if info.hit:
    apple.x = randint(-4,4)/2
    apple.y = randint(-4,4)/2
    new = Entity(model='cube', z = -1, scale=0.2, texture='assets\\body')
    body.append(new)
  for i in range(len(body)-1,0,-1):
    pos = body[i-1].position
    body[i].position = pos
  body[0].x = snake.x
  body[0].y = snake.y
  snake.x += time.dt * dx
  snake.y += time.dt * dy

def input(key):
  global dx,dy
  for x,y,z in zip(['d','a'],[2,-2],[270,90]):
    if key==x:
      snake.rotation_z = z
      dx = y
      dy = 0
  for x,y,z in zip(['w','s'],[2,-2],[180,0]):
    if key == x:
      snake.rotation_z = z
      dy = y
      dx = 0

app.run()


























