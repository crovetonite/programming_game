import pygame
import random
pygame.init()

#settings
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
txt_font = pygame.freetype.SysFont('Comic Sans MS', 25)
font = pygame.font.SysFont('Arial', 20)
objects=[]
