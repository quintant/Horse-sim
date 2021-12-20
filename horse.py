from random import uniform, randint
import random
from pygame.draw import circle, polygon
from pygame.transform import scale, flip
from colors import *
import pygame
from text import myfont

SIXE = 90

class Horse:
    def __init__(self, ID, pos: list, surface, end) -> None:
        """X/Y pos"""
        self.ID = ID
        self.pos = pos
        self.init_speed = uniform(0.37, 0.45)
        self.stamina = randint(100, 300)
        self.sprint_multiplier = random.gauss(4, 0.3)
        self.threshold = 0.88
        self.threshold2 = 5
        self.surface = surface
        self.sprinting = False
        self.sp_cnt = 1
        self.stam_t_mod = uniform(0.8, 1.2)
        self.end = end
        self.finished = False
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))

        self.f_num = 0

        self.speed1 = scale(pygame.image.load("coomer.jpg"), (SIXE, SIXE))
        self.speed2 = scale(pygame.image.load("coomer2.gif"), (SIXE, SIXE))
        self.woman = scale(pygame.image.load('woman.jpg'), (SIXE*1.303030303030303,SIXE))
        # self.slow = scale(pygame.image.load("bonk.png"), (SIXE, SIXE))
        self.slow = scale(pygame.image.load("coomer2.gif"), (SIXE, SIXE))

        self.grunt_sound = pygame.mixer.Sound("grunt.mp3")
        self.kiss_sound = pygame.mixer.Sound("kiss.mp3")
        self.scream_sound = pygame.mixer.Sound("scream.mp3")
        self.moan_sound = pygame.mixer.Sound("moan.mp3")

    def step(self):
        self.f_num += 1
        if not self.finished:
            if self.sprinting:
                self.pos[0] += self.init_speed * self.sprint_multiplier #/ self.sp_cnt
                self.stamina -= 1*self.sprint_multiplier
            else:
                self.pos[0] += self.init_speed
                self.stamina += 1
                x = random.gauss(0, 1)
                if x > self.threshold and self.stamina > 600 * self.stam_t_mod:
                    self.sp_cnt += 1
                    self.sprinting = True
                    pygame.mixer.Sound.play(self.kiss_sound)
                    pygame.mixer.Sound.play(self.grunt_sound)
                    # pygame.mixer.Sound.play(self.moan_sound)
                if x > self.threshold2:
                    self.sp_cnt -= 1 if self.sp_cnt > 1 else 0
                    pygame.mixer.Sound.play(self.scream_sound)
            if self.stamina < 0:
                self.sprinting = False
        if self.pos[0] > self.end:
            self.finished = True

    def blit(self):
        if not self.finished:
            if self.sprinting:
                # circle(self.surface, yellow, self.pos, 20)
                if self.f_num % 20 == 0:
                    self.speed1 = flip(self.speed1, True, False)
                self.surface.blit(self.speed1, self.pos)
                self.surface.blit(self.woman, (self.pos[0]+SIXE, self.pos[1]))
                # if self.f_num % 2 == 0:
                #     self.surface.blit(self.speed1, self.pos)
                # else:
                #     self.surface.blit(self.speed2, self.pos)
            else:
                # circle(self.surface, self.color, self.pos, 20)
                self.surface.blit(self.slow, self.pos)
            
            self.surface.blit(myfont.render(self.ID, False, (0, 0, 0)), (self.pos[0]-SIXE/2, self.pos[1]))
