import pygame
from colors import *
from pygame.locals import *

from horse import Horse


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 1200, 900
        self.font = None
        self.num_horses = None
        self.clock = pygame.time.Clock()
        self.horses = []
        self.div = 100

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size)
        self._running = True
        pygame.display.set_caption("Horse Betting Sim")
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.get_num_horses()
        self.horses = [Horse([0, 100 + self.div*i], self._display_surf, self.width) for i in range(self.num_horses)]

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        for horse in self.horses:
            horse.step()

    def on_render(self):
        self._display_surf.fill(black)
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
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if num.isdigit():
                            done = True
                            self.num_horses = int(num)
                        else:
                            num = ""
                    elif event.key == pygame.K_BACKSPACE:
                        num = num[:-1]
                    else:
                        num += event.unicode
            disp(num)
