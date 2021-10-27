
from ursina import *
from ursina.prefabs.\
  first_person_controller \
  import FirstPersonController

app = Ursina()
Sky()
player = FirstPersonController()

from ursina.shaders \
import basic_lighting_shader
boxes = []
for n in range(12):
  for k in range(12):
    box = Button(
      color=color.white,
      model='sphere',
      position=(k,0,n),
      texture='grass',
      shader=basic_lighting_shader,
      parent=scene,
      origin_y=0.5
    )
    boxes.append(box)

def input(key):
  for box in boxes:
    if box.hovered:
      if key =='left mouse down':
        new = Button(
          color=color.white,
          model='sphere',
          position=box.position+
          mouse.normal,
          texture='grass',
          shader=basic_lighting_shader,
          parent=scene,
          origin_y=0.5
        )
        boxes.append(new)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)

sword = Entity(model='assets\\blade', texture='assets\sword', rotation=(30,-40),
               position=(0.35,-0.6), parent=camera.ui, scale=(0.2,0.15))

def update():
  if held_keys['left mouse']:
    sword.position = (0.45,-0.5)
  elif held_keys['right mouse']:
    sword.position = (0.45,-0.5)
  else:
    sword.position = (0.5,-0.6)

app.run()
