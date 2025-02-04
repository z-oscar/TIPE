from El_Gamal_Elliptic import *

my_curve = Curve(-1, 3, 127)
tab = my_curve.generate_points_object()

p = tab[42]

o = my_curve.get_order(p)
print(o)

private_key, public_key = create_keys(-1, 3, 127, p, o, 3)

msg = my_curve.multi_fast(52, p)
coded_msg = encryption(public_key, msg)
decoded_msg = decryption(private_key, public_key, coded_msg)

print("le point était :")
msg.print_point()
print("\nle message décodé obtenu est :")
decoded_msg.print_point()