from pygame import draw
from pygame import Color


class Player:

    def __init__(self, player_id, start_pos, screen):
        self.screen = screen
        self.player_id = player_id
        self.player_pos = (start_pos[0] * 40 + 20, start_pos[1] * 40 + 20)
        self.player_color = Color(0, 0, 0)

        if player_id == 0:
            self.player_color = Color(0, 0, 255) #rgb blue
        elif player_id == 1:
            self.player_color = Color(255, 0, 0) #rgb red

    def move(self, update_val):
        self.player_pos = (self.player_pos[0] + update_val[0]*40, self.player_pos[1] - update_val[1]*40)
        print(self.player_pos, update_val)

    def draw(self):
        circle_rad = 20
        self.player_pos = (self.player_pos[0], self.player_pos[1])
        draw.circle(self.screen, self.player_color, self.player_pos, circle_rad)
