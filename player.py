from pygame import draw
import keyboard

class Player:

    def __init__(self, player_id, start_pos, maze):
        self.maze = maze
        self.player_id = player_id
        self.pos = start_pos
        self.color = (0, 0, 0)

        if player_id == 0:
            self.color = (0, 0, 255) #rgb
            self.up = 'w'
            self.down = 's'
            self.left = 'a'
            self.right = 'd'
        elif player_id == 1:
            self.color = (255, 0, 0) #rgb red
            self.up = 'i'
            self.down = 'k'
            self.left = 'j'
            self.right = 'l'

    def update(self):
        if keyboard.is_pressed(self.up):
            direction = (0, -1)
        elif keyboard.is_pressed(self.left):
            direction = (-1, 0)
        elif keyboard.is_pressed(self.down):
            direction = (0, 1)
        elif keyboard.is_pressed(self.right):
            direction = (1, 0)
        else:
            direction = (0, 0)

        self.move(direction)

    def move(self, direction):
        new_pos = ((self.pos[0] + direction[0]), (self.pos[1] + direction[1]))
        if self.is_legal(new_pos):
            self.pos = new_pos
    
    def draw(self, screen):
        circle_rad = 20
        position = (20 + (self.pos[0] * 40), 20 + (self.pos[1] * 40))
        draw.circle(screen, self.color, position, circle_rad)

    def is_legal(self, new_pos):
        n = (new_pos[1] * 16) + new_pos[0]
        if self.maze.grid[n].type != "W":
            return True
        else:
            return False
