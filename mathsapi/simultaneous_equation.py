import random


def simultaneous_equation(value):
    x = value
    y = random.randint(1, 10)
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    answer1 = x + y
    answer2 = a * x + b * y

    equation1 = f"X + Y = {answer1}"
    equation2 = f"{a}X + {b}Y = {answer2}"

    return f"Find X:\n{equation1}\n{equation2}"
