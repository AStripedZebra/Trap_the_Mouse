import pygame

class Grid_element:

    def __init__(self, number, element_type):
        self.y = int(number / 16)
        self.x = number % 16
        self.type = element_type
        self.color = (0,0,0)
        if self.type == "W":
            self.color = (100, 100, 100)


    def set_type(self, new_type):
        self.type = new_type

    def __str__(self):
        return self.type

    def draw(self, surface):
        pixel = pygame.Rect(320 + self.x, 320 + self.y, 40, 40)
        pixel.inflate(400,400)
        pygame.draw.rect(surface, self.color, pixel)
