import pygame

from settings import *
from obstacles import *
from player import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('interface/tile.png').convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (size, size))
        self.rect = self.image.get_rect(center = pos)

    def collide(self):
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

    def update(self):
        self.collide()

class Level():
    def __init__(self, level, surface):
        self.display_surface = surface
        self.setup(level)

    def setup(self, layout):
        self.tile_group = pygame.sprite.Group()
        self.obstacle_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                if (cell == 'x'):
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tile_group.add(tile)
                if (cell == 'c'):
                    x = col_index * tile_size
                    y = row_index * tile_size
                    chest = Chest((x, y), level1_data.get((row_index, col_index)))
                    self.obstacle_group.add(chest)
                if (cell == 'p'):
                    x = col_index * tile_size
                    y = row_index * tile_size
                    p1 = Player((x, y))
                    player_group.add(p1)
                    

    def run(self):
        self.tile_group.draw(self.display_surface)
        self.tile_group.update()
        self.obstacle_group.draw(self.display_surface)
        self.obstacle_group.update()
        player_group.draw(self.display_surface)
        player_group.update()