from pygame import draw
from pygame import Color

class Player:

    def __init__(self, player_id, start_pos, screen):
        self.screen = screen
        self.player_id = player_id
        player_pos = start_pos
        player_color = Color(0, 0, 0)

        if player_id == 0:
            player_color = Color(0, 0, 255) #rgb blue
        elif player_id == 1:
            player_color = Color(255, 0, 0) #rgb red

    def move(self, player_pos):
        pass
    
    def draw_player(self):
        circle_rad = 20
        draw.circle(self.screen, self.player_color, self.player_pos, circle_rad)
