import pygame

class Grid_element:

    def __init__(self, n, element_type):
        self.number = n
        self.y = int(self.number / 16)
        self.x = self.number % 16
        self.type = element_type
        self.neighbours = []
        self.parent = None
        self.distance = None
        self.score = None
        self.position = (self.x, self.y)
        self.safety_score = 0
        self.destination_safety_score = 0
        if self.type == "W":
            self.color = (100, 100, 100)
        else:
            self.color = (0, 0, 0)


    def set_type(self, new_type):
        self.type = new_type

    def draw(self, surface):
        pixel = pygame.Rect(self.x * 40, self.y * 40, 40, 40)
        pygame.draw.rect(surface, self.color, pixel)

    def reset_neighbours(self):
        self.neighbours = []

    def reset_state(self):
        self.parent = None
        self.score = None
        self.distance = None
        if self.type == "W":
            self.color = (100, 100, 100)
        else:
            #self.color = (0, 0, 0)
            pass

    def get_neighbours(self):
        return self.neighbours[:]

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def set_parent(self, parent):
        self.parent = parent
        if parent.distance is not None:
            self.distance = parent.distance+1

    def set_color(self, new_color):
        self.color = new_color

    def set_score(self, score):
        self.score = score
 
    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return (self.score is not None) and (other.score is None or self.score < other.score)

    def __repr__(self):
        return "[%s, %s, %s]" % (self.position, self.score, self.type)

    #def __str__(self):
     #   return self.type