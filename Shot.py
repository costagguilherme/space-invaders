from tupy import *

class Shot(Image):
  def __init__(self):
      self.file = 'enemieV1.png'
      self.battlefield = None

  def update(self):
    self.y-=5
    for enemie in self.battlefield.enemies:
        if(self._collides_with(enemie)):
            print(f'colidiu como o inimigo n° {enemie.id}')
            enemie.destroy()
            self.destroy()
            self.battlefield.enemies.remove(enemie)
            self.battlefield.shots.remove(self)


