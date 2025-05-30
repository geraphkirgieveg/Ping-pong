from pygame import *
import random

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,wight, height):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(wight,height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 420:
            self.rect.y += self.speed




back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 60
INIT_SPEED = 4
MAX_SPEED = 8
ACCEL_FACTOR = 1.05

speed_x = INIT_SPEED * random.choice((-1,1))
speed_y = random.uniform(-2,2)



racket1 = Player('racket.png', 30 , 200, 4, 40 , 150)
racket2 = Player('racket.png', 520 , 200, 4, 40 , 150)
ball = GameSprite('tenis_ball.png', 200, 200, 4, 50 ,50)

font.init()
font = font.SysFont('Arial', 35)
lose1 = font.render('Игрок 1 проиграл', True, (180,0,0))
lose2 = font.render('Игрок 2 проиграл', True, (180,0,0))

def bounce_off_paddle(paddale):
    global speed_x, speed_y
    rel_intersect_y = (ball.rect.centery - paddale.rect.centery)/(paddale.rect.height/2)
    speed_y = rel_intersect_y * abs(speed_x)
    speed_x = -speed_x * ACCEL_FACTOR


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(back)
        racket1.update_l()
        racket2.update_r()
        ball.rect.x += speed_x
        ball.rect.y -= speed_y

        if sprite.collide_rect(racket1, ball):
            bounce_off_paddle(racket1)

        if sprite.collide_rect(racket2, ball):
            bounce_off_paddle(racket2)

        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose2,(200,200))

        if ball.rect.x > 600:
            finish = True
            window.blit(lose2,(200,200))


        racket1.reset()
        racket2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)

