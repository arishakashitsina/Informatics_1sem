from cmath import sqrt


def scp(self, other):
    return self.x * other.x, self.y * other.y, self.z * other.z


def mul(self, other):
    return self.x * other, self.y * other, self.z * other


class Vector:
    def __init__(self, x, y, z):
        assert (isinstance(x, int))
        assert (isinstance(y, int))
        assert (isinstance(z, int))
        self.x = x
        self.y = y
        self.z = z

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z

    def __mul__(self, other):
        if isinstance(other, int):
            return mul(self, other)
        return scp(self, other)