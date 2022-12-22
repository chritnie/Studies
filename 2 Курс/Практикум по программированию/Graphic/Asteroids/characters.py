import math
import TKinter as tkinter

width, height = 800, 800

class ImageStorage:

    def __init__(self, image_info, image):

        if not isinstance(image_info, ImageInfo):
            raise ValueError("Нужен экземпляр ImageInfo!")
        if not isinstance(image, tkinter.image.Image):
            raise ValueError("Нужен экземпляр tkinter.image для изображения!")

        self._image_info = image_info
        self._image = image

    @property
    def image(self):
        return self._image

    @property
    def info(self):
        return self._image_info


def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)

class ImageInfo:


    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self._center = center
        self._size = size
        self._radius = radius
        if lifespan:
            self._lifespan = lifespan
        else:
            self._lifespan = float("inf")
        self._animated = animated

    @property
    def center(self):
        return self._center

    @property
    def size(self):
        return self._size

    @property
    def radius(self):
        return self._radius

    @property
    def lifespan(self):
        return self._lifespan

    @property
    def animated(self):
        return self._animated


class Sprite:

    def __init__(self, pos, vel, angle, ang_vel, image, info):
        # Позиция
        self._pos = [pos[0], pos[1]]
        # Скорость
        self._vel = [vel[0], vel[1]]
        # Угол текущий
        self._angle = angle
        # Угол вращения
        self._angle_vel = ang_vel

        self._image = image
        self._image_center = info.center
        self._image_size = info.size
        self._radius = info.radius
        self._lifespan = info.lifespan
        self._animated = info.animated
        self._counter = 0

    @property
    def position(self):
        return self._pos

    @property
    def radius(self):
        return self._radius

    def draw(self, canvas):

        canvas.draw_image(
                self._image,
                self._image_center,
                self._image_size,
                self._pos,
                self._image_size,
                self._angle,
            )

    def update(self):

        self._angle += self._angle_vel
        self._pos[0] = (self._pos[0] + self._vel[0]) % width
        self._pos[1] = (self._pos[1] + self._vel[1]) % height
        self._counter += 1

        if self._counter > self._lifespan:
            return True
        return False

    def collide(self, other_object):

        dist = math.pow((self.position[0] - other_object.position[0]), 2) + math.pow(
            (self.position[1] - other_object.position[1]), 2
        )
        dist = math.pow(dist, 0.5)

        # Было столкновение
        if self._radius + other_object.radius > dist:
            return True

        # Не было столкновения
        return False


class SpaceShip:

    def __init__(self, pos, vel, angle, image, info):
        # Позиция
        self._pos = [pos[0], pos[1]]
        # Скорость
        self._vel = [vel[0], vel[1]]
        # Угол текущий
        self._angle = angle
        # Угол вращения
        self._angle_vel = 0

        self._image = image
        self._image_center = info.center
        self._image_size = info.size
        self._radius = info.radius
        self._ismove = False

    def draw(self, canvas):

        canvas.draw_image(
                self._image,
                self._image_center,
                self._image_size,
                self._pos,
                self._image_size,
                self._angle,
            )

    def update(self):


        self._angle += self._angle_vel
        self._pos[0] = (self._pos[0] + self._vel[0]) % width
        self._pos[1] = (self._pos[1] + self._vel[1]) % height

        fv = angle_to_vector(self._angle)

        if self._ismove:
            self._vel[0] += fv[0] / 10
            self._vel[1] += fv[1] / 10
        else:
            self._vel[0] = 0
            self._vel[1] = 0

        # Скорость перемещения
        self._vel[0] *= 1 - 0.001
        self._vel[1] *= 1 - 0.001

    def shoot(self, started, bullet_group, bullet_image, bullet_info):


        if not started:
            return

        vel = [0, 0]
        fw = angle_to_vector(self._angle)

        # Скорость снаряда
        vel[0] = self._vel[0] + fw[0] * 15
        vel[1] = self._vel[0] + fw[1] * 15
        bullet_pos = [self._pos[0] + fw[0] * 40, self._pos[1] + fw[1] * 40]
        a_bullet = Sprite(bullet_pos, vel, 0, 0, bullet_image, bullet_info)
        bullet_group.add(a_bullet)
        return bullet_group

    def incAv(self):
        """Поворот влево"""
        self._angle_vel -= 0.1

    def decAv(self):
        """Поворот вправо"""
        self._angle_vel += 0.1

    def setAv(self):
        """Окончание поворота влево/вправо"""
        self._angle_vel = 0

    @property
    def ismove(self):
        return self._ismove

    @ismove.setter
    def ismove(self, val):
        self._ismove = val

    @property
    def position(self):
        return self._pos

    @position.setter
    def position(self, value):
        self._pos = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        self._radius = value

    @property
    def vel(self):
        return self._vel

    @vel.setter
    def vel(self, value):
        self._vel = value

    @property
    def angle(self):
        return self_angle

    @angle.setter
    def angle(self, value):
        self._angle = value

    @property
    def angle_vel(self):
        return self._angle_vel

    @angle_vel.setter
    def angle_vel(self, value):
        self._angle_vel = value

