from pygame import draw

class player():

    x_pos = 0
    y_pos = 0

    def __init__(self, player_id, start_x, start_y):
        player_id = 0
        x_pos = start_x
        y_pos = start_y

    def move(self, x_pos, y_pos, nunchuck_x, nunchuck_y):
        x_pos = x_pos + nunchuck_x
        y_pos = y_pos + nunchuck_y

    def draw_player():
        draw.circle
