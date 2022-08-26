import pygame
from sys import exit
from random import randint
from player import Player
from obstacle import Obstacle
from image_manager import ImageManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Halloween Jumper')
        self.screen = pygame.display.set_mode((960, 540))
        self.img_manager = ImageManager()
        pygame.display.set_icon(self.img_manager.game_icon)

        self.test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

        self.score_message, self.press_space, self.game_caption = None, None, None
        self.score_message_rectangle = None
        self.press_space_rectangle = None
        self.game_caption_rectangle = None


        self.witch_animation_timer = None
        self.ghost_animation_timer = None
        self.obstacle_timer = None

        self.score = 0
        self.game_active = False
        self.start_time = 0
        self.clock = pygame.time.Clock()

        self.bg_Music = pygame.mixer.Sound('Audio/Game_music.mp3')
        self.bg_Music.set_volume(0.3)
        self.bg_offsets = [0]*9

        self.player = pygame.sprite.GroupSingle()
        self.obstacle_group = pygame.sprite.Group()

        self.player_stand = self.img_manager.player_stand
        self.player_stand_rectangle = None

        self.bg_Music.play()

        # Groups
        self.player.add(Player(self.img_manager))
        self.show_intro_screen()
        self.create_timers()
        self.start_game()

    def start_game(self):
        while True:
            self.check_game_events()
            if self.game_active:
                self.parallax_draw(self.img_manager.background_images)
                self.draw_entities()
                self.game_active = self.collision_sprite()
                self.display_score()
            else:
                self.draw_outro_screen()
            pygame.display.update()
            self.clock.tick(60)

    def show_intro_screen(self):
        # Intro screen
        self.player_stand = pygame.transform.rotozoom(self.img_manager.player_stand, 0, 2.5)
        self.player_stand_rectangle = self.player_stand.get_rect(center=(480, 270))

        # Intro text
        self.game_caption = self.test_font.render('Halloween Runner', False, '#31F5EC')
        self.game_caption_rectangle = self.game_caption.get_rect(center=(480, 70))

        self.press_space = self.test_font.render('Press [ SPACE ] to play', False, '#31F5EC')
        self.press_space_rectangle = self.press_space.get_rect(center=(480, 450))

        self.score_message = self.test_font.render(f'Your score: {self.score}', False, '#31F5EC')
        self.score_message_rectangle = self.score_message.get_rect(center=(400, 330))


    def parallax_draw(self, image_list: list[pygame.Surface]) -> None:

        background_width = self.img_manager.background_images[0].get_width()

        for index, i in enumerate(image_list):
            self.bg_offsets[index] += index*index / 20
            if self.bg_offsets[index] > background_width:
                self.bg_offsets[index] -= background_width

            for x in range(3):
                self.screen.blit(i, (x * background_width - self.bg_offsets[index], 0))

    def draw_entities(self):
        # Player
        self.player.draw(self.screen)
        self.player.update()

        # Obstacle
        self.obstacle_group.draw(self.screen)
        self.obstacle_group.update()

    def spawn_enemy(self):
        if randint(0, 2):
            self.obstacle_group.add(Obstacle('ghost', self.img_manager))
        else:
            self.obstacle_group.add(Obstacle('witch', self.img_manager))

    def check_game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.game_active:
                if event.type == self.obstacle_timer:
                    self.spawn_enemy()

            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.start_time = pygame.time.get_ticks()
                    self.game_active = True

    def create_timers(self):
        self.obstacle_timer = pygame.USEREVENT + 1  # custom user event
        pygame.time.set_timer(self.obstacle_timer, 1500)

        self.ghost_animation_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ghost_animation_timer, 500)

        self.witch_animation_timer = pygame.USEREVENT + 2
        pygame.time.set_timer(self.witch_animation_timer, 200)

    def collision_sprite(self):
        if pygame.sprite.spritecollide(self.player.sprite, self.obstacle_group, False):
            self.obstacle_group.empty()
            return False
        else:
            return True

    def display_score(self):
        self.score = round((pygame.time.get_ticks() - self.start_time) / 1000)
        active_score_surface = self.test_font.render(f'Score: {self.score}', False, '#31F5EC')
        active_score_rectangle = active_score_surface.get_rect(center=(480, 100))
        self.screen.blit(active_score_surface, active_score_rectangle)


    def draw_outro_screen(self):
        self.screen.fill('#000000')

        if self.score == 0:
            self.screen.blit(self.press_space, self.press_space_rectangle)
            self.screen.blit(self.player_stand, self.player_stand_rectangle)
            self.screen.blit(self.game_caption, self.game_caption_rectangle)
        else:
            self.screen.blit(self.game_caption, self.game_caption_rectangle)
            self.img_manager.tombstone_rectangle = self.img_manager.tombstone.get_rect(center=(480, 270))
            self.screen.blit(self.img_manager.tombstone, self.img_manager.tombstone_rectangle)
            score_surface = self.test_font.render(f'Score: {self.score}', False, '#31F5EC')
            score_rectangle = score_surface.get_rect(center=(480, 450 ))
            self.screen.blit(score_surface, score_rectangle)


game = Game()
