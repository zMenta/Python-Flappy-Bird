"""
File containing general setup of the game.
"""

screen_resolutions = {
    "288x512": (288,512),
    "576x1024": (576,1024)
}

variables = {
    "fps_limit": 120,
    "screen_size": screen_resolutions["288x512"],
    "gravity": 0.25,
    "world_speed": 2,
    "spawn_pipe_timer": 1200,
    "random_pipe_sprites": True
}
