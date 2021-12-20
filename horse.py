from random import uniform, randint
import random
from pygame.draw import circle
from colors import *

class Horse:
    def __init__(self, pos:list, surface, end) -> None:
        """X/Y pos"""
        self.pos = pos
        self.init_speed = uniform(.35, .45)
        self.stamina = randint(100, 300)
        self.sprint_multiplier = uniform(3, 4)
        self.threshold = 0.8
        self.surface = surface
        self.sprinting = False
        self.sp_cnt = 1
        self.stam_t_mod = uniform(0.8, 1.2)
        self.end = end
        self.finished = False

    def step(self):
        if not self.finished:
            if self.sprinting:
                self.pos[0] += self.init_speed * self.sprint_multiplier
                self.stamina -= 10
            else:
                self.pos[0] += self.init_speed
                self.stamina += 1
                x = random.normalvariate(0, 1)
                if x > self.threshold and self.stamina > 500*self.stam_t_mod:
                    self.sp_cnt+=1
                    self.sprinting = True
            if self.stamina < 0:
                self.sprinting = False
        if self.pos[0] > self.end:
            self.finished = True
        
    def blit(self):
        if not self.finished:
            circle(self.surface, blue, self.pos, 20)
    