from tupy import *
from Shot import Shot
from Enemie import Enemie
from Scene import Scene





scene = Scene()

spaceShip = scene.generateSpaceShip()
scene.generateEnemies()


shot = Shot()
shot.x = spaceShip.x
shot.y = spaceShip.y - 20
shot.scene = scene



            
run(globals())            