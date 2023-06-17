from tupy import *
from Shot import Shot
from Enemie import Enemie
from SpaceShip import SpaceShip

class Scene(Image):
    def __init__(self):
        self.enemies = []
        self.spaceShip = None
        self.file = 'cenary.jpg'
        self.x = 450
        self.y = 250
        self.currentShot = None
        self.shots = []

    def generateEnemies(self):
        enemieId = 1

        xCoordinate = 50
        yCoordinate = 20
        for i in range(17):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        xCoordinate = 150
        yCoordinate = 50
        for i in range(13):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        xCoordinate = 250
        yCoordinate = 80
        for i in range(9):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        xCoordinate = 350
        yCoordinate = 110
        for i in range(5):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        xCoordinate = 400
        yCoordinate = 140
        for i in range(3):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        enemie = Enemie()
        enemie.x = 450
        enemie.y = 170
        enemie.id = enemieId
        
        self.enemies.append(enemie)

    def generateSpaceShip(self):
        spaceShip = SpaceShip()
        spaceShip.x = 450
        spaceShip.y = 460
        self.spaceShip = spaceShip
        return spaceShip
    
    def update(self):
        if keyboard.is_key_just_down('space'):
            shot = Shot()
            shot = shot
            shot.x = self.spaceShip.x
            shot.y = self.spaceShip.y - 20
            shot.scene = self
            self.shots.append(shot)


        for shot in self.shots:
            shot.update()
        # if (self.currentShot is not None):
        #     print('nao é nulo')
        #     self.currentShot.update()