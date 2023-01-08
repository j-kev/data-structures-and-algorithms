class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def norm(self):
        return (self.x**2 + self.y**2 + self.z**2) ** 0.5

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

    def __str__(self):
        return "(%f, %f, %f)" %(self.x, self.y, self.z)


v = Vector(3, 4, 1)
u = Vector(3, 6, 0)
print(v.norm())
print(Vector(5, 12, 5).norm())
print(v + u)

