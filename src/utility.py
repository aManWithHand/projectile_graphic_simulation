import os
import pygame


class Utillity:
    @staticmethod
    def load_png(name: str) -> pygame.Surface | pygame.Rect:
        fullname = os.path.join("pic", name)
        fullname = os.path.join(os.getcwd(),fullname)
        try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
        except FileNotFoundError:
            print(f"Cannot load image: {fullname}")
            raise SystemExit
        return image, image.get_rect()