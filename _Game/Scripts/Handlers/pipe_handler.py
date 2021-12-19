from random import randint
from random import choice
from typing import Tuple
import pygame

from _Game.Scripts.Options.game_variables import variables as v
from _Game.Scripts.Objects.Pipe import Pipe


SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, v["spawn_pipe_timer"])

def spawn_pipe(event,pipe_list_limit=12,pipe_list=[]) -> list:
    """Spawn a pipe.

    Args:
        event (pygame.event.get()): pygame event
        pipe_list (list): The list that will return
        pipe_list_limit (int): The maximum number of pipes that are able to be inside the pipe_list
    """
    
    if event.type == SPAWNPIPE:

        pipe_list.extend(create_pipes())
        
        if len(pipe_list) >= pipe_list_limit:
            pipe_list.pop(0)

    return pipe_list


def create_pipes(randint_modifier=(-220,220), random_pipe_sprites=v["random_pipe_sprites"]) -> Tuple:
    """Creates a new pipe

    Args:
        randint_modifier (tuple): Tuple value to be used in randint to modify Y position of the pipes.
    """
    if random_pipe_sprites:
        pipe_sprites = ["_Game/Images/pipe-green.png","_Game/Images/pipe-red.png"]
        sprite = choice(pipe_sprites)

    if not random_pipe_sprites:
        sprite = "_Game/Images/pipe-green.png"

    y_modifier = randint(randint_modifier[0],randint_modifier[1])

    bottom = (700,910+y_modifier)
    top = (700,0+y_modifier)

    bottom_pipe = Pipe(sprite, bottom)
    top_pipe = Pipe(sprite, top)
    top_pipe.surface = pygame.transform.flip(top_pipe.surface, False, True)
    

    return bottom_pipe,top_pipe


def pipes_animation(pipe_list) -> None:
    """Animates each pipe from the list.

    Args:
        pipe_list (list[Pipes]): A list containing Pipes objects to be animated
    """
    for pipe in pipe_list:
        pipe.animate(v["world_speed"])

def pipes_blit(pipe_list, screen) -> None:
    """Draws the pipes surfaces on the screen.

    Args:
        pipe_list (list[Pipes]): A list containing Pipes objects to be drawn
        screen (pygame.display.set_mode(screen_size)): The screen you want to draw the pipes on
    """
    for pipe in pipe_list:
        screen.blit(pipe.surface,pipe.rect)


