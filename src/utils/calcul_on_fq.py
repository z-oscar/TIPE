from .expo import modular_power
from .operation_modulaire import modular_division
import matplotlib.pyplot as plt


def find_square(p: int):
    """
    :param p: a primary integer, with q = 3 mod 4
    :return: tab array of integers that are square
    """
    power = int((p - 1) / 2)
    tab = []
    for i in range(p):
        if modular_power(i, power, p) == 1:
            tab.append(i)
    return tab


def extended_euclid_rec(a: int, b: int):
    """
    this function don't return pgcd(a,b) because we will us it only for a, b such as pgcd(a, b) = 1
    :param a: an integer
    :param b: an integer such as pgcd(a, b) = 1
    :return: (u, v) such as u*a + v*b = pgcd(a, b)
    """
    if b == 0:
        return (1, 0)
    else:
        u, v = extended_euclid_rec(b, a % b)
        return (v, u - (a // b) * v)


def find_root(x: int, p: int):
    """
    :param x: an integer : we suppose that x is a square
    :return: y such as y^2 = x
    """
    u, v = extended_euclid_rec(2, int((p - 1) / 2))
    if u < 0:
        u = p - 1 + u
    y = modular_power(x, u, p)
    return y


def generate_root(p: int):
    """

    :param p: a primary integer
    :return: return the couple (x,y) such as y^2 = x
    """
    tab = find_square(p)
    res = []
    for x in tab:
        root = find_root(x, p)
        res.append((x, root))
        res.append((x, -root))
    return res


def generate_curve(a: int, b: int, p: int):
    """
    This function generate all the point of the elliptic curve y^2 = x^3 + a*x + b mod p
    :param a:
    :param b:
    :param p:
    :return: an array of all then point of the elliptic curve
    """
    tab = []
    power = int((p - 1) / 2)
    for i in range(p):
        z = ((i ** 3) + a * i + b) % p
        if modular_power(z, power, p) == 1:
            root = find_root(z, p)
            tab.append((i, root))
            tab.append((i, p - root))
    return tab


def add_point_of_curve(a, q, x1, y1, x2, y2):
    """
    We can note that we do not need b to calculate the addition of two points
    :param a, q: We work on the elliptic curve y^2  = x^3 + a*x + b mod q
                ( We can note that we do not need b to calculate the addition of two points )
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return: return (x1, y1) + (x2, y2) = (x3, y3)
    """

    if x1 != x2:
        m = modular_division((y2 - y1), (x2 - x1), q)
        x3 = (m ** 2 - x1 - x2) % q
        y3 = (m * (x1 - x3) - y1) % q
        return x3, y3
    elif x1 == x2 and y1 != y2:
        return "inf"
    elif (x1, y1) == (x2, y2) and y1 != 0:
        m = modular_division((3 * (x1 ** 2) + a), (2 * y1), q)
        x3 = (m ** 2 - 2 * x1) % q
        y3 = (m * (x1 - x3) - y1) % q
        return x3, y3
    else:
        return "inf"




def mult_point_of_curve(a, q, x, y, n):
    xres = x
    yres = y
    for i in range(n):
        xres, yres = add_point_of_curve(a, q, xres, yres, x, y)
    return xres, yres


def verifie(tab):
    for i, j in tab:
        z = modular_power(j, 2, 103)
        z2 = (i ** 3 + -3 * i + 4) % 103
        if z != z2:
            print(i, j)


def show_curve(a, b, q):
    tab = generate_curve(a, b, q)
    print(tab)
    tabx = [i[0] for i in tab]
    taby = [i[1] for i in tab]
    plt.scatter(tabx, taby)
    plt.show()


def test2():
    tab = generate_curve(-3, 4, 103)
    print(tab)
    tabx = [i[0] for i in tab]
    taby = [i[1] for i in tab]
    plt.scatter(tabx, taby)
    plt.scatter([90, 98, 59], [3, 10, 37])
    plt.show()
    verifie(tab)

def test3():
    tab = generate_curve(-3, 4, 103)
    point = tab[0]
    tab2 = [point]
    for i in range(103):
        tab2.append(add_point_of_curve(-3, 103, tab2[i][0],tab2[i][1], point[0], point[1] ))
    print(tab)
    print(tab2)


