
from ursina import *
app = Ursina()
window.fullscreen=True
Sky()
bird = Animation(
  'assets\doodle\\bird',
  collider='box',
  color=color.orange,
  y=15
)
camera.add_script(
  SmoothFollow(
    target=bird,
    offset=[0,0,-50],
    speed=3
  )
)

platform = Entity(
  model='cube',
  color=color.green,
  texture='white_cube',
  collider='box',
  scale=(3,0.5)
)
plates = []
for i in range(5):
  p = duplicate(
    platform,
    y=platform.y+5
  )
  plates.append(p)

from random import randint

down = True
def makeTrue():
  global down
  down = True


label = Text(
  text='',
  color=color.olive,
  position=(-0.2,0.4),
  size=2*Text.size
)
points=bird.y


def update():
  global down, points
  points=max(points,bird.y)
  label.text = str(round(
    100*points
  ))
  if points - bird.y > 15:
    quit()

  bird.x -=held_keys['a']*12*time.dt
  bird.x +=held_keys['d']*12*time.dt
  bird.y -=7*time.dt
  if down and bird.intersects().hit:
    down = False
    invoke(makeTrue, delay=0.5)
    bird.animate_y(
      bird.y+7,
      duration=0.4,
      curve=curve.in_circ
    )
    plates.append(
      duplicate(
        platform,
        y=plates[-1].y+5,
        x=randint(-5,5)
      )
    )
    obj = plates[0]
    plates.pop(0)
    destroy(obj)


app.run()

