from tupy import *


class Tiro(Image):
  def update(self):
    self.y-=1

class Alvo(Image):
    pass

class Nave(Image):
    def update(self):
        if keyboard.is_key_down('Left'):
            self.x -= 5
        if keyboard.is_key_down('Right'):
            self.x += 5

        if keyboard.is_key_just_down('space'):
            tiro = Tiro()
            tiro.file = 'tiro.png'
            tiro.x = self.x
            tiro.y = self.y
        
nave = Nave()
nave.file = 'star.png'
nave.x = 300
nave.y = 300

# tiro = Tiro()
# tiro.file = 'tiro.png'
# tiro.x = 300
# tiro.y = 301

alvo = Alvo()
alvo.file = 'ivysaur.png'
alvo.x = 300
alvo.y = 20
run(globals())