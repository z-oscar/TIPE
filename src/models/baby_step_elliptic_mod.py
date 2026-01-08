from math import sqrt

from .elliptic_curve_mod import Curve
from .point import Point
from .transfert_message_elgamal import receive_msg


def search2(p: Point, tab):
    for i in range(len(tab)):
        if (p.x == tab[i].x and p.y == tab[i].y) or (p.is_inf and tab[i].is_inf):
            return i
    return -1


def search(p: Point, d):
    try:
        return d[p]
    except KeyError:
        return -1


def baby_step_giant_step(c: Curve, g: Point, n: int, p: Point):
    """
    :param p:
    :param c:
    :param g:
    :param n: g is of order n
    :return: k such as kg = p
    """
    m = round(sqrt(n)) + 1
    d = {}
    new_p = Point(True)
    for j in range(m):
        d[new_p] = j
        new_p = c.add(new_p, g)
    inv = (c.multi(m, g)).inv()
    y = p

    for i in range(m + 1):
        j = search(y, d)
        if j == -1:
            y = c.add(y, inv)
        else:
            return i * m + j


def attack(public_key, coded_msg):
    c, g, n, p = public_key
    q = baby_step_giant_step(c, g, n, p)
    return receive_msg(public_key, q, coded_msg)

