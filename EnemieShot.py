from tupy import *
from SpaceShip import SpaceShip
from typing import List, Union
from Wall import Wall
from Shot import Shot
from Audio import Audio

class EnemieShot(Shot):
   def __init__(self) -> None:
      super().__init__()
      self.file = 'enemie_shot.png'
      self._spaceShip: Union[SpaceShip, None] = None
      self._enemieShots: List[EnemieShot] = []


   def update(self) -> None:
      """
        Destrói o tiro caso ele ultrapasse o limite da tela
        Verifica a coalisão do tiro inimigo com a nave
      """
      self.y+=15
      if(self.y > 500):
          self.destroy()
          self._enemieShots.remove(self)
      
      if isinstance(self._spaceShip, SpaceShip):
        spaceShipLifes = self._spaceShip._life._lifes
        if (spaceShipLifes > 0 and self._collides_with(self._spaceShip)):
            self.destroy()
            self._enemieShots.remove(self)
            self._spaceShip._life._lifes-=1
            if (self._spaceShip._life._lifes == 0):
                toast(f'Vidas: {self._spaceShip._life._lifes}, você perdeu', 100000)
                self._spaceShip.destroy()
                Audio().play('fail.mp3')
                self._spaceShip._hide()
    
      if isinstance(self._wall, Wall):
        if self._collides_with(self._wall):
            self.destroy()
            self._enemieShots.remove(self)