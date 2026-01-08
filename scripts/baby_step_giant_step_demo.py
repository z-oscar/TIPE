"""Demo for discrete log solving with baby-step giant-step."""

from src.models.baby_step_giant_step import baby2, baby_step_giant_step


def run_demo():
    print(baby2(599, 3, 400))
    print(baby_step_giant_step(599, 3, 400))


if __name__ == "__main__":
    run_demo()
