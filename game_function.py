import sys
import pygame

def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(settings, screen, humans):
    for human in humans:
        human.update()
    screen.fill(settings.bg_color)
    for human in humans:
        human.blitme()
    pygame.display.flip()
