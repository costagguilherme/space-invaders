from tupy import *
from Shot import Shot
from Enemie import Enemie
from Scene import Scene


scene = Scene()
spaceShip = scene.generateSpaceShip()
scene.generateEnemies()
 
run(globals())            