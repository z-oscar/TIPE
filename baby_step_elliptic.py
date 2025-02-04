from elleptic_curve_object import *
from math import *

def recherche(tab, p):
    """

    :param tab: tableau de tuple
    :param x: élément recherché en deuxième position d'un tuple
    :return: le premier élément du tuple dans lequel est x si il existe -1 sinon
    """
    for i in range(len(tab)):
        if tab[i][1].x == p.x and tab[i][1].y == p.y:
            return tab[i][0]
    return -1

def baby_step_giant_step(curve: Curve, g: Point, n: int, b: Point):
    """

        :param q: on travaille dans Z/qZ
        :param g: g est un générateur de Z/qZ
        :param b: g^x : inconnue
        :return: x tel que g^x = b mod q
        """
    m = int(ceil(sqrt(n)))
    tab = []
    """Baby step"""
    for j in range(1, m+1):
        tab.append((j, curve.multi(j, g)))

    y = b
    inv = curve.multi((n-m-1), g)
    inv.print_point()
    """Giant step"""
    for i in range(m+1):
        j = recherche(tab, y)
        if j == -1:
            y = curve.add(y, inv)
            y.print_point()
        else:
            return i*m + j

curve = Curve(0,1)
g = Point(False, 2,3)
test2 = curve.add()
test = baby_step_giant_step(curve, g, 6, Point(False,2,3))
print(test)
