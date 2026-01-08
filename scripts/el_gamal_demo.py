"""Run a basic ElGamal (integer) encryption/decryption demonstration."""

from src.models.el_gamal import creation_cles, chiffrement_message, dechiffrement_message


def run_demo():
    msg = "Hello world!"
    private_key, public_key = creation_cles(101, 3, 5)
    msg_crypte = chiffrement_message(public_key, msg)
    msg_decrypte = dechiffrement_message(private_key, public_key, msg_crypte)

    print(msg)
    print(msg_crypte)
    print(msg_decrypte)


if __name__ == "__main__":
    run_demo()
