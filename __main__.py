# import libraries
import sys
import pygame
import winsound
from player import Player
from game_logic import Game_logic
from serial_communication import Serial_communication
from mouse import Mouse
from maze import Maze
from pygame.locals import *

pygame.init()

# setting Fps rate of the game
fps = 5
fpsClock = pygame.time.Clock()

# create screen
width, height = 640, 640
screen = pygame.display.set_mode((width, height))

# create serial communication
serial = Serial_communication()

# create game objects
maze = Maze()
p1 = Player(0, (0, 0), maze, serial)
p2 = Player(1, (15, 0), maze, serial)
mouse = Mouse((15, 15), maze)

# create game logics
game_logic = Game_logic(p1, p2, mouse, screen)
game_over_sound = 'Wilhelm Scream.wav'

# Game loop.
while True:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update.
    mouse.new_path()
    mouse.move(p1, p2)
    p1.update()
    p2.update()

    # Draw
    serial.send_data(p1, p2, mouse)
    maze.draw(screen)
    mouse.draw(screen)
    p1.draw(screen)
    p2.draw(screen)
    pygame.display.flip()
    fpsClock.tick(fps)

    # When the players win a sound will be played and the code breaks out the game loop
    if game_logic.game_is_over():
        winsound.PlaySound(game_over_sound, winsound.SND_FILENAME)
        break
