from spaceship import *
from asteroids import *
from bullet import *

pygame.init()

background = pygame.image.load('images/background.png')
logo = pygame.image.load('images/logo.png')

pygame.display.set_caption('Астероиды')
canvas = pygame.display.set_mode((width, height))
time = pygame.time.Clock()

start = True
score, lives = 0, 3


def interface():
    canvas.blit(background, (0,0))
    font = pygame.font.SysFont('TimesNewRoman',30)
    livesText = font.render('Жизни : ' + str(lives), 1, (255, 255, 255))
    scoreText = font.render('Очки: ' + str(score), 1, (255,255,255))

    ship.draw(canvas)
    for a in asteroids:
        a.draw(canvas)
    for b in Bullets:
        b.draw(canvas)


    if start:
        canvas.blit(logo, (width // 2 - 200, height // 2 - 150))
    canvas.blit(scoreText, (25, 55))
    canvas.blit(livesText, (25, 25))
    pygame.display.update()

Bullets = []
asteroids = []
count = 0
run = True
while run:
    time.tick(70)
    count += 1
    if not start:
        if count % 50 == 0:
            ran = random.choice([1,1,1,2,2,3])
            asteroids.append(Asteroid())

        ship.beyond()
        for b in Bullets:
            b.moving()
            if b.beyond():
                Bullets.pop(Bullets.index(b))


        for a in asteroids:
            a.x += a.xspeed
            a.y += a.yspeed

            if (a.x >= ship.x - ship.width//2 and a.x <= ship.x + ship.width//2) or (a.x + a.width <= ship.x + ship.width//2 and a.x + a.width >= ship.x - ship.width//2):
                if(a.y >= ship.y - ship.height//2 and a.y <= ship.y + ship.height//2) or (a.y  +a.height >= ship.y - ship.height//2 and a.y + a.height <= ship.y + ship.height//2):
                    lives -= 1
                    asteroids.pop(asteroids.index(a))
                    break

            for b in Bullets:
                if (b.x >= a.x and b.x <= a.x + a.width) or b.x + b.width >= a.x and b.x + b.width <= a.x + a.width:
                    if (b.y >= a.y and b.y <= a.y + a.height) or b.y + b.height >= a.y and b.y + b.height <= a.y + a.height:
                        score += 1
                        asteroids.pop(asteroids.index(a))
                        Bullets.pop(Bullets.index(b))
                        break

        if lives <= 0:
            start = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            ship.movingRight()
        if keys[pygame.K_LEFT]:
            ship.movingLeft()
        if keys[pygame.K_UP]:
            ship.movingStraight()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Bullets.append(Bullet())
            if event.key == pygame.K_SPACE:
                if start:
                    start = False
                    lives = 3
                    asteroids.clear()

    interface()
pygame.quit()