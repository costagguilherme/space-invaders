from tupy import *
from Enemie import Enemie
from typing import List
from typing import Union
from Wall import Wall

class Shot(Image):
  def __init__(self) -> None:
      self.file = 'spaceship_shot.png'
      self._enemies: List[Enemie] = []
      self._shots: List[Shot] = []
      self._wall : Union[Wall, None] = None

  def update(self) -> None:
    self.y-=30
    for enemie in self._enemies:
        if(self._collides_with(enemie)):
            self.destroy()
            enemie.destroy()
            self._enemies.remove(enemie)
            self._shots.remove(self)
    if(self.y < 0):
        self.destroy()
        self._shots.remove(self)

    if isinstance(self._wall, Wall):
        if self._collides_with(self._wall):
            self.destroy()
            self._shots.remove(self)
      




