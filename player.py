import pygame
import random as r

from settings import *

class Player(pygame.sprite.Sprite):
    characters = ['red', 'blue', 'white']
    def __init__(self, location = (SCREEN_HEIGHT / 2, SCREEN_WIDTH / 2), username = 'Player', character = (characters[r.randint(0, 2)])):
        super().__init__()
        self.location = location
        self.username = username
        self.character = character
        self.timer = 0

        self.image_list = [pygame.image.load('player_models/player1.png'), pygame.image.load('player_models/player2.png')]
        self.image = pygame.transform.smoothscale(self.image_list[0], (50, 50))
        self.rect = self.image.get_rect(center = (self.location))

    def animate(self):
        self.timer += .1
        if (int(self.timer) == 5):
            self.image = pygame.transform.smoothscale(self.image_list[1], (50, 50))
        elif (int(self.timer) >= 10):
            self.image = pygame.transform.smoothscale(self.image_list[0], (50, 50))
            self.timer = 0

    def keybind(self):
        if (pygame.key.get_pressed()[pygame.K_w]):
            self.rect.y -= 5
        elif (pygame.key.get_pressed()[pygame.K_s]):
            self.rect.y += 5
        elif (pygame.key.get_pressed()[pygame.K_d]):
            self.rect.x += 5
        elif (pygame.key.get_pressed()[pygame.K_a]):
            self.rect.x -= 5

    def update(self):
        self.keybind()
        self.animate()