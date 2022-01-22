import sys
import pygame
import keyboard
from player import Player
from mouse import Mouse
from maze import Maze
from pygame.locals import *

pygame.init()

fps = 60
fpsClock = pygame.time.Clock()

width, height = 640, 640
screen = pygame.display.set_mode((width, height))
maze = Maze()

p1 = Player(0, (0, 0), maze, screen)
p2 = Player(1, (15, 0), maze, screen)
mouse = Mouse((15, 15), p1, p2, screen)

# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.
    if keyboard.is_pressed('w'):
        print('w')
        update_val = (0, 1)
    elif keyboard.is_pressed('a'):
        print('a')
        update_val = (-1, 0)
    elif keyboard.is_pressed('s'):
        print('s')
        update_val = (0, -1)
    elif keyboard.is_pressed('d'):
        print('d')
        update_val = (1, 0)
    else:
        update_val = (0, 0)

    p1.move(update_val)
    p2.move(update_val)

    # Draw.
    maze.draw(screen)
    p1.draw()
    p2.draw()
    pygame.display.flip()
    fpsClock.tick(fps)