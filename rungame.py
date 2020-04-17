import pygame
import sys
from settings import Settings
from human import Human
import game_function as gf

window = pygame.display.set_mode((1000, 500))
pygame.display.set_caption('Banana')
screen = pygame.Surface((1000, 500))
info_string = pygame.Surface((1000, 500))

class Menu:
    def __init__(self, punkts=[126, 140, u'Punkt', (50, 0, 50), (100, 0, 50), 0]):
        self.punkts = punkts

    def render(self, surface, font, num_punkt):
        for r in self.punkts:
            if num_punkt == r[5]:
                surface.blit(font.render(r[2], 1, r[4]), (r[0], r[1] -30))
            else:
                surface.blit(font.render(r[2], 1, r[3]), (r[0], r[1] -30))

    def menu(self):
        done = True
        pygame.font.init()
        font_menu = pygame.font.Font(None, 100)
        punkt = 0
        while done:
            info_string.fill((230, 230, 230))
            screen.fill((230, 230, 230))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 50:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        sys.exit()
                    if e.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                    if e.key == pygame.K_SPACE:
                        if punkt == 0:
                            done = False
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()
            window.blit(info_string, (0, 0))
            window.blit(screen, (0, 30))
            pygame.display.flip()

punkts = [(400, 100, u'Start', (0, 0, 0), (120, 10, 10), 0), (400, 300, u'Quit', (0, 0, 0), (120, 10, 10), 1)]

game = Menu(punkts)
game.menu()

def run_game():
    fps = 60
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(settings.screen_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Банан")
    bg_color = (230, 230, 230)
    human = Human(settings, screen)
    while True:
        gf.check_event()
        clock.tick(fps)
        gf.update_screen(settings, screen, human)
        
run_game()
