from spaceship import *

ship = Spaceship()

class Bullet(object):
    def __init__(self):
        self.point = ship.head
        self.x, self.y = self.point
        self.width = 3
        self.height = 3
        self.c = ship.cos
        self.s = ship.sin
        self.xspeed = ship.cos * 10
        self.yspeed = ship.sin * 10

    def moving(self):
        self.x += self.xspeed
        self.y -= self.yspeed

    def draw(self, canvas):
        pygame.draw.rect(canvas, (255, 0, 0), [self.x, self.y, self.width, self.height])

    def beyond(self):
        if self.x < -50 or self.x > width or self.y > height or self.y < -50:
            return True
