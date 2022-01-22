from pygame import draw
from pygame import Color


class Mouse:

    def __init__(self, start_pos, player1, player2, screen):
        self.screen = screen
        mouse_pos = start_pos
        mouse_color = Color(0, 0, 0)

        p1 = player1
        p2 = player2

    def move(self, x_pos, y_pos, nunchuck_input):
        pass

    def draw_player(self):
        circle_rad = 20
        draw.circle(self.screen, self.mouse_color, self.mouse_pos, circle_rad)

    def escape_AI(self):
        pass

    def get_possible_moves(self, maze):
        pass
