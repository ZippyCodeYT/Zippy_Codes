
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()
Sky(texture='sky_sunset')
player = FirstPersonController()

sword = Entity(model='assets\\blade', texture='assets\sword', rotation=(30,-40),
               position=(0.6,-0.6), parent=camera.ui, scale=(0.2,0.15))

def update():
  if held_keys['left mouse']:
    sword.position = (0.6,-0.5)
  elif held_keys['right mouse']:
    sword.position = (0.6,-0.5)
  else:
    sword.position = (0.7,-0.6)

boxes = []
for n in range(12):
  for k in range(12):
    box = Button(color=color.white, model='cube', position=(k,0,n),
                 texture='assets\grass',parent=scene, origin_y=0.5)
    boxes.append(box)

def input(key):
  for box in boxes:
    if box.hovered:
      if key == 'left mouse down':
        new = Button(color=color.white, model='cube',position= box.position + mouse.normal,
                     texture='assets\grass', parent=scene, origin_y=0.5)
        boxes.append(new)
      if key == 'right mouse down':
        boxes.remove(box)
        destroy(box)
app.run()

