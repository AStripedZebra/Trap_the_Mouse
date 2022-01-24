import sys
import pygame
import keyboard
from player import Player
from mouse import Mouse
from maze import Maze
from pygame.locals import *

pygame.init()

fps = 3
fpsClock = pygame.time.Clock()

width, height = 640, 640
screen = pygame.display.set_mode((width, height))
maze = Maze()

p1 = Player(0, (0, 0), maze)
p2 = Player(1, (15, 0), maze)
mouse = Mouse((15, 15), maze)

# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.
    #mouse.new_path()
    mouse.move(p1, p2)
    p1.update()
    p2.update()


    # Draw.
    maze.draw(screen)
    mouse.draw(screen)
    p1.draw(screen)
    p2.draw(screen)
    pygame.display.flip()
    fpsClock.tick(fps)
