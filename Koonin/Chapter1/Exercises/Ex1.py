r"""
Exercise 1.1: Using any function for which you can evaluate the
derivatives analytically, investigate the accuracy of the formulas in Table 1.2 for various values of h

Let us consider the function sin(x)
"""
import math
import numpy as np


def f(x):
    return math.sin(x)


def deriv(x):
    return "{:.5E} {:.5E} {:.5E}".format(math.cos(x), -math.sin(x), -math.cos(x))


def FourPoint(f, x, h):
    dfdx = (-2.0 * f(x - h) - 3.0 * f(x) + 6.0 *
            f(x + h) - f(x + 2.0 * h)) / (6.0 * h)
    d2fdx2 = (f(x - h) - 2.0 * f(x) + f(x + h)) / h ** 2
    d3fdx3 = (-f(x - h) + 3.0 * f(x) - 3.0 *
              f(x + h) + f(x + 2.0 * h)) / h ** 3
    return np.array([dfdx, d2fdx2, d3fdx3])


def FivePoint(f, x, h):
    dfdx = (f(x - 2.0 * h) - 8.0 * f(x - h) + 8.0 * f(x + h) - f(x + 2.0 * h)) / (
        12.0 * h
    )
    d2fdx2 = (
        -f(x - 2.0 * h)
        + 16.0 * f(x - h)
        - 30.0 * f(x)
        + 16.0 * f(x + h)
        - f(x + 2.0 * h)
    ) / (12.0 * h ** 2)
    d3fdx3 = (-f(x - 2.0 * h) + 2.0 * f(x - h) - 2.0 * f(x + h) + f(x + 2.0 * h)) / (
        2.0 * h ** 3
    )
    return np.array([dfdx, d2fdx2, d3fdx3])


def main():
    x = math.pi / 6.0
    title = "{:12} {:12} {:12} {:12}".format(
        " ", "First ", "Second ", "Third ")
    for i in range(5):
        h = 0.1 ** i
        y = f"{h:.5E}"
        fourPointArray = FourPoint(f, x, h)
        fivePointArray = FivePoint(f, x, h)
        fourPointStr = ' '.join(f'{x:.5E}' for x in fourPointArray)
        fivePointStr = ' '.join(f'{x:.5E}' for x in fivePointArray)
        data = [y, fourPointStr, fivePointStr, deriv(x)]
        prefix = ["h        ", "Four Point", "Five Point", "Exact     "]
        print(title)
        for col, row in zip(prefix, data):
            print(col, row)


if __name__ == "__main__":
    main()
