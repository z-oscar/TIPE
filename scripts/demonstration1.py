from src.models.elliptic_curve_mod import Curve
from src.models.point import Point


def run_demo():
    infinity_point = Point(True)  # Point à l'infini
    _ = infinity_point

    my_point = Point(False, 5, 2)  # Point de coordonnées (5, 2)
    _ = my_point

    """Courbe d'équation y^2 = x^3 - x + 3 mod 127"""
    my_curve = Curve(-1, 3, 127)
    p1 = Point(False, 2, 124)
    print(my_curve.belongs_to_curve(p1))


if __name__ == "__main__":
    run_demo()




