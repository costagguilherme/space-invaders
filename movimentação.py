from tupy import *

class Nave(Image):
    def __init__(self):
        self.file = 'nv_V1.png'
        self.contador = 0
    
    def vira_direita(self):
        if self.file == 'nv_V2D.png':
            self.x += 5
            self.contador += 1
        elif self.file == 'nv_V3D.png':
            self.x += 10



    def update(self):
        if keyboard.is_key_down('Right'):
            if self.file == 'nv_V1.png':
                self.file = 'nv_V2D.png'
            if self.file == 'nv_V2D.png':
                self.vira_direita()
            # elif self
        
        if keyboard.is_key_up('Right'):
            self.file = 'nv_V1.png'
            self.contador = 0



        if keyboard.is_key_down('Left'):
            if self.file == 'nv_V1.png':
                self.file = 'nv_V2E.png'
            if self.contador == 15:
                self.file = 'nv_V3E.png'
            if self.file == 'nv_V2E.png':
                self.x -= 7
                self.contador +=1
            elif self.file == 'nv_V3E.png':
                self.x -= 12
        
        if keyboard.is_key_up('Left'):
            self.file = 'nv_V1.png'
            self.contador = 0

Navinha = Nave()

            
run(globals())            