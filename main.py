import sys
import pygame

screen = pygame.display.set_mode((576,1024))
clock = pygame.time.Clock()

#Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    clock.tick(60)