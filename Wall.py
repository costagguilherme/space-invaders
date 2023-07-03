from tupy import *
import random

class Wall(Image):
    def __init__(self) -> None:
        self.file = 'wall.png'
        self._limiter : int = 35
        self.x =500
        self.y = 350
        self._sense: str = random.choice(['left','right'])


    def turnRight(self) -> None:
        if self.x >= 100 and self._sense == 'right':
             self.x += 10
        if self.x == 750:
            self._sense = 'left'
    
    def turnLeft(self) -> None:
        if self.x <= 750 and self._sense == 'left':
             self.x -= 10
        if self.x == 100:
            self._sense = 'right'

    def update(self) -> None:
        self.turnLeft()
        self.turnRight()