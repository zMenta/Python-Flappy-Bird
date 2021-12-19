import sys
import pygame 
pygame.init()

from _Game.Scripts.Objects.Bird import Bird
from _Game.Scripts.Objects.Floor import Floor
from _Game.Scripts.Options.game_variables import variables as v
import _Game.Scripts.Handlers.pipe_handler as pipe_handler
import _Game.Scripts.Handlers.bird_handler as bird_handler

def main():
    
    screen = pygame.display.set_mode(v["screen_size"])
    screen_values = v["screen_size"]
    clock = pygame.time.Clock()

    bg_surface = pygame.image.load("_Game/Images/background-day.png").convert()
    if v["screen_size"] == (576,1024):
        bg_surface = pygame.transform.scale2x(bg_surface)

    floor = Floor("_Game/Images/base.png", screen)
    bird = Bird("_Game/Images/yellowbird-midflap.png",(screen_values[0]/5,screen_values[1]/2), 20)

    #Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE:
                    bird.flap(9)

            pipe_list = pipe_handler.spawn_pipe(event) 

        screen.blit(bg_surface,(0,0))
        screen.blit(bird.surface,bird.rect)
        pipe_handler.pipes_blit(pipe_list, screen)

        floor.animate(v["world_speed"],screen.get_height() - floor.surface_1.get_height()/2)
        pipe_handler.pipes_animation(pipe_list)
        bird.animate(v["gravity"])

        if bird_handler.bird_out_of_bounds(bird.rect, screen.get_height() - floor.surface_1.get_height()/2, screen.get_height()*1.2 ):
            print("OUT OF BOUNDS")

        pygame.display.update()
        clock.tick(v["fps_limit"])

if __name__ == "__main__":
    main()