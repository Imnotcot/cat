import systemfile
import playerfile
import shootfile
import pygame
import random

pygame.init()

class Enemy:
    def __init__(self):
        self.x = random.randint(0, systemfile.system.screen_with)
        self.y = random.randint(0, systemfile.system.screen_hight)
        self.dir = 'up'
        self.speed = 5
        self.i = 0
        self.surf = pygame.image.load('img/enemy/Enemy_Up.png').convert_alpha()

    def move(self):
        if systemfile.system.player.x > self.x and not abs(systemfile.system.player.x-self.x) < 10:
            self.x += self.speed
            self.surf = pygame.image.load('img/enemy/Enemy_Right.png').convert_alpha()
            self.dir = 'right'
        elif systemfile.system.player.x < self.x and not abs(systemfile.system.player.x-self.x) < 10:
            self.x -= self.speed
            self.surf = pygame.image.load('img/enemy/Enemy_Left.png').convert_alpha()
            self.dir = 'left'
        elif systemfile.system.player.y > self.y and not abs(systemfile.system.player.y-self.y) < 10:
            self.y += self.speed
            self.surf = pygame.image.load('img/enemy/Enemy_Down.png').convert_alpha()
            self.dir = 'down'
        elif systemfile.system.player.y < self.y and not abs(systemfile.system.player.y-self.y) < 10:
            self.y -= self.speed
            self.surf = pygame.image.load('img/enemy/Enemy_Up.png').convert_alpha()
            self.dir = 'up'

        if self.i == 20:
            systemfile.system.shoot.Eshoots.append(shootfile.Enemy_shoot(self.x, self.y, self.dir))
            self.i = 0
        else:
             self.i += 1

systemfile.system.enemys = []
