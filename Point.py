class Point:
    def __init__(self, is_inf, x=0, y=0):
        self.is_inf = is_inf
        self.x = x
        self.y = y

    def __hash__(self):
        return hash((self.x, self.y, self.is_inf))

    def __eq__(self, other):
        if (self.is_inf or other.is_inf):
            return self.is_inf and other.is_inf
        else:
            return self.x == other.x and self.y == self.y

    def __repr__(self):
        if self.is_inf:
            return "inf"
        else:
            return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __str__(self):
        if self.is_inf:
            return "inf"
        else:
            return "(" + str(self.x) + ", " + str(self.y) + ")"

    def print_point(self):
        print("(", self.x, ",", self.y, ")")

    def inv(self):
        return Point(self.is_inf, self.x, - self.y)



