import pygame
import time
import random
 
pygame.init()
 
# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
 
# Set the width and height of the screen [width, height]
width = 500
height = 500
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snake Game")
 
# Initialize the snake and its starting position
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont(None, 30)
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False
    x1 = width / 2
    y1 = height / 2
    x1_change = 0
    y1_change = 0
    snake_List = []
    Length_of_snake = 1
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
    clock = pygame.time.Clock()
    # Game loop flag
    game_over = False

    while not game_over:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block_size
                    x1_change = 0

        # Check if the snake hits the boundaries
        if x1 >= window_width or x1 < 0 or y1 >= window_height or y1 < 0:
            game_over = True

        # Update the snake position
        x1 += x1_change
        y1 += y1_change

        # Draw the snake and the food
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [food_x, food_y, snake_block_size, snake_block_size])
        pygame.draw.rect(game_display, white, [x1, y1, snake_block_size, snake_block_size])
        pygame.display.update()

        # Check if the snake eats the food
        if x1 == food_x and y1 == food_y:
            print("Yummy!!")
            food_x = round(random.randrange(0, window_width - snake_block_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, window_height - snake_block_size) / 10.0) * 10.0

        # FPS
        clock = pygame.time.Clock()
        clock.tick(snake_speed)

    # Quit pygame
    pygame.quit()
    quit()

game_loop()
