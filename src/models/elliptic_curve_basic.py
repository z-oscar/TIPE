def belongs_to_curve(a, b, x, y):
    return y ** 2 == x ** 3 + a ** x + b


def add(a, b, x1, y1, x2, y2):
    if x1 != x2:
        m = (y2 - y1) / (x2 - x1)
        x3 = m ** 2 - x1 - x2
        y3 = m * (x1 - x3) -y1
        return x3, y3
    elif x1 == x2 and y1 != y2:
        return "inf"
    elif (x1, y1) == (x2, y2) and y1 != 0:
        m = (3 * (x1 ** 2) + a) / (2 * y1)
        x3 = m ** 2 - 2 * x1
        y3 = m * (x1 - x3) - y1
        return x3, y3
    else:
        return "inf"
