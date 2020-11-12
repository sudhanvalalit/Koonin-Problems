"""
The following FORTRAN program finds the positive root of the function 

..math::
    f(x) = x^2 - 5, x_0 = 5^{1/2} = 2.236068
    
to a tolerance of 10^{-6} using x = 1 as an initial guess and an initial step size of 0.5:
"""

import numpy as np

# tolerance
tolx = 1e-6


def func(x):
    return x*x - 5.0


def main():
    x = 1.0
    fold = func(x)
    dx = 0.5
    it = 0
    while abs(dx) > tolx:
        it += 1
        x += dx
        diff = np.sqrt(5.0) - x
        print("Iteration: {}, x: {:.7f}, Error: {:.5E}".format(
            it, x, diff))
        if fold*func(x) < 0:
            x -= dx
            dx /= 2


if __name__ == "__main__":
    main()
