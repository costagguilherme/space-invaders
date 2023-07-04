from tupy import Image
from Helpers import Timer
class Enemie(Image):
    def __init__(self) -> None:
        self.file = 'enemieV1.png'
        self._id: int = 0
        self._counter: int = 0

    def setId(self, id: int) -> None:
        self._id = id