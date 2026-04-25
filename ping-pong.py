from random import randint 
from pygame import *

mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.size_x = size_x
        self.size_y = size_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

      
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()         
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

height = 600
width = 800

screen = display.set_mode((width, height))
display.set_caption('ping-pong')
clock = time.Clock()
FPS = 60

background = transform.scale(image.load("galaxy.jpg"), (width, height))
player1 = Player('rocket.png', 200, 400, 4, 80, 50)
player2= Player('rocket.png', 400, 400, 4, 80, 50)

run = True
finish = False
while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
    if not finish: 
        screen.blit(background, (0, 0))
        player1.update()
        player1.reset
        player2.update()
        player2.reset
        display.update()
    clock.tick(FPS)
 