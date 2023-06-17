from tupy import *


class SpaceShip(Image):
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
            if self.contador == 15:
                self.file = 'spaceshipV3right.png'
            if self.file == 'spaceshipV2right.png':
                self.x += 7
                self.contador +=1
            elif self.file == 'spaceshipV3right.png':
                self.x += 12
        
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


class Enemie(Image):
    def __init__(self):
        self.file = 'enemieV1.png'
        self.id = 0


class Shot(Image):
  def __init__(self):
      self.file = 'enemieV1.png'
      self.scene = None

  def update(self):
    self.y-=1
    for enemie in self.scene.enemies:
        if(self._collides_with(enemie)):
            print(f'colidiu como o inimigo n° {enemie.id}')

class Scene(Image):
    def __init__(self):
        self.enemies = []
        self.spaceShip = None
        self.file = 'cenary.jpg'
        self.x = 450
        self.y = 250

    def generateEnemies(self):
        enemieId = 1

        xCoordinate = 50
        yCoordinate = 20
        for i in range(17):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        xCoordinate = 150
        yCoordinate = 50
        for i in range(13):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        xCoordinate = 250
        yCoordinate = 80
        for i in range(9):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        xCoordinate = 350
        yCoordinate = 110
        for i in range(5):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        xCoordinate = 400
        yCoordinate = 140
        for i in range(3):
            enemie = Enemie()
            enemie.x = xCoordinate
            enemie.y = yCoordinate
            enemie.id = enemieId
            self.enemies.append(enemie)
            xCoordinate = xCoordinate + 50
            enemieId+=1

        enemie = Enemie()
        enemie.x = 450
        enemie.y = 170
        enemie.id = enemieId
        
        self.enemies.append(enemie)

    def generateSpaceShip(self):
        spaceShip = SpaceShip()
        spaceShip.x = 450
        spaceShip.y = 460
        self.spaceShip = spaceShip
        return spaceShip
    
    def update(self):
        if keyboard.is_key_just_down('space'):
            shot = Shot()
            shot.x = self.spaceShip.x
            shot.y = self.spaceShip.y - 20
            shot.scene = scene



scene = Scene()

spaceShip = scene.generateSpaceShip()
scene.generateEnemies()


shot = Shot()
shot.x = spaceShip.x
shot.y = spaceShip.y - 20
shot.scene = scene



            
run(globals())            