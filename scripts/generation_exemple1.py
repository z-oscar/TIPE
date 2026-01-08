from src.utils.calcul_on_fq import extended_euclid_rec


def run_demo():
    for i in range(126):
        if (i**63) % 127 == 1:
            print(i)

    u, v = extended_euclid_rec(2, 63)
    print(u, v)


if __name__ == "__main__":
    run_demo()
