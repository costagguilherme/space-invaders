from tupy import *

class Shot(Image):
  def __init__(self):
      self.file = 'spaceship_shot.png'
      self.battlefield = None

  def update(self):
    self.y-=30
    for enemie in self.battlefield.enemies:
        if(self._collides_with(enemie)):
            print(f'colidiu com o inimigo n° {enemie.id}')
            enemie.destroy()
            self.destroy()
            self.battlefield.enemies.remove(enemie)
            self.battlefield.shots.remove(self)
    if(self.y < 0):
        self.destroy()
        self.battlefield.shots.remove(self)


