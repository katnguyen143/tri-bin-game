# Kat Nguyen
# Period 3
# Final Project - Tri-bin Game

import pygame
from pygame.locals import *
import random
import time

# globals
screen_width = 1250
screen_height = 950
screen_color = (135, 206, 250)
score = 0

# item types
recycle_type = 1
compost_type = 2
trash_type = 3

# colors
black = (  0,   0,   0)
white = (255, 255, 255)
red   = (255,   0,   0)
yellow = (255, 236, 139)
brown = (139, 115, 85)
green = (61, 145, 64)
blue = (30, 144, 255)
lightgrey = (211, 211, 211)
grey = (48, 48, 48)

speed = 45

# classes
class TrashItem(pygame.sprite.Sprite):
    item_type = 0
    def __init__(self, item_type, image_name, scale):
        super(TrashItem, self).__init__()

        self.item_type = item_type
        pos = getRandomPosition()
        self.image = pygame.image.load(image_name).convert_alpha()
        width, height = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(width*scale), int(height*scale)) )
        self.rect = self.image.get_rect(center=pos)

    def hasCollided(self, sprite):
        return pygame.sprite.collide_rect(self, sprite)

class Bin(pygame.sprite.Sprite):
    bin_type = 0
    def __init__(self, bin_type, pos, size, color):
        super(Bin, self).__init__()

        self.bin_type = bin_type
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(topleft=pos)

    def hasCollided(self, sprite):
        return pygame.sprite.collide_rect(self, sprite)

    def draw(self):
        screen.blit( self.surf, self.rect )

# functions

def getRandomPosition():
    margin = 100
    x = random.randint( margin, screen_width-margin )
    y = random.randint( margin, 300 )
    return (x,y)

def drawLabel(screen, text, x, y, color1, color2, size = 50):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = str(text)
    text = font.render(text, True, color1, color2)
    screen.blit(text, (x,y))

def updateScore( item, bin ):
    global score
    item_type = selected.item_type
    bin_type = bin.bin_type

    if item_type == bin_type:
    	score += 1
    print( "item_type =", item_type, "bin_type =", bin_type, "score =", score, "items=", len(items))

# main

# init 

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Tri-Bin Game")

# trash bins

recycle_bin = Bin( recycle_type, (100,550), (250,900), blue )
compost_bin = Bin( compost_type, (500,550), (250,900), green )
trash_bin = Bin( trash_type, (900,550), (250,900), grey )

recycle_outline = pygame.rect.Rect(93, 543, 263, 900)
compost_outline = pygame.rect.Rect(493, 543, 263, 900)
trash_outline = pygame.rect.Rect(893, 543, 263, 900)

score_outline = pygame.rect.Rect(20, 20, 260, 90)
score_box = pygame.rect.Rect(25, 25, 250, 80)

bins = [ recycle_bin, compost_bin, trash_bin ]

# objects

cardboard = TrashItem( recycle_type, 'cardboard.png', 0.5 )
apple = TrashItem( compost_type, 'apple.png', 0.18 )
styrofoam = TrashItem( trash_type, 'styrofoam.png', 0.12 )
blackplastic = TrashItem( trash_type, 'blackplastic.png', 0.5 )
soda = TrashItem( recycle_type, 'soda.png', 0.03 )
paper_ball = TrashItem( recycle_type, 'paper_ball.png', 0.2 )
pen = TrashItem( trash_type, 'pen.png', 0.4 )
pizza_box = TrashItem( compost_type, 'pizza_box.png', 0.17 )
solo_cup = TrashItem( recycle_type, 'solo_cup.png', 0.2 )
starbucks = TrashItem( recycle_type, 'starbucks.png', 0.1 )
straw = TrashItem( trash_type, 'straw.png', 0.06 )
tinfoil = TrashItem( recycle_type, 'tinfoil.png', 0.12 )
twine = TrashItem( compost_type, 'twine.png', 0.25 )
post_it = TrashItem( recycle_type, 'post_it.png', 0.3 )
brokenglass = TrashItem( trash_type, 'brokenglass.png', 0.3 )
teabag = TrashItem( compost_type, 'teabag.png', 0.4 )
ziplock = TrashItem( trash_type, 'ziplock.png', 0.12 )
cupcake_liner = TrashItem( compost_type, 'cupcake_liner.png', 0.1 )

items = [ cardboard, apple, styrofoam, blackplastic, soda, paper_ball, pen, pizza_box, solo_cup, starbucks, straw, tinfoil, twine, post_it, brokenglass, teabag, ziplock, cupcake_liner ]

# mainloop

clock = pygame.time.Clock()

selected = None
running = True
item_length = len(items)
timer_value = 10
prev_sec = 0
initial_time = time.time()

# main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # KEYDOWN event
        if event.type == KEYDOWN:
            # esc key
            if event.key == K_ESCAPE:
                running = False
        # QUIT event
        elif event.type == QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:            
                for item in items:
                    if item.rect.collidepoint(event.pos):
                        selected = item
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            selected = None
        elif event.type == pygame.MOUSEMOTION:
            if selected:
                selected.rect.center = event.pos
                for bin in bins:
                    if selected.hasCollided( bin ):
                        updateScore( selected, bin )
                        items.remove(selected)
                        selected = None
                        break

    # draws
    screen.fill(screen_color)

    # draw the trash items to the screen
    for item in items:
        screen.blit( item.image, item.rect )

    # bins
    pygame.draw.rect(screen, lightgrey, recycle_outline)
    recycle_bin.draw()
    drawLabel(screen, "Recycle", 160, 650, white, blue)

    pygame.draw.rect(screen, lightgrey, compost_outline)
    compost_bin.draw()
    drawLabel(screen, "Compost", 555, 650, white, green)

    pygame.draw.rect(screen, lightgrey, trash_outline)
    trash_bin.draw()
    drawLabel(screen, "Trash", 980, 650, white, grey)

    # score
    pygame.draw.rect(screen, white, score_outline)
    pygame.draw.rect(screen, yellow, score_box)
    drawLabel(screen, "Score: " + str(score) + "/" + str(item_length), 50, 63, white, yellow )

    #time
    if len(items) > 0:
        sec = int( time.time() - initial_time + .5)
        if prev_sec != sec:
            print( sec )
            prev_sec = sec

    drawLabel(screen, "Time: " + str(sec), 50, 33, white, yellow)

    # update the display
    pygame.display.flip()

    # constant game speed
    clock.tick(speed)


# end

pygame.quit()
