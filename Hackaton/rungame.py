import pygame, sys
from settings import Settings
from human import Human
import game_function as gf


def run_game():
    FPS = 60
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Банан")
    bg_color = (230, 230, 230)
    human = Human(settings, screen)
    while True:
        gf.check_event()
        clock.tick(FPS)
        gf.update_screen(settings, screen, human)

run_game()