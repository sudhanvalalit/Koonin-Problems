"""
Exercise 1.1: Using any function for which you can evaluate the
derivatives analytically, investigate the accuracy of the formulas in Table 1.2 for various values of h

Let us consider the function sin(x)
"""
import math


def f(x):
    return math.sin(x)


def deriv(x):
    return "{:.5E} {:.5E} {:.5E}".format(math.cos(x), -math.sin(x), math.cos(x))


def FourPoint(x, h):
    dfdx = (-2.0 * f(x - h) - 3.0 * f(x) + 6.0 * f(x + h) - f(x + 2.0 * h)) / (6.0 * h)
    d2fdx2 = (f(x - h) - 2.0 * f(x) + f(x + h)) / h ** 2
    d3fdx3 = (-f(x - h) + 3.0 * f(x) - 3.0 * f(x + h) + f(x + 2.0 * h)) / h ** 3
    return "{:.5E} {:.5E} {:.5E}".format(dfdx, d2fdx2, d3fdx3)


def FivePoint(x, h):
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
    return "{:.5E} {:.5E} {:.5E}".format(dfdx, d2fdx2, d3fdx3)


def main():
    x = math.pi / 6.0
    title = "{:12} {:12} {:12} {:12}".format(" ", "First ", "Second ", "Third ")
    for i in range(5):
        h = 0.1 ** i
        y = "{:.5E}".format(h)
        data = [y, FourPoint(x, h), FivePoint(x, h), deriv(x)]
        prefix = ["h        ", "Four Point", "Five Point", "Exact     "]
        print(title)
        for col, row in zip(prefix, data):
            print(col, row)


if __name__ == "__main__":
    main()
