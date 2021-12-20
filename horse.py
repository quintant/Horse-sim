from random import uniform, randint
import random
from pygame.draw import circle, polygon
from pygame.transform import scale, flip
from colors import *
import pygame
from text import myfont, myfontS

from constants import speed1, speed2, woman, grunt_sound, kiss_sound, SIXE

class Horse:
    def __init__(self, ID, pos: list, surface, end, profile) -> None:
        """X/Y pos"""
        self.profile = profile
        self.ID = ID
        self.pos = pos
        self._create_stats()
        
        self.threshold = 3.2
        self.threshold2 = 5
        self.surface = surface
        self.sprinting = False
        self.sp_cnt = 1
        
        self.end = end
        self.finished = False

        self.f_num = 0
        
        self.animation = False
        # self.speed1 = scale(pygame.image.load("coomer.jpg"), (SIXE, SIXE))
        # self.speed2 = scale(pygame.image.load("coomer2.gif"), (SIXE, SIXE))
        # self.woman = scale(pygame.image.load('woman.jpg'), (SIXE*1.303030303030303,SIXE))
        # self.slow = scale(pygame.image.load("coomer2.gif"), (SIXE, SIXE))

        # self.grunt_sound = pygame.mixer.Sound("grunt.mp3")
        # self.kiss_sound = pygame.mixer.Sound("kiss.mp3")
        # self.scream_sound = pygame.mixer.Sound("scream.mp3")


        self.stamina = randint(100, 300)
        self._renew_color()

    def _renew_color(self):
        self.color = (randint(0,255),randint(0,255),randint(0,255))

    def _create_stats(self):
        # self.init_speed = random.gauss(1, 0.3)
        self.init_speed = random.gauss(0.69, 0.3)
        self.sprint_multiplier = random.gauss(2, 0.3)

    def step(self):
        if not self.finished:
            self.f_num += 1
            if self.pos[0] > 1800:
                self.init_speed *= 0.9999
            if self.sprinting:
                self.pos[0] += self.init_speed * self.sprint_multiplier
                self.stamina -= 1*self.sprint_multiplier
            else:
                self.pos[0] += self.init_speed
                x = random.gauss(0, 1)
                if x > self.threshold:
                    self.stamina = randint(300, 500)
                    self.sprinting = True
                    pygame.mixer.Sound.play(kiss_sound)
                    pygame.mixer.Sound.play(grunt_sound)
                elif x <-2.3:
                    self._create_stats()

            if self.stamina < 0:
                self.sprinting = False
        if self.pos[0] > self.end:
            self.finished = True

    def blit(self):
        if not self.finished:
            if self.sprinting:
                if self.f_num % 20 == 0:
                    self.animation ^= True
                    self._renew_color()
                if self.animation:
                    show = speed1
                else:
                    show = speed2
                self.surface.blit(show, self.pos)
                self.surface.blit(woman, (self.pos[0]+SIXE, self.pos[1]))
                self.surface.blit(myfontS.render(f'COOMER', False, self.color), (self.pos[0]-SIXE/2-20, self.pos[1]+40))
                self.surface.blit(myfontS.render(f'POWER!!', False, self.color), (self.pos[0]-SIXE/2-20, self.pos[1]+60))
            else:
                self.surface.blit(self.profile, self.pos)
            
            self.surface.blit(myfont.render(self.ID, False, (255, 255, 255)), (self.pos[0]-SIXE/2, self.pos[1]))
            
