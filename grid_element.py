import pygame

class Grid_element:
    #this class manages the elements and contains methods needed mainly for the search algorithm
    def __init__(self, n, element_type):
        self.number = n #number in the grid list
        self.y = int(self.number / 16)  #x position in matrix
        self.x = self.number % 16   #y position in matrix
        self.type = element_type    #type can be wall (W) or open (_)
        self.neighbours = []    #list of neighbours, empty on intitialization
        self.parent = None  #variables for parent, distance and manhattan score
        self.distance = None
        self.score = None
        self.position = (self.x, self.y)
        self.safety_score = 0   #two types of safety score for the mouse
        self.destination_safety_score = 0
        if self.type == "W":    #color according to the type of element
            self.color = (100, 100, 100)
        else:
            self.color = (0, 0, 0)

    def draw(self, surface):    #this method draws the element as a 40*40 square on the screen
        pixel = pygame.Rect(self.x * 40, self.y * 40, 40, 40)
        pygame.draw.rect(surface, self.color, pixel)

    def reset_state(self):
        #this method resets all variables altered during search
        self.parent = None
        self.score = None
        self.distance = None
        if self.type == "W":
            self.color = (100, 100, 100)
        else:
            self.color = (0, 0, 0)
            pass

    def get_neighbours(self):
        #gives the neighbours
        return self.neighbours[:]

    def manhattan_distance(self, other):
        #calculates manhattan distance to another element
        return abs(self.x - other.x) + abs(self.y - other.y)

    def set_parent(self, parent):
        #this method sets its parent to what the input is, also it gives the distance accordingly
        self.parent = parent
        if parent.distance is not None:
            self.distance = parent.distance+1

    def set_color(self, new_color):
        self.color = new_color

    def set_score(self, score):
        self.score = score

    #overloading some of the oparators to perform comparisons easily
 
    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return (self.score is not None) and (other.score is None or self.score < other.score)

    def __repr__(self):
        return "[%s, %s, %s]" % (self.position, self.score, self.type)

    #def __str__(self):
     #   return self.type