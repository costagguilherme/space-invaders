from tupy import *
from typing import List

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

