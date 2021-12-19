import pygame
from _Game.Scripts.Options.game_variables import variables as v
pygame.init()

class Pipe:
    def __init__(self, sprite_path, position) -> None:
        """Pipe class

        Args:
            sprite_path (str): [The path of the sprite]
            position (tuple): [Position of the pipe, center]
        """
        self.sprite_path = sprite_path
        self.position = position

        self.surface = pygame.image.load(sprite_path).convert()
        if v["screen_size"] == (576,1024):
            self.surface = pygame.transform.scale2x(self.surface)

        self.rect = self.surface.get_rect(center = self.position)


    def animate(self, speed) -> None:
        """Animates the pipe from right to left.

        Args:
            speed (number): Determines the speed of the pipe.
        """

        self.rect.centerx -= speed