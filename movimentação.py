from tupy import *

class Nave(Image):
    def __init__(self):
        self.file = 'spaceship.png'
        self.contador = 0
    
    def vira_direita(self):
        if self.file == 'spaceshipV2right.png':
            self.x += 5
            self.contador += 1
        elif self.file == 'spaceshipV3right.png':
            self.x += 10



    def update(self):
        if keyboard.is_key_down('Right'):
            if self.file == 'spaceship.png':
                self.file = 'spaceshipV2right.png'
            if self.file == 'spaceshipV2right.png':
                self.vira_direita()
            # elif self
        
        if keyboard.is_key_up('Right'):
            self.file = 'spaceship.png'
            self.contador = 0



        if keyboard.is_key_down('Left'):
            if self.file == 'spaceship.png':
                self.file = 'spaceshipV2left.png'
            if self.contador == 15:
                self.file = 'spaceshipV3left.png'
            if self.file == 'spaceshipV2left.png':
                self.x -= 7
                self.contador +=1
            elif self.file == 'spaceshipV3left.png':
                self.x -= 12
        
        if keyboard.is_key_up('Left'):
            self.file = 'spaceship.png'
            self.contador = 0

Navinha = Nave()

            
run(globals())            