from tupy import *

class Shot(Image):
  def __init__(self):
      self.file = 'spaceship_shot.png'
      self._battlefield = None

  def update(self):
    self.y-=30
    for enemie in self._battlefield._enemies:
        if(self._collides_with(enemie)):
            enemie.destroy()
            self.destroy()
            self._battlefield._enemies.remove(enemie)
            self._battlefield._shots.remove(self)
    if(self.y < 0):
        self.destroy()
        self._battlefield._shots.remove(self)


class EnemieShot(Shot):
   def update(self):
      self.y+=5
      if(self.y > 500):
          self.destroy()
          self._battlefield._enemieShots.remove(self)
      
      spaceShipLifes = self._battlefield._spaceShip._lifes
      if (spaceShipLifes > 0 and self._collides_with(self._battlefield._spaceShip)):
          self.destroy()
          self._battlefield._enemieShots.remove(self)
          self._battlefield._spaceShip._lifes-=1
          toast(f'Vidas: {self._battlefield._spaceShip._lifes}')
          if (self._battlefield._spaceShip._lifes == 0):
            toast(f'Vidas: {self._battlefield._spaceShip._lifes}, você perdeu', 100000)
            self._battlefield._spaceShip.destroy()
            self._battlefield._spaceShip._hide()


