import pygame
from sys import exit
from image_manager import ImageManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Halloween Jumper')
        self.screen = pygame.display.set_mode((1200, 540))
        self.img_manager = ImageManager()
        pygame.display.set_icon(self.img_manager.icon)
        self.bg_offsets = [0]*9
        print(self.bg_offsets)
        self.img_manager.background_images = self.img_manager.load_image("Graphics/Background/layers")

        self.clock = pygame.time.Clock()
        self.start_game()

    def check_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    def start_game(self):
        while True:
            self.check_game_events()
            self.parallax_draw(self.img_manager.background_images)
            pygame.display.update()
            self.clock.tick(60)

    def parallax_draw(self, image_list: list[pygame.Surface]) -> None:

        background_width = self.img_manager.background_images[0].get_width()

        for index, i in enumerate(image_list):
            self.bg_offsets[index] += index*index / 20
            if self.bg_offsets[index] > background_width:
                self.bg_offsets[index] -= background_width

            for x in range(3):
                self.screen.blit(i, (x * background_width - self.bg_offsets[index], 0))

game = Game()
