import pygame
from os import walk


class ImageManager:
    def __init__(self):
        self.icon = (pygame.image.load('Graphics/Entities/icon.png'))
        self.background_images = []

    def load_image(self, path: str) -> list[pygame.Surface]:
        image_list = []
        pictures = list(walk(path))[0][2]
        for pic in pictures:
            image = pygame.image.load(f"{path}/{pic}").convert_alpha()
            image_list.append(image)
        return image_list
