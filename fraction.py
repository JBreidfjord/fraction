def gcd(a, b):
    while a % b != 0:
        prev_a, prev_b = a, b
        a = prev_b
        b = prev_a % prev_b
    return b

class Fraction:
    def __init__(self, num: int, den: int):
        common = gcd(den, num)
        self.num = int(num / common)
        self.den = int(den / common)

    def __repr__(self):
        return f'Fraction({self.num},{self.den})'

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __add__(self, other):
        num = (self.num * other.den) + (other.num * self.den)
        den = self.den * other.den
        return Fraction(num, den)

    def __sub__(self, other):
        num = (self.num * other.den) - (other.num * self.den)
        den = self.den * other.den
        return Fraction(num, den)

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def __eq__(self, other) -> bool:
        num_1 = self.num * other.den
        num_2 = self.den * other.num
        return num_1 == num_2

    def __ne__(self, other) -> bool:
        num_1 = self.num * other.den
        num_2 = self.den * other.num
        return num_1 != num_2

    def __gt__(self, other) -> bool:
        num_1 = self.num * other.den
        num_2 = self.den * other.num
        return num_1 > num_2

    def __ge__(self, other) -> bool:
        num_1 = self.num * other.den
        num_2 = self.den * other.num
        return num_1 >= num_2

    def __lt__(self, other) -> bool:
        num_1 = self.num * other.den
        num_2 = self.den * other.num
        return num_1 < num_2

    def __le__(self, other) -> bool:
        num_1 = self.num * other.den
        num_2 = self.den * other.num
        return num_1 <= num_2

    # todo:
    # We'd like to use arithmetic operations between our fractions and integers or floats
    # If we have a negative fraction, the sign is applied to the denominator which doesn't look very nice
    # Conversion from fraction to float
    # Allowing a Fraction object to be created from a single float input
    # Reflected arithmetic operators after implementing operations with ints and floats