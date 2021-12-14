import pygame
from pygame import surface

screen = pygame.display.set_mode((576,1024))

class Floor:
    """
    Floor class and it's method to draw
    """
    def __init__(self, path) -> None:
        self.path = str(path)
        self.surface_1 = pygame.image.load(self.path).convert()
        self.surface_1 = pygame.transform.scale2x(self.surface_1)
        self.surface_2 = pygame.image.load(self.path).convert()
        self.surface_2 = pygame.transform.scale2x(self.surface_2)

    def animate(self, speed, screen_size=576):
        floor1_x_pos = 0
        floor2_x_pos = screen_size
        floor1_x_pos -= speed
        floor2_x_pos -= speed
        if floor1_x_pos <= -self.surface_1.get_width():
            floor1_x_pos = 576
        
        if floor2_x_pos <= -self.surface_2.get_width():
            floor2_x_pos = 576

        screen.blit(self.surface_1,(floor1_x_pos,850))
        screen.blit(self.surface_2,(floor2_x_pos,850))
