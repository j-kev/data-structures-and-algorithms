class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def norm(self):
        return (self.x**2 + self.y**2) ** 0.5

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

    def __str__(self):
        return "(%f, %f)" %(self.x, self.y)


v = Vector(3, 4)
u = Vector(3, 6)
print(v.norm())
print(Vector(5, 12).norm())
print(v + u)

