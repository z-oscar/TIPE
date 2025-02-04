from random import randint

def creation_cles(q,g,a):
    """
    :param q: un entier premier (dans la pratique tres grand)
    :param g: un entier générateur de Z/qZ donc tel que p^q = 1
    :param a: un entier compris entre 0 et ordre(g) = q
    :return: couple de clé publique et clé privée pour le crypto systeme El Gamal
    """
    h = g ** a
    public_key = (q, h, g)
    private_key = a
    return private_key, public_key


def chiffrement(public_key, msg):
    """
    :param public_key: clé publique de la personne à qui on veut envoyer un msg
    :param msg: message à chiffrer convertie en entier
    :return: le message crypté
    """
    q, h, g = public_key
    k = randint(0, q)
    p = (g ** k) % q
    s = (h ** k) % q
    return p, msg * s


def dechiffrement(private_key, public_key, msg_encrypte):
    """
    :param private_key: clé privé de la personne qui recois le message
    :param public_key: clé publique de la personne qui recois le message
    :param msg_encrypte: message recu crypté
    :return: retourne le message decrypté
    """
    q, h, g = public_key
    p, msg = msg_encrypte
    s = p ** private_key % q
    return int(msg/s)


def chiffrement_message(public_key, msg):
    res = []
    for lettre in msg :
        res.append(chiffrement(public_key, ord(lettre)))
    return res

def dechiffrement_message(private_key, public_key, msg_encrypte):
    res = ""
    for i in msg_encrypte :
        res = res + chr(dechiffrement(private_key, public_key, i))
    return res

"""
test 1

message = 123456789

private_key, public_key = creation_cles(101,3,5)
msg_encrypte = cryptage(public_key,message)
print(cryptage(public_key,message))
print(decryptage(private_key, public_key,msg_encrypte))
print("done")
"""

"""test 2"""

msg = "Hello world!"

private_key, public_key = creation_cles(101,3,5)
msg_crypte = chiffrement_message(public_key, msg)
msg_decrypte = dechiffrement_message(private_key, public_key, msg_crypte)

print(msg)
print(msg_crypte)
print(msg_decrypte)