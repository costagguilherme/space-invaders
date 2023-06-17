from tupy import *
from Scene import Scene


scene = Scene()
spaceShip = scene.generateSpaceShip()
scene.generateEnemies()
 
run(globals())            