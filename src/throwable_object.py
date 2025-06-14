from pygame.sprite import Sprite
from pygame.math import Vector2
import pygame
from utility import Utillity as util

class ThrowableObject(Sprite):

    """A base class for moving object by initial speed
    Returns: self
    Functions: update
    Attributes: speed, image, rect, area"""

    def __init__(self,
                 image: str, 
                 position: tuple = (0,0),
                 speed: tuple = (0,0),
                 gravity: tuple = (0,100),
                 *groups):
        super().__init__(*groups)
        self.speed = Vector2(speed)
        self.image, self.rect = util.load_png(image)
        self.rect.center = position
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.gravity = Vector2(gravity)
        self.position = Vector2(self.rect.center)

    def update(self, delta, *args, **kwargs):
        self._move(delta)
        
    def _move(self, delta) -> None:
        #self.rect = self.rect.move((self.speed - Vector2(0,self.gravity)* delta) * delta)
        # self.rect.center =  self.rect.center + self.speed * delta
        # self.rect.center = Vector2(self.start_position) + self.speed * time + self.gravity * time * time
        self.speed += self.gravity * delta
        self.position += self.speed * delta
        self.rect.center = self.position