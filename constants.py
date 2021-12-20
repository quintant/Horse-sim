from pygame.transform import scale, flip
import pygame

pygame.mixer.init()

SIXE = 90
speed1 = scale(pygame.image.load("coomer.jpg"), (SIXE, SIXE))
speed2 = flip(speed1, True, False)
woman = scale(pygame.image.load("woman.jpg"), (SIXE * 1.303030303030303, SIXE))

slow0 = scale(pygame.image.load("coomer2.gif"), (SIXE, SIXE))
slow1 = scale(pygame.image.load("coomer-army.jpg"), (SIXE, SIXE))
slow2 = scale(pygame.image.load("coomer-army2.jpg"), (SIXE, SIXE))
slow3 = scale(pygame.image.load("coomer-aus.jpg"), (SIXE, SIXE))
slow4 = scale(pygame.image.load("coomer-clown.jpg"), (SIXE, SIXE))
slow5 = scale(pygame.image.load("coomer-lizzard.png"), (SIXE, SIXE))
slow6 = scale(pygame.image.load("doomer-girl.jpg"), (SIXE, SIXE))
slow7 = scale(pygame.image.load("doomer.jpg"), (SIXE, SIXE))
slow8 = scale(pygame.image.load("coomeryoda.png"), (SIXE, SIXE))

coomer_list = [slow0, slow1,slow2,slow3,slow4,slow5,slow6,slow7,slow8]

grunt_sound = pygame.mixer.Sound("grunt.mp3")
kiss_sound = pygame.mixer.Sound("kiss.mp3")
scream_sound = pygame.mixer.Sound("scream.mp3")
