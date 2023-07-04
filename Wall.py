from tupy import *
import random
from KeyboardEnum import KeyboardEnum

class Wall(Image):
    def __init__(self) -> None:
        self.file = 'wall.png'
        self._limiter : int = 35
        self.x =500
        self.y = 350
        self._sense: str = random.choice([KeyboardEnum.LEFT.value, KeyboardEnum.RIGHT.value])


    def turnRight(self) -> None:
        if self.x >= 100 and self._sense == KeyboardEnum.RIGHT.value:
             self.x += 10
        if self.x == 750:
            self._sense = KeyboardEnum.LEFT.value
    
    def turnLeft(self) -> None:
        if self.x <= 750 and self._sense == KeyboardEnum.LEFT.value:
             self.x -= 10
        if self.x == 100:
            self._sense = KeyboardEnum.RIGHT.value

    def update(self) -> None:
        """
            Faz a movimentação do obstáculo
        """
        self.turnLeft()
        self.turnRight()