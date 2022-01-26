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

        # set keyboard input and color per player
        # player 1 uses wasd and is blue
        if player_id == 0:
            self.color = (0, 0, 255)  # rgb
            self.up = 'w'
            self.down = 's'
            self.left = 'a'
            self.right = 'd'
        # player 2 uses ijkl and is red
        elif player_id == 1:
            self.color = (255, 0, 0)  # rgb red
            self.up = 'i'
            self.down = 'k'
            self.left = 'j'
            self.right = 'l'

    # update/move the player
    def update(self):

        # Default/null direction
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

        # nunchuck control
        # the data that is sent is A int int B int int. the ints are either 012:
        # 0 = don't move, 1 = move up/right & 2 = move down/down
        # The letter represents the nunchuck A = 1 & B = 2
        # The first int is always the x-coordinate and the second is the y-coordinate

        data = self.serial.receive_data()
        if len(data) > 5:
            # converts & reads data for player 1
            if self.player_id == 0 and data[2] == 'A':
                convert = [int(data[3]), int(data[4])]
                if convert[0] == 2:
                    convert[0] = -1
                if convert[1] == 2:
                    convert[1] = -1
                self.direction = (convert[0], -convert[1])

            # converts & reads data for player 2
            if self.player_id == 1 and data[5] == 'B':
                convert = [int(data[6]), int(data[7])]
                if convert[0] == 2:
                    convert[0] = -1
                if convert[1] == 2:
                    convert[1] = -1
                self.direction = (convert[0], -convert[1])
            self.move(self.direction)

    # updates/moves the player
    def move(self, direction):
        new_pos = ((self.pos[0] + direction[0]), (self.pos[1] + direction[1]))
        # checks if the move is legal
        if self.is_legal(new_pos):
            self.pos = new_pos
        self.grid_number = (self.pos[1] * 16) + self.pos[0]

    # draws the player
    def draw(self, screen):
        circle_rad = 20
        position = (20 + (self.pos[0] * 40), 20 + (self.pos[1] * 40))
        draw.circle(screen, self.color, position, circle_rad)

    # Check if a move is legal
    def is_legal(self, new_pos):
        #Check if a move is not outside the grid
        if new_pos[0] != -1 and new_pos[0] != 16 and new_pos[1] != -1 and new_pos[1] != 16:
            n = (new_pos[1] * 16) + new_pos[0]

            #Check if a move is not towards a wall
            if self.maze.grid[n].type != "W":
                return True
        return False
