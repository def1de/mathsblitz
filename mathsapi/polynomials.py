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

def integral(limit1, limit2):
    #Generating random polynomial
    coefficients = [random.randint(-10, 10) for _ in range(3)]
    poly = np.poly1d(coefficients)

    #Integrating
    integral_poly = np.polyint(poly)

    #Evaluating integral at limits
    integral_value = np.polyval(integral_poly, limit2) - np.polyval(integral_poly, limit1)

    #Creating string of polynomial
    str_poly = f"{coefficients[0]}x^2"
    power = 2
    for coeff in coefficients[1:]:
        power = power-1 if power != "" else ""
        power = power if int(power) > 0 else ""
        
        if coeff < 0:
            str_poly += f"{coeff}x^{power}"
        else:
            str_poly += f"+{coeff}x^{power}"

    return str_poly, round(integral_value)