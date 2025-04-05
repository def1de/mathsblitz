import random
import numpy as np
import math


def trig_integral(integral_value):
    list_of_integrals = []
    list_of_integrals.append(
        f"\\(\\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} {integral_value}sin(x) \\,dx\\)"
    )
    list_of_integrals.append(
        f"\\(\\int_{{0}}^{{\\frac{{\\pi}}{{2}}}} {integral_value}cos(x) \\,dx\\)"
    )
    list_of_integrals.append(
        f"\\(\\int_{{0}}^{{\\pi}} {0.5*integral_value}sin(x) \\,dx\\)"
    )
    list_of_integrals.append(
        f"\\(\\int_{{\\frac{{\\pi}}{{2}}}}^{{2\\pi}} {-integral_value}sin(x) \\,dx\\)"
    )
    list_of_integrals.append(
        f"\\(\\int_{{\\frac{{\\pi}}{{2}}}}^{{\\pi}} {-integral_value}cos(x) \\,dx\\)"
    )
    list_of_integrals.append(
        f"\\(\\int_{{\\frac{{\\pi}}{{2}}}}^{{\\frac{{3\\pi}}{{2}}}} {-0.5*integral_value}cos(x) \\,dx\\)"
    )
    selected_integral = random.choice(list_of_integrals)

    return selected_integral
    # return f"\\(\\int_{{'{0}'}}^{{'hello'}} \\{integral_value}sin(x) \\,dx\\)"


def create_easy_linear_integral(value):
    random_num = random.randint(1, 3)
    if random_num == 1:
        if value >= 0:
            integral_value = 0
            while integral_value == 0:
                integral_value = random.randint(
                    -value // 2, value // 2
                ) * random.randint(-3, 3)
        if value < 0:
            integral_value = 0
            while integral_value == 0:
                integral_value = random.randint(
                    value // 2, -value // 2
                ) * random.randint(-3, 3)
        trig_value = trig_integral(integral_value)
        print("trig_value", trig_value)
        value -= integral_value

    a = 0
    b = None
    print("not found")
    found = False
    while found == False:
        m = random.randint(-5, 5) * 2
        while m == 0:
            m = random.randint(-5, 5) * 2
        c = random.randint(-5, 5)
        discriminant = c**2 - 4 * ((m / 2) * (-value))
        if discriminant > 0:
            roots = [
                ((-c + math.sqrt(discriminant)) / (m)),
                (-c - math.sqrt(discriminant)) / (m),
            ]
            for root in roots:
                if root.is_integer():
                    b = int(root)
                    found = True
                    print("found")

        elif discriminant == 0:
            root = (-c + math.sqrt(discriminant)) / (m)
            if root.is_integer():
                b = int(root)
                found = True
                print("found")
        if b == 0:
            found = False
    if b < 0:
        a = b
        b = 0
        m = -m
        c = -c
    if c > 0:
        c = "+" + str(c)
    elif c == 0:
        c = ""
    print(a, b)
    print(m, "x", "+", c)
    # integral = f"\[ \int_{a}^{b} {m}x + {c} \,dx \]"
    integral = f"\\(\\int_{{{a}}}^{{{b}}} {m}x {c} \\,dx\\)"
    if random_num == 1:
        return f"find the integral of:" + "<br>" + f"{integral} \\(+\\) {trig_value}"
    else:
        return f"find the integral of:" + "<br>" + f"{integral}"


def create_hard_linear_integral(value):

    random_num = random.randint(1, 4)
    if random_num == 1 or random_num == 2:
        if value >= 0:
            integral_value = 0
            while integral_value == 0:
                integral_value = random.randint(
                    -value // 2, value // 2
                ) * random.randint(-3, 3)
        if value < 0:
            integral_value = 0
            while integral_value == 0:
                integral_value = random.randint(
                    value // 2, -value // 2
                ) * random.randint(-3, 3)
        trig_value = trig_integral(integral_value)
        print("trig_value", trig_value)
        value -= integral_value
    # Generating random linear equation
    # Check if coefficients are not 0
    found = False
    while found == False:
        m = random.randint(-5, 5) * 2
        while m == 0:
            m = random.randint(-5, 5) * 2
        print("not found")
        b = random.randint(-2, 2)
        c = random.randint(-5, 5)
        discriminant = c**2 - 4 * ((m / 2) * (value - (b * c) - (m * 0.5 * b**2)))
        if discriminant > 0:
            roots = [
                ((-c + math.sqrt(discriminant)) / (m)),
                (-c - math.sqrt(discriminant)) / (m),
            ]
            for root in roots:
                if root.is_integer() and root < b:
                    a = int(root)
                    found = True
                    print("found")

        elif discriminant == 0:
            root = (-c + math.sqrt(discriminant)) / (m)
            if root.is_integer() and root < b:
                a = int(root)
                found = True
                print("found")

    print(a, b)

    if c > 0:
        c = "+" + str(c)
    elif c == 0:
        c = ""
    integral = f"\\(\\int_{{{a}}}^{{{b}}} {m}x {c} \\,dx\\)"
    if random_num == 1 or random_num == 2:
        return f"find the integral of:" + "<br>" + f"{integral} \\(+\\) {trig_value}"
    else:
        return f"find the integral of:" + "<br>" + f"{integral}"
