import random
import numpy as np

def create_new_quadratic(roots):
    polynomial_coefficients_float = np.poly(roots)
    polynomial_coefficients_int = np.round(polynomial_coefficients_float).astype(int)
    poly = np.poly1d(polynomial_coefficients_int)
    return poly

def creating_vertex_equation(coefficients):
    if random.randint(0, 2):
        coefficients *= -1
        x_vertex = random.randint(-11, 11)
        roots = [x_vertex + np.emath.sqrt(coefficients), x_vertex - np.emath.sqrt(coefficients)]
        return f"find the y coordinate of the turning point of the graph: {str(create_new_quadratic(roots))}"
    else:
        y_vertex = random.randint(0, 8) ** 2
        roots = [coefficients + np.emath.sqrt(y_vertex), coefficients - np.emath.sqrt(y_vertex)]
        return f"find the x coordinate of the turning point of the graph: {str(create_new_quadratic(roots))}"
