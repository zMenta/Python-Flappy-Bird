import pygame

from _Game.Scripts._game_variables import variables as v
from _Game.Scripts.Pipe import Pipe


SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, v["spawn_pipe_timer"])

def spawn_pipe(event,pipe_rect,pipe_list=[]):
    """Spawn a pipe.

    Args:
        event (pygame.event.get()):
    """
    list(pipe_list)
    if event.type == SPAWNPIPE:
        pipe_list.append(create_pipe(pipe_rect))
        print(pipe_list)

        if len(pipe_list) >= 6:
            pipe_list.pop(0)


def create_pipe(pipe_rect):
    """Create a new pipe
    """

    print("PIPE CREATED")
    print(pipe_rect)
    return pipe_rect


