import pygame

from settings import *
from inventory import *

class Door(pygame.sprite.Sprite):
    def __init__(self, location, item = "None", opened = False, collidable = True):
        super().__init__()
        self.location = location
        self.item = item
        self.collidable = collidable

        self.image = pygame.image.load('object_models/chest_close.png')
        self.rect = self.image.get_rect(center = (self.location))

    def next_level(self):
        pass
    
    def collide(self):
        if (self.collidable == True):
            player_list = pygame.sprite.spritecollide(self, player_group, False)
            collision_tolerance = 6
            for player in player_list:
                if (self.rect.colliderect(player.rect)):
                    if (abs(self.rect.top - player.rect.bottom) < collision_tolerance):
                        player.rect.y -= 5
                    if (abs(self.rect.bottom - player.rect.top) < collision_tolerance):
                        player.rect.y += 5
                    if (abs(self.rect.left - player.rect.right) < collision_tolerance):
                        player.rect.x -= 5
                    if (abs(self.rect.right - player.rect.left) < collision_tolerance):
                        player.rect.x += 5
                    self.next_level()

    def update(self):
        self.collide()

class Chest(pygame.sprite.Sprite):
    def __init__(self, location, item = "None", opened = False, collidable = True):
        super().__init__()
        self.location = location
        self.item = item
        self.opened = opened
        self.collidable = collidable

        self.image = pygame.image.load('object_models/chest_close.png')
        self.rect = self.image.get_rect(center = (self.location))

    def open(self):
        if (self.opened == False):  
            self.image = pygame.image.load('object_models/chest_open.png')
            self.rect = self.image.get_rect(center = (self.location))
            inventory_list.append(self.item)
            print(self.item)
            self.opened = True
    
    def collide(self):
        if (self.collidable == True):
            player_list = pygame.sprite.spritecollide(self, player_group, False)
            collision_tolerance = 6
            for player in player_group:
                if (self.rect.colliderect(player.rect)):
                    if (abs(self.rect.top - player.rect.bottom) < 6):
                        player.rect.y -= 5
                    if (abs(self.rect.bottom - player.rect.top) < 6):
                        player.rect.y += 5
                    if (abs(self.rect.left - player.rect.right) < 6):
                        player.rect.x -= 5
                    if (abs(self.rect.right - player.rect.left) < 6):
                        player.rect.x += 5
                    self.open()

    def update(self):
        self.collide()