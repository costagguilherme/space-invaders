from tupy import *

class Life(Image):
    def __init__(self) -> None:
        self._lifes: int = 3
        self._file = 'Vidas3.png'
        self.x = 80
        self.y = 440

    def update(self) -> None:
        """
            Alterna imagens que representam as vidas da nave
        """
        if self._lifes == 3:
            self._file = 'Vidas3.png'
        elif self._lifes == 2:
            self._file = 'Vidas2.png'
        elif self._lifes == 1:
            self._file = 'Vidas1.png'
        elif self._lifes == 0:
            self._file = 'Vidas0.png'