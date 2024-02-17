# Limited Space Game

import pygame # Imports pygame module
import time # Imports time module

pygame.init() # Initializes pygame

SCREEN_WIDTH = 800 # Sets screen width variable to 800 pixels
SCREEN_HEIGHT = 600 # Sets screen height variable to 600 pixels

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Passes the display settings to pygame

square_player = pygame.Rect((300, 250, 15, 15)) # Creates a pygame rectange (x_location, y_location, width, height)

run = True # Sets running variable to True

def bounding_box(x, y, width, height):
    pass

def collision():
    pass

while run: # Initializes game 
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), square_player) # draws the red square on the screen params (surface, colour, rectangle) 


    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        square_player.move_ip(-1,0)
        time.sleep(0.01)
    elif key[pygame.K_d] == True:
        square_player.move_ip(1,0)
        time.sleep(0.01)
    elif key[pygame.K_s] == True:
        square_player.move_ip(0,1)
        time.sleep(0.01)
    elif key[pygame.K_w] == True:
        square_player.move_ip(0,-1)
        time.sleep(0.01)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    pygame.display.update()
pygame.quit()