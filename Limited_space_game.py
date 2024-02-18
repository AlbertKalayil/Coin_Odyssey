import pygame # Imports pygame module
import time # Imports time module
import random

pygame.init() # Initializes pygame

SCREEN_WIDTH = 800 # Sets screen width variable to 800 pixels
SCREEN_HEIGHT = 600 # Sets screen height variable to 600 pixels


coin_height = 10
coin_width = 10

box_height = 30
box_width = 30

score = 0

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Passes the display settings to pygame
screen_rect = screen.get_rect()

square_player = pygame.Rect((300, 250, 15, 15)) # Creates a pygame rectange (x_location, y_location, width, height)

run = True # Sets running variable to True

def bounding_box(x, y, width, height):
    pass

def collision():
    pass


class Coin():
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

        self.rect = pygame.Rect(self.x, self.y, coin_height, coin_width)
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

class Box():
    def __init__(self, x, y, height, width, color):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.color = color

        self.rect = pygame.Rect(self.x, self.y, box_height, box_width)
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

coins = []
boxes = []

while run: # Initializes game 
    screen.fill((0,0,0))

    pygame.draw.rect(screen, (255, 0, 0), square_player) # draws the red square on the screen params (surface, colour, rectangle) 
    

    while len(coins) < 6:
        coins.append(Coin(random.randint(20, SCREEN_WIDTH-20), random.randint(20, SCREEN_HEIGHT-20), coin_height, coin_width, (0,255,0)))
        boxes.append(Box(random.randint(20, SCREEN_WIDTH-20), random.randint(20, SCREEN_HEIGHT-20), box_height, box_width, (255,255,255)))

    for coin in coins:
        coin.draw()
        if square_player.colliderect(coin):
            coins.remove(coin)
            score += 1
        if coin.rect.collidelistall(boxes):
            coins.remove(coin)

    for box in boxes:
        box.draw()
        new_boxes_list = boxes[:]
        new_boxes_list.remove(box)
        if box.rect.collidelistall(new_boxes_list):
            boxes.remove(box)
            boxes.append(Box(random.randint(20, SCREEN_WIDTH-20), random.randint(20, SCREEN_HEIGHT-20), box_height, box_width, (255,255,255)))



    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        square_player.move_ip(-1,0)
        for box in boxes:
            if square_player.colliderect(box):
                square_player.move_ip(1,0)
        time.sleep(0.01)
    elif key[pygame.K_d] == True:
        square_player.move_ip(1,0)
        for box in boxes:
            if square_player.colliderect(box):
                square_player.move_ip(-1,0)
        time.sleep(0.01)
    elif key[pygame.K_s] == True:
        square_player.move_ip(0,1)
        for box in boxes:
            if square_player.colliderect(box):
                square_player.move_ip(0,-1)
        time.sleep(0.01)
    elif key[pygame.K_w] == True:
        square_player.move_ip(0,-1)
        for box in boxes:
            if square_player.colliderect(box):
                square_player.move_ip(0,1)
        time.sleep(0.01)

    square_player.clamp_ip(screen_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    


    
    pygame.display.update()
pygame.quit()