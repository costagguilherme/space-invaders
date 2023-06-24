from tupy import *

class SpaceShip(Image):
    def __init__(self):
        self.file = 'spaceship.png'
        self.contador = 0
        self.lifes = 3
    
    def turnRight(self):
        if self.file == 'spaceship.png':
            self.file = 'spaceshipV2right.png'
            self.angle -= 10
        if self.file == 'spaceshipV2right.png':
            self.x = self.x + 5
            self.contador = self.contador + 1
        if self.contador == 15:
            self.file = 'spaceshipV3right.png'
            self.contador += 1
        if self.file == 'spaceshipV3right.png':
            self.x = self.x + 10

    def turnLeft(self):
        if self.file == 'spaceship.png':
            self.file = 'spaceshipV2left.png'
            self.angle += 10
        if self.file == 'spaceshipV2left.png':
            self.x = self.x - 5
            self.contador = self.contador + 1
        if self.contador == 15:
            self.file = 'spaceshipV3left.png'
            self.contador += 1
        if self.file == 'spaceshipV3left.png':
            self.x = self.x -10

    def update(self):
        if keyboard.is_key_down('Right'):
            self.turnRight()
        if keyboard.is_key_up('Right') and keyboard.is_key_up('Left'):
            self.file = 'spaceship.png'
            self.contador = 0
            self.angle = 0
        if keyboard.is_key_down('Left'):
            self.turnLeft()