from tupy import *

class Shot(Image):
  def __init__(self):
      self.file = 'enemieV1.png'
      self.scene = None

  def update(self):
    self.y-=1
    for enemie in self.scene.enemies:
        if(self._collides_with(enemie)):
            print(f'colidiu como o inimigo n° {enemie.id}')
            enemie.destroy()
            self.destroy()
            self.scene.enemies.remove(enemie)

