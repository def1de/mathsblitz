import numpy as np

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
    powers = list(range(power, -1, -1))  # List of powers in descending order
    coefficients = poly.coeffs.tolist()  # Coefficients as a list

    # Write data into a dictionary
    data = dict(zip(powers, coefficients))

    return data

# Execute only if this file is not a dependency
if __name__ == "__main__":
    print(generate_polynomial())
