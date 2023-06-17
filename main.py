from tupy import *
from Shot import Shot
from Enemie import Enemie
from Scene import Scene





scene = Scene()

spaceShip = scene.generateSpaceShip()
scene.generateEnemies()


# shot = Shot()
# shot.x = spaceShip.x
# shot.y = spaceShip.y - 20
# shot.scene = scene


# shot1 = Shot()
# shot1.x = spaceShip.x
# shot1.y = spaceShip.y - 80
# shot1.scene = scene


# shot3 = Shot()
# shot3.x = spaceShip.x
# shot3.y = spaceShip.y - 130
# shot3.scene = scene


            
run(globals())            