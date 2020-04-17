import pygame
import sys

pygame.init()

window = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Banana')
screen = pygame.Surface((1000, 700))
pygame.mixer.music.load('music/videoplayback.mp3')
pygame.mixer.music.play(-1)

f = pygame.font.Font(None, 50)
f2 = pygame.font.Font(None, 90)
text = f2.render('Music', 1, (0, 0, 0))

class Settings:
    def __init__(self, pun):
        self.punkts = pun

    def render(self, surface, font, num_punkt):
        for r in self.punkts:
            if num_punkt == r[5]:
                surface.blit(font.render(r[2], 1, r[4]), (r[0], r[1] - 30))
            else:
                surface.blit(font.render(r[2], 1, r[3]), (r[0], r[1] - 30))

    def settings(self):
        done2 = True
        pygame.font.init()
        punkt = 0
        while done2:
            screen.fill((225, 225, 0))
            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if i[0] < mp[0] < i[0] + 155 and i[1] < mp[1] < i[1] + 70:
                    punkt = i[5]
            self.render(screen, f, punkt)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    sys.exit()
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_LEFT:
                        if punkt > 0:
                            punkt -= 1
                    if e.key == pygame.K_RIGHT:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                    if e.key == pygame.K_SPACE:
                        if punkt == 0:
                            done2 = False
                        elif punkt == 1:
                            pygame.mixer.music.unpause()
                        elif punkt == 2:
                            pygame.mixer.music.pause()
                    if e.key == pygame.K_ESCAPE:
                        done2 = False
                if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                    if punkt == 0:
                        done2 = False
                    elif punkt == 1:
                        pygame.mixer.music.unpause()
                    elif punkt == 2:
                        pygame.mixer.music.pause()

            screen.blit(text, (250, 190))
            window.blit(screen, (0, 0))
            pygame.display.flip()
