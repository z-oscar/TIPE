from math import ceil, sqrt

from ..utils.expo import modular_power

def recherche(tab, x):
    """

    :param tab: tableau de tuple
    :param x: élément recherché en deuxième position d'un tuple
    :return: le premier élément du tuple dans lequel est x si il existe -1 sinon
    """
    for i in range(len(tab)):
        if tab[i][1] == x:
            return tab[i][0]
    return -1

def minus_mod(q,x,y):
    """Calcul x-y mod q donne la valeur entre 1 et q"""
    res = x-y
    while res<=0 :
        res += q
    return res

def baby(q, g, b):
    m = ceil(sqrt(q))
    tab = []
    for j in range(m):
        tab.append((j, modular_power(g, j, q)))
    inv = (g ** (q-m) )% q
    y = b
    for i in range(m):
        j = recherche(tab, y)
        if j != -1:
            return i*m + j
        else:
            y = y*inv

def baby2(q, g, b):
    """

    :param q: on travaille dans Z/qZ
    :param g: g est un générateur de Z/qZ
    :param b: g^x : inconnue
    :return: x tel que g^x = b mod q
    """
    N = ceil(sqrt(q))
    tab = []
    """Baby step"""
    for j in range(1,N+1):
        tab.append((j, modular_power(g, j, q)))

    y = b
    inv = g ** N
    """Giant step"""
    j = recherche(tab, y)
    count = 0
    #print(y)
    while j==-1 :
        y = (y * inv) %q
        j = recherche(tab, y)
        count +=1
        #print(y,j)

    for i in range(count):
        j = minus_mod((q-1),j,N)
    return j


def baby_step_giant_step(q, g, b):
    """
    :param q: on travaille dans Z/qZ
    :param g: g est un générateur de Z/qZ
    :param b: g^x : inconnu
    :return: x tel que g^x = b mod q
    """
    m = int(ceil(sqrt(q)))
    tab = []
    """Baby step"""
    for j in range(1, m+1):
        tab.append((j, modular_power(g, j, q)))

    y = b
    inv = modular_power(g, (q - m - 1), q)
    """Giant step"""
    for i in range(m+1):
        j = recherche(tab, y)
        if j == -1:
            y = y * inv % q
        else:
            return i*m + j



