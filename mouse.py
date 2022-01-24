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
            if player_1.pos == step.position or player_2.pos == step.position:
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

    def new_target_(self, player_1, player_2):
        best_score = 0
        for element in self.maze.grid:
            if element.type != "W":
                dist1 = math.sqrt(
                    (player_1.pos[0] - element.position[0]) ** 2 + (player_1.pos[1] - element.position[1]) ** 2)
                dist2 = math.sqrt(
                    (player_2.pos[0] - element.position[0]) ** 2 + (player_2.pos[1] - element.position[1]) ** 2)
                dist3 = math.sqrt((element.position[0] - self.pos[0]) ** 2 + (element.position[1] - self.pos[1]) ** 2)
                destination_safety = dist1 + dist2 + dist3

                self.maze.target = element
                self.new_path()
                path_safety = 0

                for step in self.path:
                    p1_dist = math.sqrt((player_1.pos[0] - step.position[0]) ** 2 + (player_1.pos[1] - step.position[1]) ** 2)
                    p2_dist = math.sqrt((player_2.pos[0] - step.position[0]) ** 2 + (player_2.pos[1] - step.position[1]) ** 2)
                    path_safety += p1_dist + p2_dist
                path_safety /= (len(self.path) + 1)
                print(path_safety)

                element.safety_score = path_safety + destination_safety
                element.color = (255 - 3 * element.safety_score, 0, 0)
            if (element.safety_score > best_score) and element not in self.previous_targets:
                best_score = element.safety_score
                self.maze.target = element
        self.previous_targets.append(self.maze.target)
        if len(self.previous_targets) > 5:
            self.previous_targets.pop(0)


    def new_target(self, player_1, player_2):
        best_score = 0
        #calculate element safety
        for element in self.maze.grid:
            if element.type != "W":
                self.check_element_safety(player_1, player_2, element)
                #element.color = (255 - 5 * element.safety_score, 0, 0)

        for possible_destination in self.maze.grid:
            if possible_destination.type != "W":
                self.check_path_safety(possible_destination)

            total_safety_score = possible_destination.destination_safety_score + 2 * possible_destination.destination_safety_score
            red = 255 - 2 * total_safety_score
            if red < 0:
                red = 0
            elif red > 255:
                red = 255
            possible_destination.color = (red, 0, 0)

            if (total_safety_score > best_score) and (possible_destination.position != self.pos):
                best_score = total_safety_score
                self.next_pos = possible_destination
        self.maze.target = self.next_pos
        print(self.maze.target.position)
        print(self.pos)
        self.maze.target.color = (0,255,0)
        print("done")


    def check_element_safety(self, player_1, player_2, element):
        dist1 = math.sqrt(
            (player_1.pos[0] - element.position[0]) ** 2 + (player_1.pos[1] - element.position[1]) ** 2)
        dist2 = math.sqrt(
            (player_2.pos[0] - element.position[0]) ** 2 + (player_2.pos[1] - element.position[1]) ** 2)
        dist3 = math.sqrt((element.position[0] - self.pos[0]) ** 2 + (element.position[1] - self.pos[1]) ** 2)
        paths_available = (len(element.neighbours) - 2)
        safety_score = dist1 + dist2 + (0.5 * dist3) + (10 * paths_available)
        if dist1 == 0 or dist2 == 0:
            safety_score -= 999
        element.safety_score = safety_score

    def check_path_safety(self, possible_destination):
        self.maze.target = possible_destination
        self.new_path()
        path_safety = 0
        for element in self.path:
            path_safety = path_safety + element.safety_score
        path_safety = path_safety / (len(self.path) + 1)
        possible_destination.destination_safety_score = path_safety
        possible_destination.color = (255 - 5 * possible_destination.destination_safety_score, 0, 0)














    def new_target__(self, player_1, player_2):
        best_score = 0
        for element in self.maze.grid:
            if element.type != "W":
                dist1 = math.sqrt(
                    (player_1.pos[0] - element.position[0]) ** 2 + (player_1.pos[1] - element.position[1]) ** 2)
                dist2 = math.sqrt(
                    (player_2.pos[0] - element.position[0]) ** 2 + (player_2.pos[1] - element.position[1]) ** 2)
                dist3 = math.sqrt((element.position[0] - self.pos[0]) ** 2 + (element.position[1] - self.pos[1]) ** 2)
                paths_available = (len(element.neighbours) - 2)
                safety_score = dist1 + dist2 + (0.5 * dist3) + (7 * paths_available)
                element.safety_score = safety_score
                element.color = (255 - 5 * element.safety_score, 0, 0)
                print(element.color)
            if (element.safety_score > best_score) and element not in self.previous_targets:
                best_score = element.safety_score
                self.maze.target = element
        self.previous_targets.append(self.maze.target)
        if len(self.previous_targets) > 5:
            self.previous_targets.pop(0)




