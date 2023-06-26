from tupy import *

class Timer:
   def __init__(self, interval):
      self.interval = interval
      self.counter = 0

   def update(self):
      self.counter += 1

   @property
   def ticked(self):
      return self.counter % self.interval == 0

   @property
   def ticks(self):
      return self.counter // self.interval

class Animacao(Image):
   def __init__(self, files, interval):
      self.files = files
      self.timer = Timer(interval)

   def update(self):
      self.timer.update()
      self.file = self.files[self.timer.ticks % len(self.files)]
      if self.timer.ticked:
         toast('tick', 100)