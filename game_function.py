import sys
import pygame
from random import randint


def check_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def nearby(human, ill_human):

    """Проверяет рядом ли human и ill_human"""
    if ill_human.rect.left <= human.rect.right and \
       ill_human.rect.right >= human.rect.left and \
       ill_human.rect.bottom >= human.rect.top and \
       ill_human.rect.top <= human.rect.bottom:
        return True
    

def medical_exam(humans, ill_humans):

    """Проверяет заболевших в списке humans"""
    for human in humans:
        for ill_human in ill_humans:
            if nearby(human, ill_human):
                if randint(1, 101) < human.settings.infection_chance:
                    human.is_ill = True


def update_screen(settings, screen, humans, ill_humans):
    
    for human in humans:
        human.update()
    for ill_human in ill_humans:
        ill_human.update()

    medical_exam(humans, ill_humans)
    
    screen.fill(settings.bg_color)
    for human in humans:
        human.blitme()
    for ill_human in ill_humans:
        ill_human.blitme()
    pygame.display.flip()
