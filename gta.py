
from ursina import *
import random as r


app = Ursina()


camera.orthographic = True
camera.fov = 12
world = Entity(model='quad', texture='assets\street',scale=60, z=1, tag='world')


player = Entity(position=(0,-8))
man = Animation("assets\walking", parent = player, autoplay=False)
anim = Animator( animations = {
  'idle': Entity(model='quad',parent=player, scale=0.75,texture='assets\walking_0', tag='player'),
  'walking': man,
})


for i in [-8,8]:
  for j in [-2, 4]:
    house  = Sprite(model='quad',texture='assets\house',scale=0.75, collider = 'box',
                    position=(i,j,0), rotation_z=0 if i ==-8 else 180, tag="house")
  for i in [-2.5, 2.5]:
    for j in [-3.5, 6]:
      house = Sprite(model='quad', texture='assets\house', scale=0.75, collider='box',
                     position=(i, j, 0), rotation_z=270 if j ==-3.5 else 90,tag="house")



follow = SmoothFollow(target=player, offset=[0,0,-4], speed=8)
camera.add_script(follow)


npcs = []
for i in range(12):
  if i < 6:
    val = -1
    rot = 180
  else:
    rot = 0
    val = 1
  npc = Animation("assets\\npc", x=4, autoplay=True, rotation_z=rot,
                  collider='box', scale=0.75, position=(r.randint(-22,22),r.randint(-22,22)),tag='npc')
  npcs.append((npc,val))


car = Entity(model='quad',texture='assets\car',collider='box', scale=(2,1),
             rotation_z=0, y = -10, tag='car')
car_speed = 2


gun = Audio(
  'assets\gun.ogg',
  loop = False,
  autoplay = False
)
drive = Audio(
  'assets\car_drive.ogg',
  loop = True,
  autoplay = False
)


car_mode = False
front_stuck = False
back_stuck = False


def blink():
  if not car_mode and distance(car, player) < 1.5:
    dust = Entity(model=Circle(), scale=.3, color=color.smoke, position=car.position, tag='circle')
    dust.animate_scale(3, duration=.5, curve=curve.linear)
    dust.fade_out(duration=.5)
  invoke(blink, delay=1)
blink()

def update():
  global front_stuck, back_stuck, car_speed
  for npc, v in npcs:
    npc.y += v*time.dt
    if v == 1:
      if npc.y > 22:
        npc.y = -22
    else:
      if npc.y < -22:
        npc.y = 22
  if car_mode:
    player.position = car.position
    if held_keys['w']:
      if not drive.playing:
        drive.play()
      car.rotation_z -= held_keys['a'] * 100 * time.dt
      car.rotation_z += held_keys['d'] * 100 * time.dt
    elif held_keys['s']:
      if not drive.playing:
        drive.play()
      car.rotation_z += held_keys['a'] * 100 * time.dt
      car.rotation_z -= held_keys['d'] * 100 * time.dt
    else:
      drive.stop()
      car_speed = 2
    head_ray = raycast(car.position,
                       (math.cos(math.radians(360-car.rotation_z)),math.sin(math.radians(360-car.rotation_z)),0),
                                 ignore=(car,),distance=1.5)
    back_ray = raycast(car.position,
                       (-1*math.cos(math.radians(360-car.rotation_z)),-1*math.sin(math.radians(360-car.rotation_z)),0),
                                 ignore=(car,),distance=0.5)
    if not head_ray.hit or back_stuck or (head_ray.hit and head_ray.entity.tag == 'npc'):
      car_speed += 0.02
      car_speed = min(car_speed, 10)
      car.x +=held_keys['w']*car_speed*time.dt * math.cos(math.radians(car.rotation_z))
      car.y +=held_keys['w']*-car_speed*time.dt * math.sin(math.radians(car.rotation_z))
      front_stuck = False
      if head_ray.hit and head_ray.entity.tag == 'npc':
        Entity(model="quad", texture='assets\corpse', color=color.random_color(),
               scale=0.7, position = head_ray.entity.position, tag='corpse', z=0.5)
        head_ray.entity.disable()
    else:
      fron_stuck = True
    if not back_ray.hit or front_stuck or (back_ray.hit and back_ray.entity.tag == 'npc'):
      car_speed += 0.02
      car_speed = min(car_speed, 10)
      car.x -=held_keys['s']*car_speed*time.dt * math.cos(math.radians(car.rotation_z))
      car.y -=held_keys['s']*-car_speed*time.dt * math.sin(math.radians(car.rotation_z))
      back_stuck = False
      if back_ray.hit and back_ray.entity.tag == 'npc':
        Entity(model="quad", texture='assets\corpse', color=color.random_color(),
               scale=0.7, position = back_ray.entity.position, tag='corpse', z=0.5)
        back_ray.entity.disable()
    else:
      back_stuck = True
  else:
    if drive.playing:
      drive.stop()
    if held_keys['w'] or held_keys['a'] or held_keys['s'] or held_keys['d']:
      player.y += held_keys['w'] * 2 * time.dt
      player.y -= held_keys['s'] * 2 * time.dt
      player.x -= held_keys['a'] * 2 * time.dt
      player.x += held_keys['d'] * 2 * time.dt
      anim.state = 'walking'
    else:
      anim.state = 'idle'
    if held_keys['s']:
      player.rotation_z = 180
    if held_keys['w']:
      player.rotation_z = 0
    if held_keys['d']:
      player.rotation_z = 90
    if held_keys['a']:
      player.rotation_z = 270
    if held_keys['w'] and held_keys['d']:
      player.rotation_z = 45
    if held_keys['w'] and held_keys['a']:
      player.rotation_z = 315
    if held_keys['a'] and held_keys['s']:
      player.rotation_z = 225
    if held_keys['d'] and held_keys['s']:
      player.rotation_z = 135

def input(key):
  global car_mode
  if key=='q':
    quit()
  if key == 'b':
    if distance(car, player) < 1.5:
      if car_mode:
        car_mode = False
        player.position = car.position - (0, 1, 0)
        player.visible = True
        follow.target = player
      else:
        car_mode = True
        player.visible = False
        follow.target = car
  if key == 'left mouse down':
    if not car_mode:
      gun.play()
      x,y,z = mouse.position
      real_pos = player.position + (camera.fov*x, camera.fov*y, 0)
      direction = [real_pos[0]-player.x, real_pos[1]-player.y,0]
      dot  = Entity(model='sphere', color=color.black, scale=0.08,position=player.position,collider='sphere',
                    tag='bullet')
      dot.animate_position(player.position+[3*p for p in direction], duration=0.5,curve=curve.linear)
      invoke(destroy, dot, delay=0.5)
      shoot = raycast(player.position, direction, distance=10, ignore=(player,dot))
      if shoot.hit and shoot.entity.tag == 'npc':
        Entity(model="quad", texture='assets\corpse', color=color.random_color(),
               scale=0.7, position=shoot.entity.position, tag='corpse', z=0.5)
        shoot.entity.disable()

      player.rotation_z = 450-math.degrees(math.atan2(direction[1],direction[0]))


app.run()