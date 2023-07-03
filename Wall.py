from tupy import *
import random

class Wall(Image):
    def __init__(self) -> None:
        self.file : str = 'wall.png'
        self.limiter : int = 35
        self.x : int =500
        self.y : int = 350
        self.sentido : str = random.choice(['left','right'])


    def turnRight(self) -> None:
        if self.x >= 100 and self.sentido == 'right':
             self.x += 10
        if self.x == 750:
            self.sentido = 'left'
    
    def turnLeft(self) -> None:
        if self.x <= 750 and self.sentido == 'left':
             self.x -= 10
        if self.x == 100:
            self.sentido = 'right'

    def update(self) -> None:
        self.turnLeft()
        self.turnRight()