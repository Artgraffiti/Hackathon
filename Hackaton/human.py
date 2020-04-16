import pygame
from random import randint


class Human():
    def __init__(self, settings, screen):
        self.screen = screen
        self.image = pygame.image.load('images/human.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.settings = settings
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.moving = True

    def update(self):
        if self.moving:
                self.center_x += randint(-(self.settings.human_speed), self.settings.human_speed) / 10
                self.center_y += randint(-(self.settings.human_speed), self.settings.human_speed) / 10

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y


    def blitme(self):
        self.screen.blit(self.image, self.rect)