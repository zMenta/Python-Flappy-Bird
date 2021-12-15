from random import randint
import pygame

from _Game.Scripts._game_variables import variables as v
from _Game.Scripts.Pipe import Pipe


SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, v["spawn_pipe_timer"])

def spawn_pipe(event,randint_modifier=(-220,220),pipe_list=[]):
    """Spawn a pipe.

    Args:
        event (pygame.event.get()): pygame event
        randint_modifier (tuple): Tuple value to be used in randint to modify Y position of the pipes.
    """
    
    if event.type == SPAWNPIPE:
        y_modifier = randint(randint_modifier[0],randint_modifier[1])

        flip = False
        pipe_list.append(create_pipe(y_modifier,flip))
        flip = not flip
        pipe_list.append(create_pipe(y_modifier,flip))

        if len(pipe_list) >= 12:
            pipe_list.pop(0)

    return pipe_list


def create_pipe(y_modifier,flip=False):
    """Creates a new pipe
    """
    bottom = (700,900+y_modifier)
    top = (700,0+y_modifier)

    if flip == False:
        pipe = Pipe("_Game/Images/pipe-green.png", bottom)

    if flip == True:
        pipe = Pipe("_Game/Images/pipe-green.png", top)
        pipe.surface = pygame.transform.flip(pipe.surface, False, True)
    

    return pipe


def pipes_animation(pipe_list):
    """Animates each pipe from the list.

    Args:
        pipe_list (list[Pipes]): A list containing Pipes objects to be animated
    """
    for pipe in pipe_list:
        pipe.animate(v["world_speed"])

def pipes_blit(pipe_list, screen):
    """Draws the pipes surfaces on the screen.

    Args:
        pipe_list (list[Pipes]): A list containing Pipes objects to be drawn
        screen (pygame.display.set_mode(screen_size)): The screen you want to draw the pipes on
    """
    for pipe in pipe_list:
        screen.blit(pipe.surface,pipe.rect)


