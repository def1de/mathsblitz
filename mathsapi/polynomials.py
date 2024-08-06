import random
import numpy as np

def create_new_quadratic(roots):
    polynomial_coefficients_float = np.poly(roots)
    polynomial_coefficients_int = np.round(polynomial_coefficients_float).astype(int)

    #Creating string of polynomial
    str_poly = f"{polynomial_coefficients_int[0]}x^2"

    if polynomial_coefficients_int[1] < 0:
        str_poly += f"{polynomial_coefficients_int[1]}x"
    else:
        str_poly += f"+{polynomial_coefficients_int[1]}x"

    if polynomial_coefficients_int[2] < 0:
        str_poly += f"{polynomial_coefficients_int[2]}"
    else:
        str_poly += f"+{polynomial_coefficients_int[2]}"

    #Wrapping in LaTeX formula
    poly = f"\\(\\LARGE {str_poly}\\)"
    
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

def integral(limit1, limit2):
    #Generating random polynomial
    coefficients = [random.randint(-10, 10) for _ in range(3)]
    #Check if coefficients are not 0
    hasZero = True
    while hasZero:
        hasZero = False
        for i in range(3):
            if coefficients[i] == 0:
                hasZero = True
                coefficients[i] = random.randint(-10, 10)


    poly = np.poly1d(coefficients)

    #Integrating
    integral_poly = np.polyint(poly)

    #Evaluating integral at limits
    integral_value = np.polyval(integral_poly, limit2) - np.polyval(integral_poly, limit1)

    #Creating string of polynomial
    str_poly = f"{coefficients[0]}x^2"

    if coefficients[1] < 0:
        str_poly += f"{coefficients[1]}x"
    else:
        str_poly += f"+{coefficients[1]}x"

    if coefficients[2] < 0:
        str_poly += f"{coefficients[2]}"
    else:
        str_poly += f"+{coefficients[2]}"

    return str_poly, round(integral_value)