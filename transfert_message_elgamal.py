from El_Gamal_Elliptic import *
"""
my_curve = Curve(-1, 3, 7919)
lst = my_curve.generate_points_object()
n = len(lst)
print("les nombres de points est", n)
p = lst[2]
order = my_curve.get_order(p)
print("p est d'ordre : ", order)

private, public = create_keys(-1, 3, 7919, p, order, 500)
"""


def construct_dic_p_to_c(p: Point, c: Curve):
    """
    :param p: p is assumed to have an order greater than 256
    :param c: p is a point of c
    :return: dictionary point to character
    """
    dic = {}
    it = p
    for i in range(256):
        dic[it] = chr(i)
        it = c.add(it, p)
    return dic


def construct_dic_c_to_p(p: Point, c: Curve):
    """
    :param p: p is assumed to have an order greater than 256
    :param c: p is a point of c
    :return: dictionary character to point
    """
    dic = {}
    it = p
    for i in range(256):
        dic[chr(i)] = it
        it = c.add(it, p)
    return dic


def construct_list(p: Point, c: Curve): # ne sert à rien normalement
    lst = []
    it = p
    for i in range(256):
        lst.append(it)
        it = c.add(it, p)  #chaque charatère est representé par le ieme point de la courbe
    return lst


def point_to_character(p, point_list):# ne sert à rien normalement
    for i in range(256):
        q = point_list[i]
        if (p.is_inf and q.is_inf) or (p.x == q.x and p.y == q.y):
            return chr(i)


def send_msg(public_key, msg):
    l = []
    length = len(msg)
    point_dic = construct_dic_c_to_p(public_key[1], public_key[0])
    for i in range(length):
        # chaque charatere est representé par le ieme point de la courbe
        l.append(encryption(public_key, point_dic[msg[i]]))
    return l


def receive_msg(public_key, private_key, encrypted_msg):
    res = ""
    length = len(encrypted_msg)
    dic = construct_dic_p_to_c(public_key[1], public_key[0])
    for i in range(length):
        p = decryption(private_key, public_key, encrypted_msg[i])
        res = res + dic[p]
    return res



"""
msg = "hello"
encrypted_msg = send_msg(public, msg)
decrypted_msg = receive_msg(public, private, encrypted_msg)
print("le message était: ", msg)
print("le message recu est :", decrypted_msg)
"""