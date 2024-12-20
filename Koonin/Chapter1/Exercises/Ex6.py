r"""
Exercise 1.6: The function f(x) = tanh x has a root at x = 0. Write a program to show that
the Newton-Raphson method does not converge for an initial guess of x >~ 1. Can you understand
what's going wrong by considering a graph of tanh x? From the explicit form of (1.14) for
this problem, derive the critical value of the initial guess above which convergence will
not occur. Try to solve the problem using the secant method. What happens for various
initial guesses if you try to find the x = 0 root of tan x using either method? 
"""

import numpy as np
import matplotlib.pyplot as plt
from .Ex5 import Newton_Raphson, Secant


def f(x):
    return np.tanh(x)


def g(x):
    return np.tan(x)


def plot_function(f, limits):
    pass


def main():
    result = Newton_Raphson(f, 1.5)
    print(f"Root using Newton Raphson method (x > 1): {result:.6F}")
    result = Newton_Raphson(f, 0.2)
    print(f"Root using Newton Raphson method (x < 1): {result:.6F}")
    result1 = Secant(f, 0.50)
    print("Root using Secant method: {:.6F}".format(result1))

    # Investigate the behavior of latter method, i.e. secant method
    print("\t \t Iter \t Result \t Error")
    for i in range(10):
        if i % 2 == 0:
            result = Secant(g, i/10)
            diff = 0.0 - result
            print(f"Using Sec method: {i:2} \t {result:.6f} \t {diff:.5E}")
        else:
            result = Newton_Raphson(g, i/10)
            diff = 0.0 - result
            print(f"Using N-R method: {i:2} \t {result:.6f} \t {diff:.5E}")


if __name__ == "__main__":
    main()
