class pos:
    def __init__(self, wall, x, y):
        self.wall = wall
        self.x = x
        self.y = y
        self.inherit = None
        self.g = 1000
        self.h = None  # heuristic
        self.f = None


    def __lt__(self, other): 
        if isinstance(other, self.__class__):
            return self.h < other.h
        return False

    # note: THIS IS NOT MANHATTAN DISTANCE, the commented out part is, the actual heuristic isn't,
    # i changed it to euclidean
    def set_manhattan(self, exit_pos):
        self.h = (((self.x - exit_pos.x) ** 2) + ((self.y - exit_pos.y) ** 2)) ** .5
       #self.h = abs((self.x - exit_pos.x) + (self.y - exit_pos.y))


    def set_f(self):
        self.f = self.g + self.h

    def check_g(self, inherit):
        if inherit.g + 1 < self.g:
            return True
        else:
            return False