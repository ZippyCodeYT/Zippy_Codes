from ursina import *

app = Ursina()
bg = Entity(model='quad', texture='assets\BG', scale=36, z=1)
window.fullscreen = True
player = Animation('assets\player', collider='box', y=5)
fly = Entity(model='cube', texture='assets\\fly1', collider='box',
             scale=2, x=20, y=-10)

flies = []
def newFly():
  new = duplicate(fly,y=-5+(5124*time.dt)%15)
  flies.append(new)
  invoke(newFly, delay=1)


newFly()
camera.orthographic = True
camera.fov = 20

def update():
  player.y += held_keys['w']*6*time.dt
  player.y -= held_keys['s'] *6* time.dt
  a = held_keys['w']*-20
  b = held_keys['s'] *20
  if a != 0:
    player.rotation_z = a
  else:
    player.rotation_z = b
  for fly in flies:
    fly.x -= 4*time.dt
    touch = fly.intersects()
    if touch.hit:
      flies.remove(fly)
      destroy(fly)
      destroy(touch.entity)
  t = player.intersects()
  if t.hit and t.entity.scale==2:
    quit()


def input(key):
  if key == 'space':
    e = Entity(y=player.y, x=player.x+1, model='cube', scale=1,
      texture='assets\Bullet', collider='cube')
    e.animate_x(30,duration=2,curve=curve.linear)
    invoke(destroy, e, delay=2)

app.run()