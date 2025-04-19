from pygame import *

W = 700
H = 500

window = display.set_mode((W, H))
display.set_caption('Пинг Понг')
back = (114, 165, 247)
window.fill(back)

clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Racket1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < H - 200:
            self.rect.y += self.speed

class Racket2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < H - 200:
            self.rect.y += self.speed


racket_r = Racket1('racket_red.png', 0, 125, 80, 200, 5)
racket_b = Racket2('racket_blue.png', 580, 180, 100, 165, 5)
ball = GameSprite('ball.png', W//2-50, H//2, 50, 50, 0)

font.init()
font = font.Font(None, 35)
win1 = font.render('PLAYER 1 WON!', True, (180, 0, 0))
win2 = font.render('PLAYER 2 WON!', True, (180, 0, 0))
restart_game = font.render("PRESS SPACE TO RESTART GAME!", True, (0, 0, 0))

speed_y = 3
speed_x = 3

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        ball.rect.y += speed_y
        ball.rect.x += speed_x       
        racket_r.update()
        racket_r.reset()
        racket_b.update()
        racket_b.reset()
        ball.reset()

        if ball.rect.y > H-50 or ball.rect.y < 0:
            speed_y *= -1

        if sprite.collide_rect(racket_r, ball) and speed_x < 0:
            speed_x *= -1
            speed_y *= 1

        if sprite.collide_rect(racket_b, ball) and speed_x > 0:
            speed_x *= -1
            speed_y *= 1 

        if ball.rect.x < 0:
            finish = True
            window.blit(win2, (200, 200))

        if ball.rect.x > W:
            finish = True
            window.blit(win1, (200, 200))
    else:
        window.blit(restart_game, (150, H-40))
        keys = key.get_pressed()
        if keys[K_SPACE]:
            ball.rect.y = H//2
            ball.rect.x = W//2
            finish = False


    display.update()
    clock.tick(FPS)

    



