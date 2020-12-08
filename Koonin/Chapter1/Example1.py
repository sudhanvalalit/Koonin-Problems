"""
Example 1: Bohr-Sommerfeld quantization for bound states of the Lennard-Jones Potential

Computational Physics (Python version)
"""
import numpy as np
import os
import sys

sys.path.append("../display/")
from utils import Display

etol = 1e-6
xtol = 1e-6


def archon():
    """
    Finds the bound states of the Lennard-Jones potential from the Bohr-Sommerfeld
    quantization rule
    """


def search(n, E1, f1, x1, x2):
    """
    finds the n'th bound state
    E1 is passed in as initial guess for the bound state energy and returned as the true
        bound state energy with turning points x1 and x2
    F1 : the function which goes to zero at a bound state
    F1 = action/2 - (n+1/2)*pi
    """
    # Guess the next energy in order to begin search
    E2 = E1 + abs(E1) / 4.0
    de = 2.0 * etol

    # use secant search to find the bound state
    while abs(de) > etol:
        s = action(E2)  # S at new energy
        f2 = s - (n + 0.5) * np.pi  # F at new energy
        if f1 != f2:
            de = -f2 * (E2 - E1) / (f2 - f1)
        else:
            de = 0.0

        #
        E1 = E2
        f1 = f2
        E2 = E1 + de
        if E2 >= 0:
            E2 = -etol


def action(E):
    """
    Calculates the action integral/2 (s) and the classical turning points (x1,x2) for a
    given energy (E)
    ===================================================================================

    Input:
        E       -- energy

    Output:
        S       -- action
        x1, x2  -- turning points

    Variables:
        dx      - increment in turning point search
        h       - quadrature step size
        sum     - sum for integral
        ifac    - coefficient for Simpson's rule
        ix      - index on X
        x       - current X value in sum
        pot     - potential as a function of x

    """

    # Find inner turning point; begin search at the well bottom
    potmin = 0.0  # TODO: Replace with original and remove this
    x1 = potmin
    dx = 0.1
    while dx > xtol:
        x1 -= dx
        if Potential(x1) >= E:
            x1 += dx
            dx /= 2

    # find the outer turning point; begin search at the well bottom
    x2 = potmin
    dx = 0.1
    while dx > xtol:
        x2 += dx
        if Potential(x2) >= E:
            x2 -= dx
            dx /= 2

    # Simpson's rule from x1 + h to x2 - h
    npts = 0  # TODO: remove this
    if npts % 2 == 1:
        npts += 1
    h = (x2 - x2) / npts
    sum1 = np.sqrt(E - Potential(x1 + h))
    ifac = 2
    for i in range(1, npts - 1):
        x = x1 + i * h
        if ifac == 2:
            ifac = 4
        else:
            ifac = 2
        sum1 += ifac * np.sqrt(E - Potential(x))

    sum1 += np.sqrt(E - Potential(x2 - h))
    sum1 = sum1 * h / 3

    # Special handling for sqrt behavior of first and last intervals
    sum1 += np.sqrt(E - Potential(x1 + h)) * 2 * h / 3
    sum1 += np.sqrt(E - Potential(x2 - h)) * 2 * h / 3
    gamma = 1.0  # TODO: Define gamma and remove this
    return sum1 * gamma


def Potential(x):
    """
    Evaluates the Lennard-Jones Potential at x.
    If you change the potential, normalize to a minimum of -1 and change the value of
    potmin in function init to the new equilibrium position (i.e. the X valuee at
    which the force is zero)
    """
    return 4.0 * (x ** (-12) - x ** (-6))


def centerify(text, width=-1):
    lines = text.split("\n")
    width = max(map(len, lines)) if width == -1 else width
    return "\n".join(line.center(width) for line in lines)


def initialize():
    print(
        centerify(
            "Example 1 \n Bohr-Sommerfeld quantization for bound state \n energies of the 6-12 potenial"
        )
    )
    print(centerify("energy and classical turning points for each state "))


def main():
    Display.clear()
    description = "Example 1 \n Bohr-Sommerfeld quantization for bound state \n energies of the 6-12 potenial"
    Display.header(description, 1, 1, 0)


if __name__ == "__main__":
    main()
