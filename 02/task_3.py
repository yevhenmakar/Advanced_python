class Point:

    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def __add__(self, other):
        return Point(self.get_x() + other.get_x(), self.get_y() + other.get_y(), self.get_z() + other.get_z())

    def __sub__(self, other):
        return Point(self.get_x() - other.get_x(), self.get_y() - other.get_y(), self.get_z() - other.get_z())

    def __mul__(self, other):
        return Point(self.get_x() * other.get_x(), self.get_y() * other.get_y(), self.get_z() * other.get_z())

    def __truediv__(self, other):
        return Point(self.get_x() / other.get_x(), self.get_y() / other.get_y(), self.get_z() / other.get_z())

    def __abs__(self):
        return abs(self.get_x()), abs(self.get_y()), abs(self.get_z())


first_point = Point(10, 12, 15)
second_point = Point(2, -3, -5)

print(first_point.get_x(), first_point.get_y(), first_point.get_z())
print(second_point.get_x(), second_point.get_y(), second_point.get_z())

result = first_point + second_point
print((result.get_x(), result.get_y(), result.get_z()))

result = first_point - second_point
print((result.get_x(), result.get_y(), result.get_z()))

result = first_point * second_point
print((result.get_x(), result.get_y(), result.get_z()))

result = first_point / second_point
print((result.get_x(), result.get_y(), result.get_z()))

result = abs(first_point)
print(result)