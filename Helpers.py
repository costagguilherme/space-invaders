from tupy import *

class Timer:
   def __init__(self, interval: int) -> None:
      self._interval: int = interval
      self._counter: int = 0

   def update(self) -> None:
      self._counter += 1

   @property
   def ticked(self) -> bool:
      return self._counter % self._interval == 0

   @property
   def ticks(self) -> int:
      return self._counter // self._interval

class Animacao(Image):
   def __init__(self, files: str, interval: int) -> None:
      self.files: str = files
      self._timer: Timer = Timer(interval)

   def update(self) -> None:
      self._timer.update()
      self.file = self.files[self._timer.ticks % len(self.files)]
      if self._timer.ticked:
         toast('tick', 100)