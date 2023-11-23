import numpy as np
#pablo
def generate_polynomial():
    # Generate a random power for the polynomial
    power = np.random.randint(3, 6)  # You can adjust the range of powers as needed

    # Generate random integer roots for the polynomial
    roots = np.random.randint(-10, 11, power)

    # Build the polynomial using numpy's poly function
    polynomial_coefficients_float = np.poly(roots)

    # Convert coefficients to integers
    polynomial_coefficients_int = np.round(polynomial_coefficients_float).astype(int)

    # Create a polynomial object
    poly = np.poly1d(polynomial_coefficients_int)

    # Get powers and coefficients as lists
    powers, coefficients = get_powers_and_coefficients(poly)

    # Write data into a dictionary
    data = {}
    for power, coeff in zip(powers, coefficients):
        data[power]=coeff

    return data

def get_powers_and_coefficients(poly):
    powers = list(range(len(poly)+1))  # List of powers
    coefficients = poly.coeffs  # Coefficients

    return powers[::-1], coefficients

# Exectute only if this file is not a dependencie
if __name__ == "__main__":
    print(generate_polynomial())