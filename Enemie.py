from tupy import *

class Enemie(Image):
    def __init__(self):
        self.file = 'enemieV1.png'
        self._id = 0

    def setId(self, id):
        self._id = id