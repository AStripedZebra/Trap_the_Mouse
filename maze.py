class Maze:

    def __init__(self, screen_size):
        self.grid_size = (16, 16)
        self.pixel_width = screen_size[0] / self.grid_size[0]
        self.pixel_height = screen_size[1] / self.grid_size[1]
        self.grid = []
        for n in range(256):
            self.grid.append(" ")

        for y in range(16):
            for x in range(16):
                self.grid[x] = "W"

    def print_maze(self):
        for y in range(16):
            print(self.grid[(y * 16):(16 + (y * 16))])
        for i in range(len(self.grid)):
            y = int(i/16)
            x = i % 16
            print((x,y))

    def draw_maze(self, surface):
        for row in self.grid:
            for element in row:
                element.draw_grid_element(surface)
        return None

    def possible_neighbours(self, cell):
        pass

    def generate_maze(self):
        pass
