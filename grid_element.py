import pygame.draw


class Grid_element:

    def __init__(self, number, element_type):
        self.y = int(number / 16)
        self.x = number % 16
        self.type = element_type
        if self.type == "W":
            self.color = (30, 30, 30)
        if self.type == "_":
            self.color = (0, 0, 0)


    def set_type(self, new_type):
        self.type = new_type

    def __str__(self):
        return self.type

    def draw(self, surface):
        pixel = pygame.Rect(self.x + 0, self.y + 0, 40, 40)
        pygame.draw.rect(surface, self.color, pixel)
