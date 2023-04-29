import pygame
from sys import exit

import systemfile

import shootfile
import playerfile

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                systemfile.system.player.to_shoot()

    systemfile.system.player.move(pygame.key.get_pressed())

    systemfile.system.screen.blit(systemfile.system.backgroud.surf, (0, 0))
    for element in systemfile.system.shoot.Pshoots:
        element.moving()
        systemfile.system.screen.blit(element.SURF, (element.x, element.y))
    systemfile.system.screen.blit(systemfile.system.player.surf, (systemfile.system.player.x, systemfile.system.player.y))

    pygame.display.update()
    systemfile.system.clock.tick(30)
