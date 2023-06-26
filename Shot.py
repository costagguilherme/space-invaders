from tupy import *

class Shot(Image):
  def __init__(self):
      self.file = 'spaceship_shot.png'
      self.battlefield = None

  def update(self):
    self.y-=30
    for enemie in self.battlefield.enemies:
        if(self._collides_with(enemie)):
            enemie.destroy()
            self.destroy()
            self.battlefield.enemies.remove(enemie)
            self.battlefield.shots.remove(self)
    if(self.y < 0):
        self.destroy()
        self.battlefield.shots.remove(self)


class EnemieShot(Shot):
   def update(self):
      self.y+=5
      if(self.y > 500):
          self.destroy()
          self.battlefield.enemieShots.remove(self)
      
      spaceShipLifes = self.battlefield.spaceShip.lifes
      if (spaceShipLifes > 0 and self._collides_with(self.battlefield.spaceShip)):
          self.destroy()
          self.battlefield.enemieShots.remove(self)
          self.battlefield.spaceShip.lifes-=1
          toast(f'Vidas: {self.battlefield.spaceShip.lifes}')
          if (self.battlefield.spaceShip.lifes == 0):
            toast(f'Vidas: {self.battlefield.spaceShip.lifes}, você perdeu', 100000)
            self.battlefield.spaceShip.destroy()
            self.battlefield.spaceShip._hide()


