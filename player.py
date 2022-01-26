from pygame import draw
import keyboard


class Player:

    def __init__(self, player_id, start_pos, maze, serial):
        self.maze = maze
        self.player_id = player_id
        self.pos = start_pos
        self.color = (0, 0, 0)
        self.serial = serial
        self.grid_number = (self.pos[1] * 16) + self.pos[0]

        if player_id == 0:
            self.color = (0, 0, 255)  # rgb
            self.up = 'w'
            self.down = 's'
            self.left = 'a'
            self.right = 'd'
        elif player_id == 1:
            self.color = (255, 0, 0)  # rgb red
            self.up = 'i'
            self.down = 'k'
            self.left = 'j'
            self.right = 'l'

    def update(self):
        self.direction = (0, 0)
        # Keyboard Control
        if keyboard.is_pressed(self.up):
            self.direction = (0, -1)
        elif keyboard.is_pressed(self.left):
            self.direction = (-1, 0)
        elif keyboard.is_pressed(self.down):
            self.direction = (0, 1)
        elif keyboard.is_pressed(self.right):
            self.direction = (1, 0)
        self.move(self.direction)

        # nunchuck
        data = self.serial.receive_data()
        if len(data) > 5:
            if self.player_id == 0 and data[2] == 'A':
                convert = [int(data[3]), int(data[4])]
                if convert[0] == 2:
                    convert[0] = -1
                if convert[1] == 2:
                    convert[1] = -1
                self.direction = (convert[0], -convert[1])
            if self.player_id == 1 and data[5] == 'B':
                convert = [int(data[6]), int(data[7])]
                if convert[0] == 2:
                    convert[0] = -1
                if convert[1] == 2:
                    convert[1] = -1
                self.direction = (convert[0], -convert[1])
            self.move(self.direction)

    def move(self, direction):
        new_pos = ((self.pos[0] + direction[0]), (self.pos[1] + direction[1]))
        if self.is_legal(new_pos):
            self.pos = new_pos
        self.grid_number = (self.pos[1] * 16) + self.pos[0]

    def draw(self, screen):
        circle_rad = 20
        position = (20 + (self.pos[0] * 40), 20 + (self.pos[1] * 40))
        draw.circle(screen, self.color, position, circle_rad)

    def is_legal(self, new_pos):
        if new_pos[0] != -1 and new_pos[0] != 16 and new_pos[1] != -1 and new_pos[1] != 16:
            n = (new_pos[1] * 16) + new_pos[0]
            if self.maze.grid[n].type != "W":
                return True
        return False
