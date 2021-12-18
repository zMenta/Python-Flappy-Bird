
def bird_out_of_bounds(bird_rect, bottom_limit=850, top_limit=-100) -> bool:
    """Checks if the bird is out of bounds of a specific screen heights.

    Args:
        bird_rect (Bird.rect): The bird that you want to check if his rect is out of bounds of the screen
        bottom_limit (number): The screen position limit of the bottom.
        top_limit (number): The screen position limit of the top.

    """
    if bird_rect.top <= top_limit or bird_rect.bottom >= bottom_limit:
        return True

    return False