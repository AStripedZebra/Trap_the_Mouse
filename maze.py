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
            element = grid_element(n, type)
            self.grid.append(element)
            n += 1

        #for y in range(16):
            #for x in range(16):
                #self.grid[x] = "W"

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

    def draw_maze(self, surface):
        for row in self.grid:
            for element in row:
                element.draw_grid_element(surface)
        return None

    def possible_neighbours(self, cell):
        pass

    def generate_maze(self):
        pass
