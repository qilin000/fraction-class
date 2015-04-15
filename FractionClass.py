class Fraction:
    """A Fraction class.
    Supports + - * / arithmetic (between Fractions and integers, floats)
    and
    == !=  > >= < <= operators (between two Fractions). """

    def __init__(self, top, bottom):
        if type(top) is int and type(bottom) is int:
            self.common = self.gcd(top, bottom)
            self.num = top//self.common
            self.den = bottom//self.common
        else:
            raise TypeError("Must be integer")

    def __str__(self):
        if self.num == 0:
            return "0"

        elif self.den == 1:
            return str(self.num)

        elif self.num == self.den:
            return "1"

        else:
            return str(self.num)+"/"+str(self.den)

    def __repr__(self):
        if self.num == 0:
            return "0"

        elif self.den == 1:
            return str(self.num)

        elif self.num == self.den:
            return "1"

        else:
            return "Fraction(" + str(self.num)+", "+str(self.den) + ")"

    def getNum(self):

        return self.num

    def getDen(self):

        return self.den

    def __add__(self, other):
        if type(other) is Fraction:
            newnum = self.num * other.den + self.den * other.num
            newden = self.den * other.den

            return Fraction(newnum, newden)

        elif type(other) == int:
            newnum = self.num + self.den * other
            newden = self.den

            return Fraction(newnum, newden)

        elif type(other) == float:
            result = self.num/self.den + other

            return result

        else:
            raise TypeError("Must be Fraction, int or float")

    def __radd__(self, other):
        if type(other) is Fraction:
            newnum = self.num * other.den + self.den * other.num
            newden = self.den * other.den

            return Fraction(newnum, newden)

        elif type(other) == int:
            newnum = self.num + self.den * other
            newden = self.den

            return Fraction(newnum, newden)

        elif type(other) == float:
            result = other + self.num/self.den

            return result

        else:
            raise TypeError("Must be Fraction, int or float")

    def __sub__(self, other):
        if type(other) is Fraction:
            newnum = self.num * other.den - self.den * other.num
            newden = self.den * other.den

            return Fraction(newnum, newden)

        elif type(other) == int:
            newnum = self.num - self.den * other
            newden = self.den

            return Fraction(newnum, newden)

        elif type(other) == float:
            result = self.num/self.den - other

            return result

        else:
            raise TypeError("Must be Fraction, int or float")

    def __rsub__(self, other):
        if type(other) is Fraction:
            newnum = self.num * other.den - self.den * other.num
            newden = self.den * other.den

            return Fraction(newnum, newden)

        elif type(other) == int:
            newnum = self.den * other - self.num
            newden = self.den

            return Fraction(newnum, newden)

        elif type(other) == float:
            result = other - self.num/self.den

            return result

        else:
            raise TypeError("Must be Fraction, int or float")

    def __mul__(self, other):
        if type(other) is Fraction:
            newnum = self.num * other.num
            newden = self.den * other.den

            return Fraction(newnum, newden)

        elif type(other) is int:
            newnum = self.num * other
            newden = self.den

            return Fraction(newnum, newden)

        elif type(other) == float:
            result = self.num * other / self.den

            return result

        else:
            raise TypeError("Must be Fraction, int or float")

    def __rmul__(self, other):
        if type(other) is Fraction:
            newnum = self.num * other.num
            newden = self.den * other.den

            return Fraction(newnum, newden)

        elif type(other) is int:
            newnum = self.num * other
            newden = self.den

            return Fraction(newnum, newden)

        elif type(other) == float:
            result = self.num * other / self.den

            return result

        else:
            raise TypeError("Must be Fraction, int or float")

    def __truediv__(self, other):
        if type(other) is Fraction:
            newnum = self.num * other.den
            newden = self.den * other.num

            return Fraction(newnum, newden)

        elif type(other) is int:
            newnum = self.num
            newden = self.den * other

            return Fraction(newnum, newden)

        elif type(other) == float:
            result = self.num / (self.den * other)

            return result

        else:
            raise TypeError("Must be Fraction, int or float")

    def __rtruediv__(self, other):
        if type(other) is Fraction:
            newnum = self.num * other.den
            newden = self.den * other.num

            return Fraction(newnum, newden)

        elif type(other) is int:
            newnum = other * self.den
            newden = self.num

            return Fraction(newnum, newden)

        elif type(other) == float:
            result = other * self.den / self.num

            return result

        else:
            raise TypeError("Must be Fraction, int or float")

    def __eq__(self, other):
        firnum = self.num * other.den
        secnum = other.num * self.den

        return firnum == secnum

    def __ne__(self, other):
        firnum = self.num * other.den
        secnum = other.num * self.den

        return firnum != secnum

    def __gt__(self, other):
        firnum = self.num * other.den
        secnum = other.num * self.den

        return firnum > secnum

    def __ge__(self, other):
        firnum = self.num * other.den
        secnum = other.num * self.den

        return firnum >= secnum

    def __lt__(self, other):
        firnum = self.num * other.den
        secnum = other.num * self.den

        return firnum < secnum

    def __le__(self, other):
        firnum = self.num * other.den
        secnum = other.num * self.den

        return firnum <= secnum

    def gcd(self, m, n):
        """find the greatest common number between m and n."""
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm % oldn
        return n


def test():
    """test all methods in Fraction class."""

    f1 = Fraction(2,8)
    f2 = Fraction(1,2)
    f3 = Fraction(2, -9)
    f4 = Fraction(4,4)
    i  = 5
    f  = 5.0

    print("f1: ".rjust(15), f1)
    print("f2: ".rjust(15), f2)
    print("f3: ".rjust(15), f3)
    print("f4: ".rjust(15), f4)
    print("i: ".rjust(15), i)
    print("f: ".rjust(15), f)
    print("repr(f1): ".rjust(15), repr(f1))
    print("str(f1): ".rjust(15), str(f1))
    print("repr(f4): ".rjust(15), repr(f4))
    print("str(f4): ".rjust(15), str(f4))
    print()

    print("f1+f2: ".rjust(15), f1+f2)
    print("f1+f3: ".rjust(15), f1+f3)
    print("f1-f2: ".rjust(15), f1-f2)
    print("f1-f3: ".rjust(15), f1-f3)
    print("f1*f2: ".rjust(15), f1*f2)
    print('---------------------------------')
    print("f1*i: ".rjust(15), f1*i)
    print("f1*f: ".rjust(15), f1*f)
    print("i*f1: ".rjust(15), i*f1)
    print("f*f1: ".rjust(15), f*f1)
    print("f1*f3: ".rjust(15), f1*f3)
    print("f1/f2: ".rjust(15), f1/f2)
    print("f1/f3: ".rjust(15), f1/f3)
    print("f1/i: ".rjust(15), f1/i)
    print("f1/f: ".rjust(15), f1/f)
    print("i/f1: ".rjust(15), i/f1)
    print("f/f1: ".rjust(15), f/f1)
    print('---------------------------------')
    print("f1==f2: ".rjust(15), f1==f2)
    print("f1!=f2: ".rjust(15), f1!=f2)
    print("f1>f2: ".rjust(15), f1>f2)
    print("f1<f2: ".rjust(15), f1<f2)
    print("f1>=f2: ".rjust(15), f1>=f2)
    print("f1<=f2: ".rjust(15), f1<=f2)
    print("f1 + 10: ".rjust(15), f1+10)
    print("f1 + 10.1: ".rjust(15), f1+10.1)
    print("10 + f1: ".rjust(15), 10+f1)
    print("10.1 + f1: ".rjust(15), 10.1+f1)
    print("f1 - 10: ".rjust(15), f1-10)
    print("f1 - 10.1: ".rjust(15), f1-10.1)
    print("10 - f1: ".rjust(15), 10-f1)
    print("10.1 - f1: ".rjust(15), 10.1-f1)

    f1 += 1
    print("after f1 += 1: ".rjust(15), f1)

test()