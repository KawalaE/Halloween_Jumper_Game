import pygame
from random import randint
from image_manager import ImageManager
from math import sin


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, kind: str, img_mng: ImageManager, score):
        super().__init__()
        self.score = score
        self.img_manager = img_mng
        self.kind = kind
        if kind == 'ghost':
            self.frames = [self.img_manager.ghost_1, self.img_manager.ghost_2, self.img_manager.ghost_3,
                           self.img_manager.ghost_4]
            y_pos = 490
        elif kind == "witch":
            self.frames = [self.img_manager.witch_1, self.img_manager.witch_2, self.img_manager.witch_3,
                           self.img_manager.witch_4]
            y_pos = 400

        else:
            self.frames = [self.img_manager.bat_1, self.img_manager.bat_2, self.img_manager.bat_3,
                           self.img_manager.bat_4]
            y_pos = 299

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(960, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):
            self.animation_index = 0
        else:
            self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= (self.score+1)**-2 + 5
        if self.kind == "bat":
            self.rect.y += 1
        elif self.kind == "witch":
            self.rect.y = 290+sin(self.rect.x/50)*10
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

