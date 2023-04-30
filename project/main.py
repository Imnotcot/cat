import pygame
from sys import exit

import systemfile

import shootfile
import playerfile
import enemyfile

pygame.init()
i = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if i == 20:
                if event.key == pygame.K_SPACE:
                    systemfile.system.player.to_shoot()
                    i = 0
            else:
                i += 1
    print(i == 20)
    systemfile.system.player.move(pygame.key.get_pressed())

    systemfile.system.screen.blit(systemfile.system.backgroud.surf, (0, 0))

    systemfile.system.paint.enemy_shoots()
    systemfile.system.paint.player_shoots()
    systemfile.system.paint.enemys()

    systemfile.system.screen.blit(systemfile.system.player.surf, (systemfile.system.player.x, systemfile.system.player.y))

    pygame.display.update()
    systemfile.system.clock.tick(30)
