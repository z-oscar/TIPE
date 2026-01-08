"""Small sanity check for the basic elliptic curve helpers."""

from src.models.elliptic_curve_basic import add, belongs_to_curve


def run_demo():
    test1 = belongs_to_curve(0, 1, 2, 3)
    test2 = add(0, 1, 2, 3, 2, 3)
    print(test1)
    print(test2)


if __name__ == "__main__":
    run_demo()
