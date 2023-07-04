from tupy import *
from Life import Life


class SpaceShip(Image):
    def __init__(self) -> None:
        self.file = 'spaceship.png'
        self._contador: int = 0
        self._life = Life()
    
    def turnRight(self) -> None:
        if self.file == 'spaceship.png':
            self.file = 'spaceshipV2right.png'
            self.angle -= 15
        if self.file == 'spaceshipV2right.png':
            self.x = self.x + 5
            self._contador = self._contador + 1
        if self._contador == 15:
            self.file = 'spaceshipV3right.png'
            self._contador += 1
        if self.file == 'spaceshipV3right.png':
            self.x = self.x + 13

    def turnLeft(self) -> None:
        if self.file == 'spaceship.png':
            self.file = 'spaceshipV2left.png'
            self.angle += 15
        if self.file == 'spaceshipV2left.png':
            self.x = self.x - 5
            self._contador = self._contador + 1
        if self._contador == 15:
            self.file = 'spaceshipV3left.png'
            self._contador += 1
        if self.file == 'spaceshipV3left.png':
            self.x = self.x -13

    def update(self) -> None:
        if keyboard.is_key_down('Right'):
            self.turnRight()
        if keyboard.is_key_up('Right') and keyboard.is_key_up('Left'):
            self.file = 'spaceship.png'
            self._contador = 0
            self.angle = 0
        if keyboard.is_key_down('Left'):
            self.turnLeft()