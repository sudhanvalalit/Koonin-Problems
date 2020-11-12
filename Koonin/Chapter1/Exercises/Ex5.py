"""
Exercise 1.5: Write programs to solve for the positive root of x^2-5 using the Newton-Raphson
and secant methods. Investigate the behavior of the latter with changes in the initial guesses
for the root.

"""
import numpy as np
from scipy.misc import derivative

tolx = 1e-6


def f(x):
    return x**2 - 5.0


def Newton_Raphson(f, x):
    dx = 0.2
    fvalue = f(x)
    count = 0
    while abs(fvalue) > tolx:
        x += dx
        fprime = derivative(f, x, 1e-4)
        fvalue = f(x)
        dx = -fvalue/fprime
        count += 1
        if count > 1000:
            raise Exception("Exceeded the number of iterations.")
            break

    return x


def Secant(f, x):
    diff = 0.1
    df = 0.1
    while abs(diff) > tolx:
        x1 = x + df
        f1 = f(x)
        f2 = f(x1)
        dx = x1 - x
        df = f2 - f1
        df = -f(x1) * dx/df
        diff = f2 - f1
        x = x1
    return x


def main():
    result = Newton_Raphson(f, 4.0)
    print("Root using Newton Raphson method: {:.6F}".format(result))
    result1 = Secant(f, 4.0)
    print("Root using Secant method: {:.6F}".format(result1))

    # Investigate the behavior of latter method, i.e. secant method
    print("Iter \t Result \t Error")
    for i in range(10):
        result = Secant(f, i)
        diff = np.sqrt(5) - result
        print("{:2} \t {:.6f} \t {:.5E}".format(i, result, diff))


if __name__ == "__main__":
    main()
