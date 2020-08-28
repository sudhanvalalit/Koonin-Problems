"""
 Exercise 1.4: Run the code above for various tolerances, initial guesses, and initial step sizes. Note that sometimes you might find convergence to the negative root. What happens if you start with an initial guess of -3 with a step size of 6?

 Code: chap1c.for
"""

import math

tolx = 1.0e-6


def func(x):
    return x * x - 5.0


def main():
    x0 = float(input("Input value of initial guess: \n"))
    dx = float(input("Input value of step size: \n"))
    print(x0, dx)
    fold = func(x0)
    iter = 0
    while abs(dx) > tolx:
        iter += 1
        x0 += dx
        error = math.sqrt(5.0) - x0
        print("{:.5E} {:.5E} {:.5E}".format(iter, x0, error))
        if fold * func(x0) < 0.0:
            x0 -= dx
            dx = dx / 2


if __name__ == "__main__":
    main()
