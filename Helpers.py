from tupy import *

class Timer:
   def __init__(self, interval):
      self._interval = interval
      self._counter = 0

   def update(self):
      self._counter += 1

   @property
   def ticked(self):
      return self._counter % self._interval == 0

   @property
   def ticks(self):
      return self._counter // self._interval

class Animacao(Image):
   def __init__(self, files, interval):
      self.files = files
      self._timer = Timer(interval)

   def update(self):
      self._timer.update()
      self.file = self.files[self._timer.ticks % len(self.files)]
      if self._timer.ticked:
         toast('tick', 100)