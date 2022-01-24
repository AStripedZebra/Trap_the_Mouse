from pygame import draw
from pygame import Color
from search import Search
import math

class Mouse:

    def __init__(self, start_pos, maze):
        self.maze = maze
        self.pos = start_pos
        self.previous_targets = []
        self.mouse_color = Color(50, 150, 50)
        self.search = Search(maze)
        self.path = []

    def move(self, player_1, player_2):
        for step in self.path:
            while player_1.pos == step.position or player_2.pos == step.position:
                self.new_target(player_1, player_2)
                self.new_path()
        if len(self.path) > 0:
            next_move = self.path.pop()
            self.pos = next_move.position
            self.maze.start = next_move
        else:
            self.new_target(player_1, player_2)
            self.new_path()

    def draw(self, screen):
        circle_rad = 20
        position = (20 + self.pos[0] * 40, 20 + self.pos[1] * 40)
        draw.circle(screen, self.mouse_color, position, circle_rad)

    def new_path(self):
        self.search.greedy(self.pos)
        self.path = self.search.get_path()

    def new_target(self, player_1, player_2):
        best_score = 0
        for element in self.maze.grid:
            if element.type != "W":
                dist1 = math.sqrt((player_1.pos[0] - element.position[0]) ** 2 + (player_1.pos[1] - element.position[1]) ** 2)
                dist2 = math.sqrt((player_2.pos[0] - element.position[0]) ** 2 + (player_2.pos[1] - element.position[1]) ** 2)
                dist3 = math.sqrt((element.position[0] - self.pos[0]) ** 2 + (element.position[1] - self.pos[1]) ** 2)
                paths_available = (len(element.neighbours) - 2)
                safety_score = dist1 + dist2 + (0.5 * dist3) + (7 * paths_available)
                element.safety_score = safety_score
            if (element.safety_score > best_score) and element not in self.previous_targets:
                best_score = element.safety_score
                self.maze.target = element
        self.previous_targets.append(self.maze.target)
        if len(self.previous_targets) > 5:
            self.previous_targets.pop(0)






