from ursina import *
from ursina.prefabs.first_person_controller \
  import FirstPersonController

app = Ursina()
window.fullscreen = True
ground = Entity(model= 'plane',
                texture= 'grass',
                collider= 'mesh',
                scale= (100,1, 100))

player = FirstPersonController()
Sky()

myBox = Entity(model= 'cube',
               color= color.black,
               collider= 'box',
               position= (5, 0.5, 5))
myBall = Entity(model= 'sphere',
                color= color.red,
                collider= 'sphere',
                position= (5, 0.5, 10))
app.run()