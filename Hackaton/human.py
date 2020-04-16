import pygame
from random import randint


class Human():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('images/human.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.moving = True

    def update(self):
        if self.moving:
            self.rect.centerx += randint(-3, 3)
            self.rect.centery += randint(-3, 3)

    def blitme(self):
        self.screen.blit(self.image, self.rect)