import sys
import pygame

def main():
    screen = pygame.display.set_mode((576,1024))
    clock = pygame.time.Clock()

    bg_surface = pygame.image.load("_Game/Images/background-day.png").convert()
    bg_surface = pygame.transform.scale2x(bg_surface)

    floor_surface = pygame.image.load("_Game/Images/base.png").convert()
    floor_surface = pygame.transform.scale2x(floor_surface)
    floor_surface2 = pygame.image.load("_Game/Images/base.png").convert()
    floor_surface2 = pygame.transform.scale2x(floor_surface2)

    floor1_x_pos = 0
    floor2_x_pos = 576

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(bg_surface,(0,0))
        floor1_x_pos -= 2
        floor2_x_pos -= 2
        if floor2_x_pos <= -floor_surface.get_width():
            floor2_x_pos = 576

        if floor1_x_pos <= -floor_surface.get_width():
            floor1_x_pos = 576

        screen.blit(floor_surface,(floor1_x_pos,850))
        screen.blit(floor_surface2,(floor2_x_pos,850))


        pygame.display.update()
        clock.tick(120)

if __name__ == "__main__":
    main()