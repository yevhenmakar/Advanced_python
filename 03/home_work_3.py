class ComplexNumber:

    def __init__(self, real, imag=0.0):
        self._real = real
        self._imag = imag

    def get_real(self):
        return self._real

    def get_imag(self):
        return self._imag

    def __add__(self, other):
        return ComplexNumber(self.get_real() + other.get_real(), self.get_imag() + other.get_imag())

    def __sub__(self, other):
        return ComplexNumber(self.get_real() - other.get_real(), self.get_imag() - other.get_imag())

    def __mul__(self, other):
        return ComplexNumber(self.get_real() * other.get_real() - self.get_imag() * other.get_imag(),
                             self.get_imag() * other.get_real() + self.get_real() * other.get_imag())

    def __truediv__(self, other):
        r = other.get_real() ** 2 + other.get_imag() ** 2
        return ComplexNumber(((self.get_real() * other.get_real() + self.get_imag() * other.get_imag()) / r),
                             ((self.get_imag() * other.get_real() - self.get_real() * other.get_imag()) / r))


z1 = ComplexNumber(7, -4)
z2 = ComplexNumber(3, 2)

result = z1 + z2
print(result.get_real(), result.get_imag())

result = z1 - z2
print(result.get_real(), result.get_imag())

result = z1 * z2
print(result.get_real(), result.get_imag())

result = z1 / z2
print(result.get_real(), result.get_imag())