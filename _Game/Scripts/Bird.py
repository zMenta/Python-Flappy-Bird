import pygame

class Bird:
    def __init__(self, sprite_path, position) -> None:
        """Initializes Bird constructor

        Args:
            sprite_path (string): The path of the sprite the bird will be
            position (tuple): Bird position on the screen
        """
        self.sprite_path = sprite_path
        self.position = position

        self.surface = pygame.image.load(self.sprite_path).convert()
        self.surface = pygame.transform.scale2x(self.surface)
        
        self.rect = self.surface.get_rect(center = self.position)
        