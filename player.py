
class Player:

    def __init__(self, player_id, start_pos, screen):
        self.screen = screen
        self.player_id = player_id
        self.pos = start_pos
        self.color = (0, 0, 0)

        if player_id == 0:
            self.color = (0, 0, 255) #rgb blue
        elif player_id == 1:
            self.color = (255, 0, 0) #rgb red

    def move(self, player_pos):
        pass
    
    def draw_player(self):
        circle_rad = 20
        draw.circle(self.screen, self.color, self.pos, circle_rad)
