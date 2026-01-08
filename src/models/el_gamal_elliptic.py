from .elliptic_curve_mod import Curve
from .point import Point
from random import randint


def create_keys(a: int, b: int, p: int, g: Point, order: int, q: int):
    """

    :param a:
    :param b:
    :param p:
    :param g: generating point
    :param order: the order of the point g
    :param q: an integer such as 0 < n < order
    :return:
    """
    curve = Curve(a, b, p)
    h = curve.multi_fast(q, g)
    public_key = (curve, g, order, h)
    private_key = q
    return private_key, public_key


def encryption(public_key, msg: Point):
    """
    This function encrypt a msg with the public key of the person we want to send the message
    :param public_key: the public key contains: the curve on which we are working, a point p, the order of p,
    h another point
    :param msg: the message we want to send that has been converted in a point of the elliptic curve
    :return:
    """
    curve, p, order, h = public_key
    k = randint(0, order)
    c1 = curve.multi_fast(k, p)
    c2 = curve.add(msg, curve.multi_fast(k, h))
    return c1, c2


def decryption(private_key, public_key, msg_encrypted):
    curve, p, order, h = public_key
    c1, c2 = msg_encrypted
    return curve.add(c2, curve.multi_fast(private_key, c1).inv())

