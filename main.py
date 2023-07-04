from tupy import *
from Battlefield import Battlefield


battlefield = Battlefield()
battlefield.generateEnemies()
battlefield.generateWall()
spaceShip = battlefield.generateSpaceShip()
 
run(globals())
