import time
import matplotlib.pyplot as plt


def puissance_rec(x, n):
    """

    :param x: nombre à mettre à la puissance n
    :param n: puissance
    :return: x^n
    """
    if n == 1:
        return x
    if n % 2 == 0:
        return puissance(x**2, n / 2)
    return x * puissance(x ** 2, (n - 1) / 2)


def modular_power(x, n, q):
    """
    :param x: nombre à mettre à la puissance n modulo q
    :param n: puissance
    :param q: modulo
    :return: x^n mod q
    """
    e = 0
    res = 1
    while e != n:
        res = (res * x) % q
        e += 1
    return res

def puissance(x, n):
    """
    calcule x^n de facons naive récursivement
    -> ne marche pas pour grand n : maximum depth recursion
    :param x: nombre à mettre à la puissance n
    :param n: puissance
    :return: x^n
    """
    if n == 1:
        return x
    return x * puissance(x, n - 1)

def test1(x,n):
    """

    :param x: nombre à mettre à la puissance n
    :param n: puissance
    :return:
    """
    tab = []
    t = time.time()
    for i in range(n):
        res = puissance_rec(x,i)

    print(time.time() - t)
    return tab

def test_modulaire(x,d,f,q):
    """
    ici on utilise puissance_modulaire
    :param x: nombre dont on calcule les puissances de d à f
    :param d: première puissance à calculer
    :param f: dernière puissance à calculer
    :param q: molulo
    :return: tableau des puissances de x de d à f
    """
    tab = []
    t = time.time()
    for i in range(d,f,50):
        res = modular_power(x, i, q)
        tab.append(time.time() - t)
    return tab

def test_classique(x,d,f,q):
    """
        Ici on utilise le systeme de puissance modulaire de python
        :param x: nombre dont on calcule les puissances de d à f
        :param d: première puissance à calculer
        :param f: dernière puissance à calculer
        :param q: molulo
        :return: tableau des puissances de x de d à f
        """
    tab = []
    t = time.time()
    for i in range(d,f,50):
        res = (x**i)%q
        tab.append(time.time() - t)
    return tab

def main1():
    plt.xlabel("Distance")
    plt.ylabel("Density")
    tabx = [1,2,3]
    taby = [12,13,14]
    tabx2 = [1, 2, 3]
    taby2 = [20, 21, 22]
    p1, = plt.plot(tabx, taby,'o',label = "tet1",color = "black")
    p2, = plt.plot(tabx2, taby2, 'o',label = "test2", color = 'red')

    plt.legend()


    plt.title("ceci est un test")
    plt.show()

def main_test(x,d,f,q):
    plt.xlabel("Puissance")
    plt.ylabel("Temps (en s)")
    tabx = [i for i in range(d,f,50)]
    taby_modulaire = test_modulaire(x,d,f,q)
    taby_classique = test_classique(x,d,f,q,)
    p1, = plt.plot(tabx,taby_modulaire,label = "Modulaire",color = "black")
    p2, = plt.plot(tabx,taby_classique,label = "Classique",color = "red")
    plt.legend()
    plt.title("Comparaison des algorithmes d'exponentiation, des puissances de x = 50000 modulo q = 13")
    plt.show()

