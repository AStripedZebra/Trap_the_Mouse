from grid_element import *

class Maze:

    def __init__(self):
        self.grid_size = (16, 16)
        self.grid = []


        self.blueprint = (
            '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', 'W', 'W', 'W', 'W', 'W', '_', 'W', 'W', '_', 'W', 'W', 'W', 'W', 'W', '_',
            '_', 'W', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'W', '_',
            '_', 'W', '_', 'W', '_', 'W', 'W', 'W', 'W', 'W', 'W', '_', 'W', '_', 'W', '_',
            '_', 'W', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'W', '_',
            '_', 'W', '_', 'W', '_', 'W', 'W', '_', '_', 'W', 'W', '_', 'W', '_', 'W', '_',
            '_', '_', '_', 'W', '_', 'W', '_', '_', '_', '_', 'W', '_', 'W', '_', '_', '_',
            '_', 'W', '_', 'W', '_', '_', '_', 'W', 'W', '_', '_', '_', 'W', '_', 'W', '_',
            '_', 'W', '_', 'W', '_', '_', '_', 'W', 'W', '_', '_', '_', 'W', '_', 'W', '_',
            '_', ' ', '_', 'W', '_', 'W', '_', '_', '_', '_', 'W', '_', 'W', '_', '_', '_',
            '_', 'W', '_', 'W', '_', 'W', 'W', '_', '_', 'W', 'W', '_', 'W', '_', 'W', '_',
            '_', 'W', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'W', '_',
            '_', 'W', '_', 'W', '_', 'W', 'W', 'W', 'W', 'W', 'W', '_', 'W', '_', 'W', '_',
            '_', 'W', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'W', '_',
            '_', 'W', 'W', 'W', 'W', 'W', '_', 'W', 'W', '_', 'W', 'W', 'W', 'W', 'W', '_',
            '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
        )

        n = 0
        for type in self.blueprint:
            element = Grid_element(n, type)
            self.grid.append(element)
            n += 1

        self.start = self.grid[255]
        self.target = self.grid[8]

        for element in self.grid:
            element.neighbours = self.possible_neighbours(element)

    def print_maze(self):
        print(" ", end='')

        for i in range(16):
            print("_  ", end='')
        print("")

        print("|", end='')
        for element in self.grid:
            print(element, end='')
            print("  ", end='')
            if element.x == 15:
                print("|")
                if element.y != 15:
                    print("|", end='')

    def draw(self, surface):
        for element in self.grid:
            element.draw(surface)

    def possible_neighbours(self, element):
        neighbours = []
        number = element.number
        if number >= 16:
            if self.grid[number - 16].type != "W": #north
                neighbours.append(self.grid[number - 16])
        if number % 16 < 15:
            if self.grid[number + 1].type != "W": #east
                neighbours.append(self.grid[number + 1])
        if number < 240:
            if self.grid[number + 16].type != "W": #south
                neighbours.append(self.grid[number + 16])
        if number % 16 > 0:
            if self.grid[number - 1].type != "W": #west
                neighbours.append(self.grid[number - 1])
        return neighbours

    def set_start(self, start_element):
        self.start = start_element

    def reset_state(self):
        for element in self.grid:
            element.reset_state()
