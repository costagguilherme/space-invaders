from tupy import *
from Shot import Shot
from Shot import EnemieShot
from Enemie import Enemie
from SpaceShip import SpaceShip
from random import randint
from Helpers import Timer
from typing import List

class Battlefield(Image):
    def __init__(self) -> None:
        self._enemies: List[Enemie] = []
        self.file = 'cenary.jpg'
        self.x = 450
        self.y = 250
        self._shots: List[Shot] = []
        self._enemieShots: List[EnemieShot] = []
        self._timer: Timer = Timer(15)

    def generateEnemies(self) -> None:
        enemyId = 1
        coordinates = [(60, 20), (60, 50), (60, 80), (60, 110), (60, 140)]

        for coordinate in coordinates:
            xCoordinate, yCoordinate = coordinate
            for _ in range(13):
                enemy = Enemie()
                enemy.x = xCoordinate
                enemy.y = yCoordinate
                enemy.setId(enemyId)
                self._enemies.append(enemy)
                xCoordinate += 65
                enemyId += 1

    def generateSpaceShip(self) -> SpaceShip:
        spaceShip = SpaceShip()
        spaceShip.x = 450
        spaceShip.y = 460
        self._spaceShip = spaceShip
        toast(f'Vidas: {spaceShip._lifes}')
        return spaceShip
        
    def update(self) -> None:
        # Lógica para gerar os tiros da nave
        if keyboard.is_key_just_down('space') and len(self._shots) < 3 and self._spaceShip._lifes > 0:
            shot = Shot()
            shot = shot
            shot.x = self._spaceShip.x
            shot.y = self._spaceShip.y - 20
            shot._battlefield = self
            self._shots.append(shot)

        # Updates
        for shot in self._shots:
            shot.update()
            
        for enemieShot in self._enemieShots:
            enemieShot.update()

        # Lógica para gerar os tiros do inimigo
        self._timer.update()
        if (len(self._enemies) - 1) >= 0:
            if self._timer.ticked and len(self._enemieShots) < 3:
                self.generateEnemieShot()

        # Jogador venceu
        if (len(self._enemies) == 0):
            toast("Parabéns, você venceu!", 300000)

    def generateEnemieShot(self) -> None:
        randomEnemie = randint(0, len(self._enemies) - 1)
        enemie = self._enemies[randomEnemie]
        # A coordenada x só pode ter um tiro por vez
        if not self.hasEnemieShotOnXcoordinate(enemie.x):
            shot = EnemieShot()
            shot.x = enemie.x
            shot.y = enemie.y + 20
            shot._battlefield = self
            self._enemieShots.append(shot)

    def hasEnemieShotOnXcoordinate(self, xCoordinate: int) -> bool:
        for enemieShot in self._enemieShots:
            if enemieShot.x == xCoordinate:
                return True
        return False

