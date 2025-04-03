import numpy as np
import random


def findRandom(determinant):
    if determinant < 1:
        return random.randint((determinant // 2), 1)
    if determinant > 1:
        return random.randint(1, (determinant // 2))


def create_matrix_with_determinant(determinant):

    found = False
    while found == False:

        a = findRandom(determinant)
        e = findRandom(determinant)
        i = findRandom(determinant)
        f = findRandom(determinant)
        h = findRandom(determinant)
        section1 = (a * e * i) - (a * f * h)
        section2 = determinant - section1

        c = findRandom(determinant)
        d = findRandom(determinant)
        g = (-section2 + (c * d * h)) / (e * c)

        if int(g) == g:
            g = int(g)
            found = True
    print("not found")
    b = 0
    print("Matrix:", a, b, c, d, e, f, g, h, i)

    return f"Find the determinant of the matrix: \\(\\begin{{pmatrix}}{a} & {b} & {c} \\\\ {d} & {e} & {f} \\\\ {g} & {h} & {i}\\end{{pmatrix}}\\)"
