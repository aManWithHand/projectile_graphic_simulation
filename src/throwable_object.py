from pygame.sprite import Sprite
from pygame.math import Vector2

class ThrowableObject(Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.a = Vector2

    def update(self, *args, **kwargs):
        pass