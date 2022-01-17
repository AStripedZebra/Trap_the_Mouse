class grid_element:

    def __init__(self, number, element_type):
        self.y = int(number / 16)
        self.x = number % 16
        self.type = element_type

    def set_type(self, new_type):
        self.type = new_type

    def __str__(self):
        return self.type
