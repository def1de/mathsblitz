import random


def simultaneous_equation(value):
    x = value
    y = random.randint(1, 10)

    a = random.randint(1, 5)
    b = random.randint(1, 5)
    while a == b:
        b = random.randint(1, 5)

    answer1 = x + y
    answer2 = a * x + b * y

    equation1 = f"x + y = {answer1}"
    equation2 = f"{a}x + {b}y = {answer2}"
    combined_equations = (
        r"\begin{cases}" + f"{equation1}" + r"\\" + f"{equation2}" + r"\end{cases}"
    )

    return r"Find X:" + combined_equations
