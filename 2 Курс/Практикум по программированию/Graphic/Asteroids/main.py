from tkinter import *
import math
import random
from characters import *

start = False
score, lives = 0, 3

def start_game(pos):

    global start, lives, score

    center = [width / 2, height / 2]
    size = logo.info.size
    inwidth = (center[0] - size[0] / 2) < pos[0] < (center[0] + size[0] / 2)
    inheight = (center[1] - size[1] / 2) < pos[1] < (center[1] + size[1] / 2)

    if (not start) and inwidth and inheight:
        start = True
        lives = 3
        score = 0


def asteroids_spawner():

    global asteroidsgroup_set, catship


    asteroid_sprite = Sprite(
        [random.choice(range(width)), random.choice(range(height))],
        [random.randint(1, 3), random.randint(1, 3)],
        random.choice([-0.1, 0.1]),
        random.choice([-0.01, 0.01]),
        asteroid.image,
        asteroid.info,
    )


    if (
        len(asteroidsgroup_set) < 20
        and dist(asteroid_sprite.position, catship.position) > 200
        and start
    ):
        asteroidsgroup_set.add(asteroid_sprite)


def draw(canvas):

    global score, asteroidsgroup_set, lives, catship, bulletsgroup_set, start


    canvas.draw_image(
        background.image,
        background.info.center,
        background.info.size,
        [width / 2, height / 2],
        [width, height],
    )


    str1 = "Счёт: " + str(score)
    str2 = "Жизни: " + str(lives)
    canvas.draw_text(str(str2), [40, 40], 20, "white")
    canvas.draw_text(str(str1), [40, 80], 20, "white")

    catship.draw(canvas)

    catship.update()

    if lives <= 0:
        start = False
        catship = SpaceShip(
            [width / 2, height / 2], [0, 0], 0, catship_img.image, catship_img.info
        )
        catship.ismove = False

        for sprite in set(asteroidsgroup_set):
            asteroidsgroup_set.remove(sprite)

        for sprite in set(bulletsgroup_set):
            bulletsgroup_set.remove(sprite)

        for element in set(explosionsgroup_set):
            explosionsgroup_set.remove(element)

    if not start:
        canvas.draw_image(
            logo.image,
            logo.info.center,
            logo.info.size,
            [width / 2, height / 2],
            logo.info.size,
        )

    if start:
        process_sprite_group(asteroidsgroup_set, canvas)
        process_sprite_group(bulletsgroup_set, canvas)
        process_sprite_group(explosionsgroup_set, canvas)

    if group_collide(asteroidsgroup_set, catship):
        lives -= 1
        catship.position = [height / 2, width / 2]
        catship.vel = [0, 0]
        catship.angle = 0
        catship.angle_vel = 0
        catship.draw(canvas)
        catship.update()

    score += group_group_collide(asteroidsgroup_set, bulletsgroup_set)

asteroidsgroup_set = set({})
bulletsgroup_set = set({})
explosionsgroup_set = set({})

def process_sprite_group(group_set, canvas):

    for sprite in set(group_set):

        sprite.draw(canvas)

        if sprite.update():
            group_set.remove(sprite)


def group_collide(group_set, other_object):

    for sprite in set(group_set):

        if sprite.collide(other_object):
            group_set.remove(sprite)
            explosion_pos = sprite.position
            explosion_vel = [0, 0]
            explosion_avel = 0
            explosion_sprite = Sprite(
                explosion_pos,
                explosion_vel,
                0,
                explosion_avel,
                explosion.image,
                explosion.info,
            )
            explosionsgroup_set.add(explosion_sprite)
            return True

    return False


def group_group_collide(asteroids_set, bullets_set):

    counter = 0
    for sprite in copy(asteroids_set):

        if group_collide(bullets_set, sprite):
            asteroids_set.discard(sprite)
            counter += 1
    return counter

from copy import copy
import TKinter as tk

def keydown(button_id):
    global bulletsgroup_set

    if not start:
        return

    if button_id == 37 or button_id == 65:
        catship.incAv()

    if button_id == 39 or button_id == 68:
        catship.decAv()

    if button_id == 38 or button_id == 87:
        catship.ismove = True

    if button_id == 32:
        bulletsgroup_set = catship.shoot(
            start, bulletsgroup_set, bullet.image, bullet.info
        )


def keyup(button_id):
    if not start:
        return

    if button_id == 37 or button_id == 39 or button_id == 65 or button_id == 68:
        catship.setAv()

    if button_id == 38 or button_id == 87:
        catship.ismove = False


background = ImageStorage(
    ImageInfo([400, 400], [800, 800]), tk.load_image("./img/background.png")
)

logo = ImageStorage(ImageInfo([200, 125], [400, 250]), tk.load_image("./img/logo.png"))

catship_img = ImageStorage(
    ImageInfo([45, 45], [90, 90], 35), tk.load_image("./img/ship.png")
)

bullet = ImageStorage(
    ImageInfo([5, 5], [10, 10], 3, 17), tk.load_image("./img/bullet.png")
)

asteroid = ImageStorage(
    ImageInfo([45, 45], [90, 90], 40), tk.load_image("./img/asteroid.png")
)

explosion = ImageStorage(
    ImageInfo([64, 64], [128, 128], 17, 24, True), tk.load_image("./img/explosion.png")
)

width, height = 800, 800
localeframe = tk.create_frame("Зачетная работа - Астероиды", width, height)
catship = SpaceShip(
    [width / 2, height / 2], [0, 0], 0, catship_img.image, catship_img.info
)


localeframe.set_draw_handler(draw)
localeframe.set_keydown_handler(keydown)
localeframe.set_keyup_handler(keyup)
localeframe.set_mouseclick_handler(start_game)


timer = tk.create_timer(1000.0, asteroids_spawner)

timer.start()
localeframe.start()