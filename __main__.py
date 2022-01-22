import sys
import pygame
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

p1 = Player(0, (0, 0), screen)
p2 = Player(1, (16, 0), screen)
mouse = Mouse((16, 16), p1, p2, screen)

# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.

    # Draw.
    maze.draw(screen)
    pygame.display.flip()
    fpsClock.tick(fps)