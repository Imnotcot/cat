import pygame

pygame.init()

class System:
    def __init__(self):
        pygame.init()


        self.screen_with = 1550
        self.screen_hight  = 800

        self.screen = pygame.display.set_mode((self.screen_with, self.screen_hight))
        pygame.display.set_caption('Shooter')
        self.clock = pygame.time.Clock()

    def init(self):
        self.backgroud = Background()
        self.paint = Painter()


class Painter:
    def enemy_shoots(self):
        for element in system.shoot.Eshoots:
            element.moving()
            system.screen.blit(element.SURF, (element.x, element.y))

    def player_shoots(self):
        for element in system.shoot.Pshoots:
            element.moving()
            system.screen.blit(element.SURF, (element.x, element.y))

    def enemys(self):
        for element in system.enemys:
            element.move()
            print(element.surf)
            system.screen.blit(element.surf, (element.x, element.y))


class Background:
    def __init__(self):
        self.surf = pygame.image.load('img/Background.png')


system = System()
system.init()

import playerfile
import shootfile
import enemyfile

system.enemys.append(enemyfile.Enemy())