import pygame
import sys
from Window import Window
from human import Human
import game_function as gf
from Settings import Settings

pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Banana')
screen = pygame.Surface((1000, 1000))

#Window

banana_surf = pygame.image.load('images/banana2.jpg')
banana_rect = banana_surf.get_rect(bottomright=(1000, 1000))

#Banana

punk2 = [(500, 240, u'On', (0, 0, 0), (120, 10, 120), 1), (600, 240, u'Off', (0, 0, 0), (120, 10, 120), 2), (50, 60, u'Back', (0, 0, 0), (120, 0, 10), 0)]
settings = Settings(punk2)


class Menu:
    def __init__(self, pun):
        self.punkts = pun

    def render(self, surface, font, num_punkt):
        for r in self.punkts:
            if num_punkt == r[5]:
                surface.blit(font.render(r[2], 1, r[4]), (r[0], r[1]))
            else:
                surface.blit(font.render(r[2], 1, r[3]), (r[0], r[1]))

    def menu(self):
        done = True
        pygame.font.init()
        font_menu = pygame.font.Font(None, 120)
        punkt = 0
        while done:
            screen.blit(banana_surf, banana_rect)
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 70:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_UP:
                        if punkt >= 0:
                            punkt -= 1
                    if e.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                    if e.key == pygame.K_SPACE:
                        if punkt == 0:
                            done = False
                        elif punkt == 1:
                            settings.settings()
                        elif punkt == 2:
                            sys.exit()
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        settings.settings()
                    elif punkt == 2:
                        sys.exit()

            window.blit(screen, (0, 0))
            pygame.display.flip()

punkts = [(400, 100, u'Start', (0, 0, 0), (120, 10, 120), 0), (400, 500, u'Quit', (0, 0, 0), (120, 10, 10), 2), (330, 300, u'Settings', (0, 0, 0), (120, 10, 10), 1)]

game = Menu(punkts)
game.menu()

def run_game():
    fps = 60
    pygame.init()
    win = Window()
    scr = pygame.display.set_mode(win.screen_size)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Банан")
    s = Settings(pun=None)
    humans = []
    for i in range(s.human_number-1):
        humans.append(Human(win, scr))
    ill_human = Human(win, scr)
    ill_human.is_ill = True
    ill_humans = [ill_human]
        
    while True:
        gf.check_event()
        clock.tick(fps)
        gf.update_screen(win, scr, humans, ill_humans)
        for human in humans:
            if human.is_ill:
                humans.pop(humans.index(human))
                ill_humans.append(human)
        

run_game()
