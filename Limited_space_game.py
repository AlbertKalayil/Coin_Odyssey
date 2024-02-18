import pygame # Imports pygame module
import time # Imports time module
import random

pygame.init() # Initializes pygame
clock = pygame.time.Clock()

SCREEN_WIDTH = 800 # Sets screen width variable to 800 pixels
SCREEN_HEIGHT = 600 # Sets screen height variable to 600 pixels


coin_height = 10
coin_width = 10

box_height = 30
box_width = 30

score = 0
timer = 121

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Passes the display settings to pygame
screen_rect = screen.get_rect()

square_player = pygame.Rect((300, 250, 15, 15)) # Creates a pygame rectange (x_location, y_location, width, height

run = True # Sets running variable to True

def show_score_time(display_score):
    score_obj = pygame.font.SysFont('comicsans', 15, True)
    score_txt = score_obj.render(('Score:' + str(display_score)), 1 , (255,255,255))
    screen.blit(score_txt, (0, 0 ))


def show_time(display_time):
    time_obj = pygame.font.SysFont('comicsans', 15, True)
    time_txt = time_obj.render(('Time Left:' + str(display_time)), 1 , (255,255,255))
    screen.blit(time_txt, (0,15))

def game_over_screen(display_score):
    game_over_obj = pygame.font.SysFont('comicsans', 38, True)
    game_over_txt = game_over_obj.render('Time\'s up, you reached a score of: ' + str(display_score), 1, (0, 0, 255))
    screen.blit(game_over_txt, (50, 275))

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
    pygame.display.set_caption(f"Space limited game")

    pygame.draw.rect(screen, (255, 0, 0), square_player) # draws the red square on the screen params (surface, colour, rectangle) 
    
    show_score_time(score)
    show_time(round(timer))

    while len(coins) < 5:
        coins.append(Coin(random.randint(20, SCREEN_WIDTH-20), random.randint(20, SCREEN_HEIGHT-20), coin_height, coin_width, (252,240,3)))
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
    
    if timer >= 0:
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
        
        timer -= 0.016666667

    else:
        game_over_screen(score)

    
    square_player.clamp_ip(screen_rect)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    

    clock.tick(60)
    pygame.display.update()
pygame.quit()