import pygame

class Bird:
    def __init__(self, sprite_path, position, speed_limit=250) -> None:
        """Initializes Bird constructor

        Args:
            sprite_path (string): The path of the sprite the bird will be
            position (tuple): Bird position on the screen
            speed_limit (number): Determines the speed limit the bird can reach.
        """
        self.sprite_path = sprite_path
        self.position = position

        self.surface = pygame.image.load(self.sprite_path).convert()
        self.surface = pygame.transform.scale2x(self.surface)

        self.rect = self.surface.get_rect(center = self.position)
        self.speed = 0
        self.speed_limit = speed_limit

    def animate(self, gravity) -> None:
        """[Animates applying physics to it ]

        Args:
            gravity (number): [Determines the gravity force acting upon the bird.]
        """
        self.speed += gravity
        if self.speed >= self.speed_limit:
            self.speed = self.speed_limit

        self.rect.centery += self.speed

        
    def flap(self, flap_power) -> None:
        """[Makes the bird flap.The height that will fly depends on flap_power]

        Args:
            flap_power (number): [Determines the height of the flap]
        """

        self.speed = 0 
        self.speed -= flap_power

        if self.speed >= self.speed_limit:
            self.speed = self.speed_limit

        if self.speed <= -self.speed_limit:
            self.speed = -self.speed_limit
