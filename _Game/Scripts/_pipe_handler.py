import pygame

from _Game.Scripts._game_variables import variables as v
from _Game.Scripts.Pipe import Pipe


SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, v["spawn_pipe_timer"])

def spawn_pipe(event,pipe,pipe_list=[]):
    """Spawn a pipe.

    Args:
        event (pygame.event.get()): pygame event
        pipe (Pipe): Pipe object
    """
    if event.type == SPAWNPIPE:
        pipe_list.append(create_pipe(pipe))
        
        if len(pipe_list) >= 6:
            pipe_list.pop(0)

    return pipe_list


def create_pipe(pipe):
    """Create a new pipe
    """
    return pipe


def pipes_animation(pipe_list):
    """animates each pipe from the list.

    Args:
        pipe_list (list[Pipes]): A list containing Pipes objects to be animated
    """
    for pipe in pipe_list:
        pipe.animate(v["world_speed"])

def pipes_blit(pipe_list, screen):
    """Draws the pipe surfaces on the screen.

    Args:
        pipe_list (list[Pipes]): A list containing Pipes objects to be drawn
        screen (pygame.display.set_mode(screen_size)): The screen you want to draw the pipes on
    """
    for pipe in pipe_list:
        screen.blit(pipe.surface,pipe.rect)


