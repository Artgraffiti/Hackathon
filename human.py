import pygame
from random import randint


class Human:
    def __init__(self, settings, screen):
        self.screen = screen
        self.image = pygame.image.load('images/human.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.settings = settings

        self.rect.centerx = randint(self.settings.frame_left_border, self.settings.frame_right_border)
        self.rect.centery = randint(self.settings.frame_top_border, self.settings.frame_bottom_border)
        self.settings = settings
        self.center_x = float(self.rect.centerx)
        self.center_y = float(self.rect.centery)
        self.moving = True
        self.is_ill = False

    def update(self):

        if self.is_ill:
            x = self.rect.centerx
            y = self.rect.centery
            self.image = pygame.image.load('images/ill_human.png')
            self.rect = self.image.get_rect()
            self.rect.centerx = x
            self.rect.centery = y
            self.center_x = float(self.rect.centerx)
            self.center_y = float(self.rect.centery)

        if self.moving:
            if self.settings.frame_top_border < self.center_y < self.settings.frame_bottom_border:
                self.center_y += randint(-self.settings.human_speed, self.settings.human_speed) / 10
            else:
                if self.center_y <= self.settings.frame_top_border:
                    self.center_y += randint(10, self.settings.human_speed) / 10
                if self.center_y >= self.settings.frame_bottom_border:
                    self.center_y -= randint(10, self.settings.human_speed) / 10

            if self.settings.frame_right_border > self.center_x > self.settings.frame_left_border:
                self.center_x += randint(-self.settings.human_speed, self.settings.human_speed) / 10
            else:
                if self.center_x >= self.settings.frame_right_border:
                    self.center_x -= randint(10, self.settings.human_speed) / 10
                if self.center_x <= self.settings.frame_left_border:
                    self.center_x += randint(10, self.settings.human_speed) / 10

        self.rect.centerx = self.center_x
        self.rect.centery = self.center_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
