import numpy as np

def generate_polynomial():
    power = 2  
    roots = np.random.randint(-11, 11, power)

    polynomial_coefficients_float = np.poly(roots)
    polynomial_coefficients_int = np.round(polynomial_coefficients_float).astype(int)
    polynomial_coefficients_int *= np.random.randint(1, 4)
    
    poly = np.poly1d(polynomial_coefficients_int)

    return roots, polynomial_coefficients_int, poly