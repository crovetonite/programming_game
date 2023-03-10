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

class Game_Button():
    def __init__(self, x, y, width, height, image, onclickFunction=None, onePress=False):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.onclickFunction = onclickFunction
        self.onePress = onePress
        self.img = pygame.image.load(image)
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.buttonSurface = self.img
        self.buttonRect = self.img.get_rect(topleft=(self.x, self.y))

        self.alreadyPressed = False

        objects.append(self)

    def process(self):

        mousePos = pygame.mouse.get_pos()

        if self.buttonRect.collidepoint(mousePos):
            if pygame.mouse.get_pressed(num_buttons=3)[0]:

                if self.onePress:
                    self.onclickFunction()

                elif not self.alreadyPressed:
                    self.onclickFunction()
                    self.alreadyPressed = True

            else:
                self.alreadyPressed = False
        screen.blit(self.buttonSurface, (self.x, self.y))

# button function
def myFunction():
    global score
    score += 1
    objects.pop()
    customButton = Game_Button(random.choice(x_spawn), random.choice(y_spawn), 50, 70, 'he.png', myFunction)
    global start_ticks
    start_ticks = pygame.time.get_ticks()
    global timing
    timing *= 0.98


# time and score
score = 0
check = False
timing = 10
x_spawn = [100, 300, 500]
y_spawn = [70, 280]
bg = pygame.image.load('grass.jpg')
bg = pygame.transform.scale(bg, (640, 480))
# button itself
def game():
    customButton = Game_Button(random.choice(x_spawn), random.choice(y_spawn), 50, 70, 'he.png', myFunction)
    global start_ticks
    start_ticks = pygame.time.get_ticks()
    global check
    while True:
        screen.fill((30, 30, 30))
        screen.blit(bg, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        for object in objects:
            object.process()
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if check == False:
            time_surf = txt_font.render_to(screen, (50, 400), '???????????????? ' + str(timing - seconds)[:3] + ' ????????????',
                                           (250, 250, 250))
        if seconds > timing:
            check = True
        if check:
            objects.clear()
            end_surface = txt_font.render_to(screen, (50, 350), '?????????? ??????????, ???? ?????????????? ' + str(score),
                                             (220, 125, 220))
        pygame.display.flip()
        fpsClock.tick(fps)
def start():
    objects.clear()
    game()
begin = Button(220, 190, 200, 100, 'START', start)
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
