import random
import pygame

width = 800
height = 800

asteroid = pygame.image.load('images/asteroid.png')

class Asteroid(object):
    def __init__(self):
        self.image = asteroid
        self.width = 125
        self.height = 125
        self.ranPoint = random.choice([(random.randrange(0, width-self.width), random.choice([-1*self.height - 5, height + 5])), (random.choice([-1*self.width - 5, width + 5]), random.randrange(0, height - self.height))])
        self.x, self.y = self.ranPoint
        if self.x < width//2:
            self.xdir = 1
        else:
            self.xdir = -1
        if self.y < height//2:
            self.ydir = 1
        else:
            self.ydir = -1
        self.xspeed = self.xdir * random.randrange(1,3)
        self.yspeed = self.ydir * random.randrange(1,3)

    def draw(self, canvas):
        canvas.blit(self.image, (self.x, self.y))

    def beyond(self):
        if self.x > width + 50:
            self.x = 0
        elif self.x < 0 - self.width:
            self.x = width
        elif self.y < -50:
            self.y = height
        elif self.y > height + 50:
            self.y = 0