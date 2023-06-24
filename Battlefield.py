from tupy import *
from Shot import Shot
from Shot import EnemieShot
from Enemie import Enemie
from SpaceShip import SpaceShip
from random import randint
from Helpers import Timer

class Battlefield(Image):
    def __init__(self):
        self.enemies = []
        self.spaceShip = None
        self.file = 'cenary.jpg'
        self.x = 450
        self.y = 250
        self.currentShot = None
        self.shots = []
        self.enemieShots = []
        self.timer = Timer(15)

    def generateEnemies(self):
        enemyId = 1
        coordinates = [(60, 20), (60, 50), (60, 80), (60, 110), (60, 140)]

        for coordinate in coordinates:
            xCoordinate, yCoordinate = coordinate
            for _ in range(13):
                enemy = Enemie()
                enemy.x = xCoordinate
                enemy.y = yCoordinate
                enemy.id = enemyId
                self.enemies.append(enemy)
                xCoordinate += 65
                enemyId += 1

    def generateSpaceShip(self):
        spaceShip = SpaceShip()
        spaceShip.x = 450
        spaceShip.y = 460
        self.spaceShip = spaceShip
        toast(f'Vidas: {spaceShip.lifes}')
        return spaceShip
        
    def update(self):
        # Lógica para gerar os tiros da nave
        if keyboard.is_key_just_down('space') and len(self.shots) < 3:
            shot = Shot()
            shot = shot
            shot.x = self.spaceShip.x
            shot.y = self.spaceShip.y - 20
            shot.battlefield = self
            self.shots.append(shot)

        # Updates
        for shot in self.shots:
            shot.update()
            
        for enemieShot in self.enemieShots:
            enemieShot.update()

        # Lógica para gerar os tiros do inimigo
        self.timer.update()
        if (len(self.enemies) - 1) >= 0:
            if self.timer.ticked and len(self.enemieShots) < 3:
                self.generateEnemieShot()

        # Jogador venceu
        if (len(self.enemies) == 0):
            toast("Parabéns, você venceu!", 300000)

    def generateEnemieShot(self):
        randomEnemie = randint(0, len(self.enemies) - 1)
        enemie = self.enemies[randomEnemie]
        # A coordenada x só pode ter um tiro por vez
        if not self.hasEnemieShotOnXcoordinate(enemie.x):
            shot = EnemieShot()
            shot.x = enemie.x
            shot.y = enemie.y + 20
            shot.battlefield = self
            self.enemieShots.append(shot)

    def hasEnemieShotOnXcoordinate(self, xCoordinate):
        for enemieShot in self.enemieShots:
            if enemieShot.x == xCoordinate:
                return True
        return False

