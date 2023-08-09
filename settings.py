import pygame

# Height of 11
level1 = ['                                     ',
          ' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
          ' x                                  x',
          ' x c                              c x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x               c                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                             p    x',
          ' x                                  x',
          ' xddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
          '                                     ']
level1_data = {(3, 3) : 'Map', (3, 34) : 'Sword'}

level2 = ['                                     ',
          ' xddxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
          ' x p                                x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                                  x',
          ' x                              c   x',
          ' xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
          '                                     ']
level2_data = {(20, 32) : 'Armor'}

levels = [level1, level2]

tile_size = 32

SCREEN_WIDTH = 1180
SCREEN_HEIGHT = 700

player_group = pygame.sprite.GroupSingle()


