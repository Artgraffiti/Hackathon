import sys
import pygame

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, human):
    human.update()
    screen.fill(settings.bg_color)
    human.blitme()
    pygame.display.flip()
