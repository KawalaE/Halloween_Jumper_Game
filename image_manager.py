import pygame
from os import walk


class ImageManager:
    def __init__(self):
        self.background_images = self.load_image('Graphics/Background/layers')
        self.game_icon = (pygame.image.load('Graphics/Entities/icon.png'))
        self.tombstone = pygame.image.load('Graphics/Background/Tombstone/tombstone.png')


        # Player
        self.player_stand = pygame.image.load('Graphics/Entities/Player/Player_stand/Player_stand.png').convert_alpha()
        self.player_walk_1 = pygame.image.load('Graphics/Entities/Player/Player_walk/Player1.png').convert_alpha()
        self.player_walk_2 = pygame.image.load('Graphics/Entities/Player/Player_walk/Player2.png').convert_alpha()
        self.player_jump = pygame.image.load('Graphics/Entities/Player/Player_jump/Player_jump.png').convert_alpha()

        # Obstacle
        self.ghost_1 = pygame.image.load('Graphics/Entities/Ghost/Ghost1.png').convert_alpha()
        self.ghost_2 = pygame.image.load('Graphics/Entities/Ghost/Ghost2.png').convert_alpha()
        self.ghost_3 = pygame.image.load('Graphics/Entities/Ghost/Ghost3.png').convert_alpha()
        self.ghost_4 = pygame.image.load('Graphics/Entities/Ghost/Ghost4.png').convert_alpha()

        self.witch_1 = pygame.image.load('Graphics/Entities/Witch/Witch1.png').convert_alpha()
        self.witch_2 = pygame.image.load('Graphics/Entities/Witch/Witch2.png').convert_alpha()
        self.witch_3 = pygame.image.load('Graphics/Entities/Witch/Witch3.png').convert_alpha()
        self.witch_4 = pygame.image.load('Graphics/Entities/Witch/Witch4.png').convert_alpha()


    def load_image(self, path: str) -> list[pygame.Surface]:
        image_list = []
        pictures = list(walk(path))[0][2]
        for pic in pictures:
            image = pygame.image.load(f"{path}/{pic}").convert_alpha()
            image_list.append(image)
        return image_list
