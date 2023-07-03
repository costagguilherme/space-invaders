from tupy import *
from Enemie import Enemie
from SpaceShip import SpaceShip
from typing import List
from typing import Union

class Shot(Image):
  def __init__(self) -> None:
      self.file = 'spaceship_shot.png'
      self._enemies: List[Enemie] = []
      self._shots: List[Shot] = []

  def update(self) -> None:
    self.y-=30
    for enemie in self._enemies:
        if(self._collides_with(enemie)):
            enemie.destroy()
            self.destroy()
            self._enemies.remove(enemie)
            self._shots.remove(self)
    if(self.y < 0):
        self.destroy()
        self._shots.remove(self)


class EnemieShot(Shot):
   def __init__(self) -> None:
      super().__init__()
      self._spaceShip: Union[SpaceShip, None] = None
      self._enemieShots: List[EnemieShot] = []


   def update(self) -> None:
      self.y+=5
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


