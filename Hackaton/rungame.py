import pygame, sys
from settings import Settings
from human import Human
import game_function as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(ai_settings.screen_size)
    pygame.display.set_caption("Банан")
    bg_color = (230, 230, 230)
    human = Human(screen)
    while True:
        gf.check_event()
        human.update()
        screen.fill(ai_settings.bg_color)
        human.blitme()
        pygame.display.flip()

run_game()