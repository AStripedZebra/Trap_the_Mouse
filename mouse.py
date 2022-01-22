from pygame import draw
from pygame import Color
from search import Search
import maze

class Mouse:

    def __init__(self, start_pos):
        self.pos = start_pos
        self.mouse_color = Color(0, 255, 0)

        search = Search(maze, self.pos)


    def move(self):
        pass

    def draw(self, screen):
        circle_rad = 20
        draw.circle(screen, self.mouse_color, self.pos, circle_rad)
