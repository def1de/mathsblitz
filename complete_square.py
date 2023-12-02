import math
import random
import numpy as np


#uses roots to make the quadratic
def create_new_quadratic(roots):
    polynomial_coefficients_float = np.poly(roots)
    polynomial_coefficients_int = np.round(polynomial_coefficients_float).astype(int)
    #polynomial_coefficients_int*=np.random.randint(1,4)
    poly = np.poly1d(polynomial_coefficients_int)
    return poly

#creates quadratic equations with a vertex equal to coefficient
def creating_vertex_equation(coefficients):
    #for i in coefficients:
    if random.randint(0,2):
        coefficients*=-1
        x_vertex = random.randint(-11,11)
        roots = [x_vertex+np.emath.sqrt(coefficients),x_vertex-np.emath.sqrt(coefficients)]
        
        return("find the y coordinate of the turning point of the graph:",str(create_new_quadratic(roots)))
    else:
        y_vertex = (random.randint(0,8))**2
        roots = [coefficients+np.emath.sqrt(y_vertex),coefficients-np.emath.sqrt(y_vertex)]
        return("find the x coordinate of the turning point of the graph:",str(create_new_quadratic(roots)))



'''
def finding_vertex(coefficients):
    a,b,c = coefficients[0],coefficients[1],coefficients[2]
    y = -(b**2/4*a)+c
    x = -(b/2*a)
    return x,y
'''