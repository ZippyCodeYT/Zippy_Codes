from ursina import *
import random as r


app = Ursina()
Sky()

bird = Animation('assets\img',
                 collider='box',
                 scale=(2,2,2),
                 y=10)

camera.orthographic = True
camera.fov = 20

def update():
  bird.y = bird.y - 4*time.dt
  for p in pipes:
    p.x = p.x - 2*time.dt
  touch = bird.intersects()
  if touch.hit or bird.y < -10:
    quit()


def input(key):
  if key == 'space':
    bird.y = bird.y + 3

pipes = []

pipe = Entity(model='quad',
              color=color.green,
              texture='white_cube',
              position=(20,10),
              scale=(3,15,1),
              collider='box')

def newPipe():
  y = r.randint(4, 12)
  new1 = duplicate(pipe, y=y)
  new2 = duplicate(pipe, y=y-22)
  pipes.extend((new1, new2))
  invoke(newPipe, delay=5)

newPipe()

app.run()