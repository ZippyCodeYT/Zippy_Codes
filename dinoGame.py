from ursina import *
import random as r

app = Ursina()
window.fullscreen = True
window.color = color.white


dino = Animation('assets\dino',
                 collider='box',
                 x=-5)

ground1 = Entity(
  model='quad',
  texture='assets\ground',
  scale=(50,0.5,1),
  z=1
)
ground2 = duplicate(ground1, x=50)
pair = [ground1, ground2]



cactus = Entity(
  model='quad',
  texture='assets\cacti',
  x = 20,
  collider='box'
)
cacti = []
def newCactus():
  new = duplicate(cactus,
                  x=12+r.randint(0,5))
  cacti.append(new)
  invoke(newCactus, delay=2)

newCactus()



label = Text(
  text = f'Points: {0}',
  color=color.black,
  position=(-0.5, 0.4)
)
points = 0

def update():
  global points
  points += 1
  label.text = f'Points: {points}'
  for ground in pair:
    ground.x -= 6*time.dt
    if ground.x < -35:
      ground.x += 100
  for c in cacti:
    c.x -= 6*time.dt
  if dino.intersects().hit:
    dino.texture= 'assets\hit'
    application.pause()


sound = Audio(
  'assets\\beep',
  autoplay=False
)


def input(key):
  if key == 'space':
    if dino.y < 0.01:
      sound.play()
      dino.animate_y(
        2,
        duration=0.4,
        curve= curve.out_sine
      )
      dino.animate_y(
        0,
        duration=0.4,
        delay=0.4,
        curve = curve.in_sine
      )

camera.orthographic = True
camera.fov = 10

app.run()