import numpy as np

def generate_polynomial():
    power = 2  
    roots = np.random.randint(-11, 11, power)
    print("Current basic roots are:"+ str(list(roots)))

    polynomial_coefficients_float = np.poly(roots)
    polynomial_coefficients_int = np.round(polynomial_coefficients_float).astype(int)
    polynomial_coefficients_int *= np.random.randint(1, 4)
    print("Current basic coefficients are:"+str(list(polynomial_coefficients_int)))
    
    poly = np.poly1d(polynomial_coefficients_int)

    return list(roots), list(polynomial_coefficients_int)
