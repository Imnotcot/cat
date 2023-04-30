import systemfile
import playerfile
import enemyfile
import pygame

pygame.init()

class Shoot:
    def __init__(self):
        self.Pshoots = []
        self.Eshoots = []

    def init(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir
        self.speed = 15
        if dir == 'up' or dir =='down':
            self.SURF = pygame.image.load('img/shoot/Shoot_Up-Down.png')
        elif dir == 'right' or dir == 'left':
            self.SURF = pygame.image.load('img/shoot/Shoot_Right-Left.png')

    def moving(self):
        if self.dir == 'up':
            self.y -= self.speed
        elif self.dir == 'down':
            self.y += self.speed
        elif self.dir == 'right':
            self.x += self.speed
        elif self.dir == 'left':
            self.x -= self.speed
        if self.x < 0 or self.x > systemfile.system.screen_with or self.y < 0 or self.y > systemfile.system.screen_hight:
            self.delete()


class Player_shoot(Shoot):
    def __init__(self, x, y, dir):
        self.init(x, y, dir)

    def delete(self):
        systemfile.system.shoot.Pshoots.remove(self)


class Enemy_shoot(Shoot):
    def __init__(self, x, y, dir):
        self.init(x, y, dir)

    def delete(self):
        systemfile.system.shoot.Eshoots.remove(self)


systemfile.system.shoot = Shoot()
