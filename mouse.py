from pygame import draw
from pygame import Color

class Mouse:

    def __init__(self, start_pos, screen):
        self.screen = screen
        mouse_pos = start_pos
        mouse_color = Color(0, 0, 0)

    def move(self, x_pos, y_pos, nunchuck_input):
        nunchuck_input = (0, 0)
        mouse_pos = nunchuck_input

    def draw_player(self):
        circle_rad = 20
        draw.circle(self.screen, self.mouse_color, self.mouse_pos, circle_rad)
