import pygame
import random
import sys
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
#buttons!
class Button():
    def __init__(self, x, y, width, height, buttonText='Button', onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.fillColors = {
            'normal': '#ffffff',
            'hover': '#666666',
            'pressed': '#333333',
        }

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        self.buttonSurf = font.render(buttonText, True, (20, 20, 20))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        self.buttonSurface.fill(self.fillColors['normal'])
        if self.buttonRect.collidepoint(mousePos):
            self.buttonSurface.fill(self.fillColors['hover'])
            if pygame.mouse.get_pressed(num_buttons=3)[0]:
                self.buttonSurface.fill(self.fillColors['pressed'])

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False

        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width / 2 - self.buttonSurf.get_rect().width / 2,
            self.buttonRect.height / 2 - self.buttonSurf.get_rect().height / 2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)


# game cycle
def game():
    # time and score
    start_ticks = pygame.time.get_ticks()
    global score, check, timing
    score = 0
    check = False
    timing = 10
    #button function
    def myFunction():
        global score
        score +=1
        objects.pop()
        customButton = Button(random.randint(40, 600), random.randint(40, 440), 100, 50, 'BONK', myFunction)
        global start_ticks
        start_ticks = pygame.time.get_ticks()
        global timing
        timing *= 0.98
    # button itself
    customButton = Button(random.randint(40, 600), random.randint(40, 440), 100, 50, 'BONK', myFunction)
    while True:
        screen.fill((30, 30, 30))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for object in objects:
            object.process()

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if check == False:
            time_surf = txt_font.render_to(screen, (50, 350), 'осталось ' + str(timing - seconds)[:3] + ' секунд',
                                           (250, 250, 250))
        if seconds > timing:
            check = True
        if check:
            objects.clear()
            end_surface = txt_font.render_to(screen, (50, 350), 'Время вышло, Вы набрали ' + str(score),
                                             (220, 255, 125))
        pygame.display.flip()
        fpsClock.tick(fps)
def starting():
    objects.clear()
    game()


start = Button(320,240,200,100,'START GAME', starting)
while True:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    for object in objects:
        object.process()
    pygame.display.flip()
    fpsClock.tick(fps)
