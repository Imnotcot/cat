import systemfile
import shootfile
import pygame

pygame.init()

class Player:
    def __init__(self):
        self.surf = pygame.image.load('img/player/Player_Up.png').convert_alpha()
        self.x = 0
        self.y = 0
        self.dir = 'up'
        self.fast = 10

    def move(self, keys):
        if keys[pygame.K_w]:
            self.y -= self.fast
            self.surf = pygame.image.load('img/player/Player_Up.png').convert_alpha()
            self.dir = 'up'
        elif keys[pygame.K_s]:
            self.y += self.fast
            self.surf = pygame.image.load('img/player/Player_Down.png').convert_alpha()
            self.dir = 'down'
        elif keys[pygame.K_d]:
            self.x += self.fast
            self.surf = pygame.image.load('img/player/Player_Right.png').convert_alpha()
            self.dir = 'right'
        elif keys[pygame.K_a]:
            self.x -= self.fast
            self.surf = pygame.image.load('img/player/Player_Left.png').convert_alpha()
            self.dir = 'left'

    def to_shoot(self):
        systemfile.system.shoot.Pshoots.append(shootfile.Player_shoot(self.x, self.y, self.dir))


screen = systemfile.system.screen
systemfile.system.player = Player()