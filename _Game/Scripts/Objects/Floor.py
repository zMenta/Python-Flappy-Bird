import pygame
from _Game.Scripts.Options.game_variables import variables as v

class Floor:
    """
    Floor class and it's method to draw
    """
    def __init__(self, sprite_path, screen) -> None:
        """[summary]

        Args:
            sprite_path ([type]): sprite_path for the image sprite of the floor
            screen (pygame.display.set_mode((width,height))): Determines the screen
        """
        self.sprite_path = sprite_path
        self.screen = screen
        self.floor_x_pos = 0

        self.surface_1 = pygame.image.load(self.sprite_path).convert()
        self.surface_2 = pygame.image.load(self.sprite_path).convert()
        if v["screen_size"] == (576,1024):
            self.surface_1 = pygame.transform.scale2x(self.surface_1)
            self.surface_2 = pygame.transform.scale2x(self.surface_2)


    def animate(self,speed, floor_y_position):
        """Animates the floor from right to left.

        Args:
            speed (number): Determines the speed of the animation
            floor_y_position (number): Determines the y position of the floor.
        """
        self.floor_x_pos -= speed
        if self.floor_x_pos <= -self.surface_1.get_width():
            self.floor_x_pos = 0

        self.screen.blit(self.surface_1,(self.floor_x_pos,floor_y_position))
        self.screen.blit(self.surface_2,(self.floor_x_pos + self.screen.get_width(),floor_y_position))
