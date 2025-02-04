from Elliptic_curve_mod_object import *

my_curve = Curve(1, 5, 10000)

def order_sup(p: Point, min: int, c: Curve):
    """
    return if the order of p is higher than min
    :param p:
    :param min:
    :return:
    """
    it = p
    i = 0
    while i < min and not(p.is_inf):
        it = c.add(it, p)
    return p.is_inf

p = my_curve.get_a_point(0)
p.print_point()


