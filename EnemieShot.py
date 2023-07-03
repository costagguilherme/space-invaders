from tupy import *
from SpaceShip import SpaceShip
from typing import List
from typing import Union
from Wall import Wall
from Shot import Shot

class EnemieShot(Shot):
   def __init__(self) -> None:
      super().__init__()
      self.file = 'enemie_spaceship_shot.png'
      self._spaceShip: Union[SpaceShip, None] = None
      self._enemieShots: List[EnemieShot] = []


   def update(self) -> None:
      self.y+=15
      if(self.y > 500):
          self.destroy()
          self._enemieShots.remove(self)
      
      if isinstance(self._spaceShip, SpaceShip):
        spaceShipLifes = self._spaceShip._lifes
        if (spaceShipLifes > 0 and self._collides_with(self._spaceShip)):
            self.destroy()
            self._enemieShots.remove(self)
            self._spaceShip._lifes-=1
            toast(f'Vidas: {self._spaceShip._lifes}')
            if (self._spaceShip._lifes == 0):
                toast(f'Vidas: {self._spaceShip._lifes}, você perdeu', 100000)
                self._spaceShip.destroy()
                self._spaceShip._hide()
    
      if isinstance(self._wall, Wall):
        if self._collides_with(self._wall):
            self.destroy()
            self._enemieShots.remove(self)