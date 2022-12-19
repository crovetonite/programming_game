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


#time and score
start_ticks = pygame.time.get_ticks()
score = 0
check = False
timing = 10
#game cycle
while True:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
