from Point import Point


class Curve:
    def __init__(self, a, b):
        """
        The equation of the curve is y^2 = x^3 + a*x + b
        :param a:
        :param b:
        """
        self.a = a
        self.b = b


    def belongs_to_curve(self, p):
        """

        :param p: a point
        :return: if p is a point of the curve
        """
        return p.y ** 2 == p.x ** 3 + self.a ** p.x + self.b

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
            m = (p2.y - p1.y) / (p2.x - p1.x)
            x = m ** 2 - p1.x - p2.x
            y = m * (p1.x - x) - p1.y
            return Point(False, x, y)
        elif p1.x == p2.x and p1.y != p2.y:
            return Point(True)
        elif (p1.x, p1.y) == (p2.x, p2.y) and p1.y != 0:
            m = (3 * (p1.x ** 2) + self.a) / (2 * p1.y)
            x = m ** 2 - 2 * p1.x
            y = m * (p1.x - x) - p1.y
            return Point(False, x, y)
        else:
            return Point(True)

    def multi(self, n: int, p: Point):
        """
        n is suppose to not be equal to 0
        :param n:
        :param p:
        :return:
        """
        res = p
        for i in range(n):
            res = self.add(res, p)
        return res

    def multi_fast(self, n: int, p: Point):
        """
        n is suppose to not be equal to 0
        :param n:
        :param p:
        :return:
        """
        res = p
        while n != 0:
            if n % 2 == 1:
                res = self.add(res, p)
                n -= 1
            else:
                res = self.add(res, res)
                n = n / 2
        return res

