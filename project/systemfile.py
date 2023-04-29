import pygame


class System:
    def __init__(self):
        pygame.init()


        self.screen_with = 1550
        self.screen_hight  = 800

        self.screen = pygame.display.set_mode((self.screen_with, self.screen_hight))
        pygame.display.set_caption('Shooter')
        self.clock = pygame.time.Clock()

    def create(self):
        self.backgroud = Background()


class Background:
    def __init__(self):
        self.surf = pygame.image.load('img/Background.png')


system = System()
system.create()
import playerfile
import shootfile