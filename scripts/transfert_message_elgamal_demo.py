"""Demo for sending a message with elliptic-curve ElGamal."""

from src.models.el_gamal_elliptic import create_keys
from src.models.elliptic_curve_mod import Curve
from src.models.transfert_message_elgamal import receive_msg, send_msg


def run_demo():
    my_curve = Curve(-1, 3, 7919)
    lst = my_curve.generate_points_object()
    p = lst[2]
    order = my_curve.get_order(p)

    private_key, public_key = create_keys(-1, 3, 7919, p, order, 500)

    msg = "hello"
    encrypted_msg = send_msg(public_key, msg)
    decrypted_msg = receive_msg(public_key, private_key, encrypted_msg)

    print("le message était: ", msg)
    print("le message recu est :", decrypted_msg)


if __name__ == "__main__":
    run_demo()
