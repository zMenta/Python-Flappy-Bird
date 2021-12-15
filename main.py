import sys
import pygame

from _Game.Scripts.Floor import Floor

def main():
    screen = pygame.display.set_mode((576,1024))
    clock = pygame.time.Clock()

    bg_surface = pygame.image.load("_Game/Images/background-day.png").convert()
    bg_surface = pygame.transform.scale2x(bg_surface)

    floor_surface = Floor("_Game/Images/base.png", screen)

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        screen.blit(bg_surface,(0,0))
        floor_surface.animate(1.3,850)


        pygame.display.update()
        clock.tick(120)

if __name__ == "__main__":
    main()