
from ursina import *
from ursina.prefabs.first_person_controller \
  import FirstPersonController

app = Ursina()

player = FirstPersonController()
ground = Entity(
  model='plane',
  texture='grass',
  collider='mesh',
  scale=(100,1,100)
)
for i in range(10):
  for j in range(10):
    robot = FrameAnimation3d(
      'assets\\robot',
      position=(2*i,0,2*j),
      fps=18,
      scale=0.015,
      color=color.black66
    )
Sky()

app.run()