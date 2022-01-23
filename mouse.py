from pygame import draw
from pygame import Color
from search import Search

class Mouse:

    def __init__(self, start_pos, maze):
        self.maze = maze
        self.pos = start_pos
        self.mouse_color = Color(0, 255, 0)
        self.search = Search(maze)

    def move(self):
        if len(self.path) > 0:
            next_move = self.path.pop()
            print(next_move)

        else:
            self.new_target()

    def draw(self, screen):
        circle_rad = 20
        draw.circle(screen, self.mouse_color, self.pos, circle_rad)

    def new_path(self):
        self.search.greedy(self.pos)
        self.path = self.search.get_path()

    def new_target(self):
        self.maze.target = self.maze.grid[255]

