import pygame
from image_manager import ImageManager


class Player(pygame.sprite.Sprite):
    def __init__(self, img_mng: ImageManager):
        super().__init__()  # initializing Sprite Class
        self.img_manager = img_mng
        self.image = self.img_manager.player_stand
        self.rect = self.image.get_rect(midbottom=(100, 300))

        self.player_walk = [self.img_manager.player_walk_1, self.img_manager.player_walk_2]

        self.gravity = 0
        self.player_index = 0

        self.jump_sound = pygame.mixer.Sound('Audio/Jump.wav')
        self.jump_sound.set_volume(0.5)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 490:
            self.gravity = -20
            self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 490:
            self.rect.bottom = 490

    def player_animation(self):
        if self.rect.bottom < 490:
            self.image = self.img_manager.player_jump
        else:
            self.player_index += 0.1
            if self.player_index > len(self.player_walk):
                self.player_index = 0
            else:
                self.image = self.player_walk[int(self.player_index)]

    def update(self):

        self.player_input()
        self.apply_gravity()
        self.player_animation()


