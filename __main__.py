import sys
import pygame
import keyboard
from player import Player
from game_logic import Game_logic
from serial_communication import Serial_communication
from mouse import Mouse
from maze import Maze
from pygame.locals import *
from pydub import AudioSegment
from pydub.playback import play

pygame.init()

fps = 5
fpsClock = pygame.time.Clock()

width, height = 640, 640
screen = pygame.display.set_mode((width, height))
maze = Maze()
serial = Serial_communication()

p1 = Player(0, (0, 0), maze, serial)
p2 = Player(1, (15, 0), maze, serial)
mouse = Mouse((15, 15), maze)
game_logic = Game_logic(p1, p2, mouse, screen)

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

    if game_logic.game_is_over():
        break
