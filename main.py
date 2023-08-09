import pygame
import random as r

from player import *
from obstacles import *
from settings import *
from tile import *

from sys import exit, platform

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Slime Factory')
pygame.display.set_icon(pygame.image.load('interface/icon.png'))

clock = pygame.time.Clock()

l1 = Level(level1, screen)
l2 = Level(level2, screen)

levels = [l1, l2]
level = levels[0]

def refresh():

    screen.fill('black')

    level.run()

while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            exit()

    refresh()

    pygame.display.flip()
    clock.tick(60)