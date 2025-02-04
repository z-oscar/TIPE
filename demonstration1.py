from Elliptic_curve_mod_object import *

infinity_point = Point(True) # Point à l'infini

my_point = Point(False, 5, 2) # Point de coordonnées (5, 2)

"""Courbe d'équation y^2 = x^3 - x + 3 mod 127"""
my_curve = Curve(-1, 3, 127)
p1 = Point(False, 2, 124)
print(my_curve.belongs_to_curve(p1))




