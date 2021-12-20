from random import sample
import pygame
from colors import *
from pygame.locals import *
from constants import coomer_list

from horse import Horse


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = None
        self.width, self.height = None, None
        self.font = None
        self.num_horses = None
        self.clock = pygame.time.Clock()
        self.horses = []
        self.div = 100
        self.playing = False
        # self.bg = pygame.image.load("bg.jpg")

    def on_init(self):
        pygame.init()
        # self._display_surf = pygame.display.set_mode(self.size)
        self._display_surf = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.size = self.width, self.height = pygame.display.get_surface().get_size()
        self._running = True
        pygame.display.set_caption("Horse Betting Sim")
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.get_num_horses()
        self.init_horses()
    
    def init_horses(self):
        profile = sample(coomer_list, k=self.num_horses)
        self.horses = [Horse(str(i), [60, 100 + self.div*i], self._display_surf, self.width, profile[i]) for i in range(self.num_horses)]
        self.playing = False

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                self.playing ^= True
            elif event.key == pygame.K_r:
                self.init_horses()
            elif event.key == pygame.K_i:
                self.get_num_horses()
                self.init_horses()
            elif event.key == pygame.K_ESCAPE:
                self._running = False

    def on_loop(self):
        if self.playing:
            for horse in self.horses:
                horse.step()

    def on_render(self):
        self._display_surf.fill(black)
        # self._display_surf.blit(self.bg, (0,0))
        for horse in self.horses:
            horse.blit()
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        while self._running:
            self.clock.tick(60)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

    def get_num_horses(self):
        def disp(n):
            self._display_surf.fill(black)
            text = self.font.render("How many horses?", True, green, blue)
            textRect = text.get_rect()
            textRect.center = (self.width // 2, self.height // 2)
            self._display_surf.blit(text, textRect)
            # Num horses
            text = self.font.render(n, True, green, blue)
            textRect = text.get_rect()
            textRect.center = (self.width // 2, self.height // 2 + 32 + 2)
            self._display_surf.blit(text, textRect)
            pygame.display.update()

        num = ""
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if num.isdigit() and (0 < int(num) < 9):
                            done = True
                            self.num_horses = int(num)
                        else:
                            num = ""
                    elif event.key == pygame.K_BACKSPACE:
                        num = num[:-1]
                    else:
                        num += event.unicode
            disp(num)
        