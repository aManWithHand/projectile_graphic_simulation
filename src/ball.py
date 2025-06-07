import os
from throwable_object import ThrowableObject

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "img")

class Ball(ThrowableObject):
    def __init__(self,
                 position: tuple = (0,0), 
                 speed: tuple = (0,0), 
                 gravity: tuple = (0,100)):
        
        super().__init__(image= os.path.join(IMAGE_DIR, "ball.png"),
                         position= position,
                         speed= speed,
                         gravity= gravity)