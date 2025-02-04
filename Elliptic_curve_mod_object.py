from Point import Point
from calcul_on_Fq import modular_division, find_root
from expo import modular_power
import matplotlib.pyplot as plt


class Curve:
    def __init__(self, a: int, b: int, q: int):
        """
        The equation of the curve is y^2 = x^3 + a*x + b mod q
        :param a:
        :param b:
        """
        self.a = a
        self.b = b
        self.q = q

    def __repr__(self):
        return "(Curve : y^2 = x^3 + " + str(self.a) + " * x + " + str(self.b) + " mod " + str(self.q) + ")"

    def __str__(self):
        return "(Curve : y^2 = x^3 + " + str(self.a) + " * x + " + str(self.b) + " mod " + str(self.q) + ")"

    def belongs_to_curve(self, p: Point):
        """

        :param p: a point
        :return: if p is a point of the curve
        """
        if p.is_inf:
            return True
        return (p.y ** 2) % self.q == (p.x ** 3 + self.a * p.x + self.b) % self.q

    def generate_points(self):
        """
        This function generates all the point of the elliptic curve y^2 = x^3 + a*x + b mod p
        """
        points = []
        power = int((self.q - 1) / 2)
        for i in range(self.q):
            z = ((i ** 3) + self.a * i + self.b) % self.q
            if modular_power(z, power, self.q) == 1:
                root = find_root(z, self.q)
                points.append((i, root))
                points.append((i, self.q - root))
        return points

    def generate_points_object(self):
        """
        This function generates all the point of the elliptic curve y^2 = x^3 + a*x + b mod p
        """
        points = []
        power = int((self.q - 1) / 2)
        for i in range(self.q):
            z = ((i ** 3) + self.a * i + self.b) % self.q
            if modular_power(z, power, self.q) == 1:
                root = find_root(z, self.q)
                points.append(Point(False, i, root))
                points.append(Point(False, i, self.q - root))
        return points

    def get_a_point(self, n: int):
        """
        :return
        :param n:
        :return:
        """
        power = int((self.q - 1) / 2)
        for i in range(n,self.q):
            z = ((i ** 3) + self.a * i + self.b) % self.q
            if modular_power(z, power, self.q) == 1:
                root = find_root(z, self.q)
                return Point(False, i, root)
        return Point(True)

    def add(self, p1: Point, p2: Point):
        """

        :param p1: A point on the curve
        :param p2: An other point on the curve
        :return: p = p1 + p2
        """
        if p1.is_inf:
            return p2
        elif p2.is_inf:
            return p1
        elif p1.x != p2.x:
            m = modular_division((p2.y - p1.y), (p2.x - p1.x), self.q)
            x3 = (m ** 2 - p1.x - p2.x) % self.q
            y3 = (m * (p1.x - x3) - p1.y) % self.q
            return Point(False, x3, y3)
        elif p1.x == p2.x and p1.y != p2.y:
            return Point(True)
        elif (p1.x, p1.y) == (p2.x, p2.y) and p1.y != 0:
            m = modular_division((3 * (p1.x ** 2) + self.a), (2 * p1.y), self.q)
            x3 = (m ** 2 - 2 * p1.x) % self.q
            y3 = (m * (p1.x - x3) - p1.y) % self.q
            return Point(False, x3, y3)
        else:
            return Point(True)

    def multi(self, n: int, p: Point):
        """
        :param n: integer assumed to be positive
        :param p: a point
        :return: n * p
        """
        res = Point(True)
        for i in range(n):
            res = self.add(res, p)
        return res

    def multi_fast(self, n: int, p: Point):
        """

        :param n: integer assumed to be positive
        :param p: a point
        :return: n * p
        """
        if n == 0:
            return Point(True)
        res = p
        acc = Point(True)
        while n > 1:
            if n % 2 == 1:
                acc = self.add(acc, res)
                n = n - 1
            else:
                res = self.add(res, res)
                n = int(n / 2)
        return self.add(res, acc)

    def get_order(self, p: Point):
        n = 0
        save = p
        while not p.is_inf:
            p = self.add(p, save)
            n += 1
        return n

    def show(self):
        tab = self.generate_points()
        tabx = [i[0] for i in tab]
        taby = [i[1] for i in tab]
        plt.scatter(tabx, taby)
        plt.show()

    def show_addition(self, p1: Point, p2: Point):
        tab = self.generate_points()
        tabx = [i[0] for i in tab]
        taby = [i[1] for i in tab]
        plt.scatter(tabx, taby, c='blue',)

        p3 = self.add(p1, p2)

        delta = (p1.y - p2.y) / (p1.x - p2.x)
        b = p1.y - (delta * p1.x)
        plt.plot([-b/delta, (103-b)/delta], [0, 103], 'red')
        plt.scatter([p1.x, p2.x], [p1.y, p2.y], c='black')
        plt.scatter([p3.x], [p3.y], c='orange')
        plt.show()


