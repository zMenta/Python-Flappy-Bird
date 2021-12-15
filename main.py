import sys
import pygame

from _Game.Scripts.Bird import Bird
from _Game.Scripts.Floor import Floor
from _Game.Scripts._game_variables import variables as v

def main():
    screen = pygame.display.set_mode(v["screen_size"])
    clock = pygame.time.Clock()

    bg_surface = pygame.image.load("_Game/Images/background-day.png").convert()
    bg_surface = pygame.transform.scale2x(bg_surface)

    floor = Floor("_Game/Images/base.png", screen)
    bird = Bird("_Game/Images/yellowbird-midflap.png",(100,512), 20)

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.flap(12)


        screen.blit(bg_surface,(0,0))
        screen.blit(bird.surface,bird.rect)

        print(bird.speed)

        floor.animate(2,850)
        bird.animate(v["gravity"])


        pygame.display.update()
        clock.tick(v["fps_limit"])

if __name__ == "__main__":
    main()