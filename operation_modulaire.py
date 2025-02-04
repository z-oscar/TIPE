def modular_division(a: int, b: int, q: int):
    """
    :param a:
    :param b:
    :param q:
    :return: a / b mod p
    """
    a = a % q
    b = b % q
    acc = b
    res = 1
    while a != acc:
        acc = (acc + b) % q
        res += 1
    return res


def generate(x, q):
    tab = []
    res = x
    for i in range(q-1):
        res = (res + x) % q
        tab.append(res)
    return tab


