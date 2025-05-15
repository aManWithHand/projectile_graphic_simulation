from throwable_object import ThrowableObject


class Ball(ThrowableObject):
    def __init__(self,
                 position: tuple = (0,0), 
                 speed: tuple = (0,0), 
                 gravity: tuple = (0,100)):
        super().__init__(image="ball.jpg", position=position, speed=speed, gravity=gravity)