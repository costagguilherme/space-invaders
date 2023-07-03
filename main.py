from tupy import *
from Battlefield import Battlefield


battlefield = Battlefield()
spaceShip = battlefield.generateSpaceShip()
battlefield.generateEnemies()
battlefield.generateWall()
 
run(globals())
