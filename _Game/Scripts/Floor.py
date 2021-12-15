import pygame

screen = pygame.display.set_mode((576,1024))

class Floor:
    """
    Floor class and it's method to draw
    """
    def __init__(self, path, screen) -> None:
        """[summary]

        Args:
            path ([type]): Path for the image sprite of the floor
            screen (pygame.display.set_mode((width,height))): Determines the screen
        """
        self.path = path
        self.screen = screen
        self.floor_x_pos = 0

        self.surface_1 = pygame.image.load(self.path).convert()
        self.surface_1 = pygame.transform.scale2x(self.surface_1)
        self.surface_2 = pygame.image.load(self.path).convert()
        self.surface_2 = pygame.transform.scale2x(self.surface_2)


    def animate(self,speed, floor_y_position):
        """Animates the floor from right to left.

        Args:
            speed (number): Determines the speed of the animation
        """
        self.floor_x_pos -= speed
        if self.floor_x_pos <= -self.surface_1.get_width():
            self.floor_x_pos = 0

        self.screen.blit(self.surface_1,(self.floor_x_pos,floor_y_position))
        self.screen.blit(self.surface_2,(self.floor_x_pos + screen.get_width(),floor_y_position))
