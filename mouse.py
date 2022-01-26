#import modules:
from pygame import draw
from pygame import Color
from search import Search
import math

class Mouse:
    #this class controls the mouse in the game. It can find a suitable destination and path, and it can change this when a player gets too close

    def __init__(self, start_pos, maze):
        self.maze = maze    #the maze the mouse navigates
        self.pos = start_pos    #the mouse's starting coordinates
        self.grid_number = (self.pos[1] * 16) + self.pos[0] #the position of the mouse in the grid list
        self.mouse_color = Color(50, 150, 50)   #mouse's color in pygame window
        self.search = Search(maze)  #search object for
        self.path = []  #contains the mouse's path for calculations and next moves


    def move(self, player_1, player_2):
        for step in self.path:  #if the player comes too close to the mouse's current path
            if (abs(player_1.pos[0] - step.position[0]) < 2 and abs(player_1.pos[1] - step.position[1]) < 2) or abs((player_2.pos[0] - step.position[0]) < 2 and abs(player_2.pos[1] - step.position[1]) < 2):
                self.new_target(player_1, player_2)
                self.new_path() #find a new target and calculate the path to it

        if len(self.path) > 0:  #if there is something in the path list
            next_move = self.path.pop() #take the next move and move there
            self.pos = next_move.position
            self.maze.start = next_move #adjust the mouse position in the maze as well
        else:
            self.new_target(player_1, player_2)
            self.new_path() #if the destination is reached, find a new target and calculate the path
        self.grid_number = (self.pos[1] * 16) + self.pos[0] #update the mouse's position in the grid list


    def draw(self, screen):
        circle_rad = 20
        position = (20 + self.pos[0] * 40, 20 + self.pos[1] * 40) #calculate position on screen
        draw.circle(screen, self.mouse_color, position, circle_rad) #draw a circle in the position of the mouse object in the grid

    def new_path(self):
        self.search.greedy()    #find a path using greedy search
        self.path = self.search.get_path()  #compute the path and put it in the path list

    def new_target(self, player_1, player_2): #this method uses heuristics to calculate a safe destination
        best_score = 0
        #calculate position safety
        for element in self.maze.grid:
            if element.type != "W": #for all elements in the grid that are not walls:
                self.check_element_safety(player_1, player_2, element)
                #element.color = (255 - 5 * element.safety_score, 0, 0) #for debugging purposes

        for possible_destination in self.maze.grid:
            if possible_destination.type != "W":    #for every possible destination in the grid that isn't a wall
                self.check_path_safety(possible_destination)    #check how safe the path is
            #add the weighted scores:
            total_safety_score = possible_destination.destination_safety_score + 2 * possible_destination.destination_safety_score
            '''#for debugging purposes:
            red = 255 - 2 * total_safety_score
            if red < 0:
                red = 0
            elif red > 255:
                red = 255
            possible_destination.color = (red, 0, 0)
            #this colors the squares a shade of red according to their total safety score
            '''#update the best safety score that is not the current position of the mouse
            if (total_safety_score > best_score) and (possible_destination.position != self.pos):
                best_score = total_safety_score
                self.next_pos = possible_destination
        self.maze.target = self.next_pos    #set the target to the position with best calculated score
        #print(self.maze.target.position)
        #print(self.pos)
        #self.maze.target.color = (0,255,0) #for debugging purposes


    def check_element_safety(self, player_1, player_2, element):
        #this method uses heuristics to estimate the safety of a position on the grid
        #the distance from the position to player 1, more is safer:
        dist1 = math.sqrt(
            (player_1.pos[0] - element.position[0]) ** 2 + (player_1.pos[1] - element.position[1]) ** 2)
        #the distance from the position to player 2, more is safer:
        dist2 = math.sqrt(
            (player_2.pos[0] - element.position[0]) ** 2 + (player_2.pos[1] - element.position[1]) ** 2)
        #the amount of available neighbours from that position, this prevents it from being trapped in corners:
        paths_available = (len(element.neighbours) - 2)
        safety_score = dist1 + dist2 + (20 * paths_available)   #add the weighted scores
        if dist1 == 0 or dist2 == 0:
            safety_score -= 999 #if the player is in this position, it is very dangerous
        if element.position[0] == 0 or element.position[0] == 15:
            safety_score -= 10 #the outer walls are more dangerous
        if element.position[1] == 0 or element.position[1] == 15:
            safety_score -= 10
        element.safety_score = safety_score #update the safety score

    def check_path_safety(self, possible_destination):
        #this method checks the safety of the path to a possible destination
        self.maze.target = possible_destination
        self.new_path() #set the possible destination as target and compute a path
        path_safety = 0
        for element in self.path:   #go over all positions in the path and add their safety score
            path_safety = path_safety + element.safety_score
        path_safety = path_safety / (len(self.path) + 0.5)  #devide by the amount of positions +0.5 (to encourage the mouse to move)
        possible_destination.destination_safety_score = path_safety #update the safety score
        #for debugging purposes:
        #possible_destination.color = (255 - 5 * possible_destination.destination_safety_score, 0, 0)




