import sys
import pygame 
pygame.init()

from _Game.Scripts.Bird import Bird
from _Game.Scripts.Floor import Floor
from _Game.Scripts.Pipe import Pipe
from _Game.Scripts._game_variables import variables as v
import _Game.Scripts._pipe_handler as _pipe_handler

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

            pipe = Pipe("_Game/Images/pipe-green.png", (400,900))   
            pipe_list = _pipe_handler.spawn_pipe(event,pipe)
            print(pipe_list)

        screen.blit(bg_surface,(0,0))
        screen.blit(bird.surface,bird.rect)
        # screen.blit(pipe.surface,pipe.rect) 
        _pipe_handler.pipes_blit(pipe_list, screen)

        floor.animate(v["world_speed"],850)
        # pipe.animate(v["world_speed"])
        _pipe_handler.pipes_animation(pipe_list)
        bird.animate(v["gravity"])
 

        pygame.display.update()
        clock.tick(v["fps_limit"])

if __name__ == "__main__":
    main()