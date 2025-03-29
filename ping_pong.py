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



class Ball(GameSprite):
    def update(self):
        pass

racket_r = Racket1('racket_red.png', 0, 180, 130, 200, 5)
racket_b = Racket2('racket_blue.png', 580, 180, 100, 165, 5)

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket_r.update()
        racket_r.reset()
        racket_b.update()
        racket_b.reset()
    
    display.update()
    clock.tick(FPS)

    



