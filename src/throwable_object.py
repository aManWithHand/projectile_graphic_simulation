from pygame.sprite import Sprite
from pygame.math import Vector2
import pygame
import utility as util

class ThrowableObject(Sprite):

    """A base class for moving object by initial speed
    Returns: -
    Functions: update
    Attributes: speed, image, rect, area"""

    def __init__(self, image: str, speed: tuple = (0,0), *groups):
        super().__init__(*groups)
        self.speed = Vector2(speed)
        self.image, self.rect = util.load_png(image)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()

    def update(self, *args, **kwargs):
        self._move()

    def _move() -> None:
        pass