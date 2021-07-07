








from ursina import *
from ursina.prefabs.first_person_controller \
import FirstPersonController

app = Ursina()
Sky()
player = FirstPersonController()

for n in range(15):
  for k in range(15):
    box = Button(
      position= (k,0,n),
      color= color.orange,
      highlight_color = color.lime,
      model= 'cube',
      texture= 'white_cube',
      origin_y= 0.5,
      parent= scene
    )


app.run()






















