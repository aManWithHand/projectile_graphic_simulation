from throwable_object import ThrowableObject


class Ball(ThrowableObject):
    def __init__(self, speed: tuple = (0,0)):
        super().__init__(image="ball.jpg", speed=speed)