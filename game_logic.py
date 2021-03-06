import pygame


class Game_logic:

    def __init__(self, player1, player2, mouse, screen):
        self.p1 = player1
        self.p2 = player2
        self.mouse = mouse
        self.screen = screen
        self.game_over_bg_color = (0, 0, 255)  # rgb
        self.game_over = False

    # function that checks whether a player is on top of the mouse
    # it will return true which will mean that the game is over
    def game_is_over(self):
        if self.p1.pos == self.mouse.pos:
            self.game_over = True
        if self.p2.pos == self.mouse.pos:
            self.game_over = True
        return self.game_over
