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

