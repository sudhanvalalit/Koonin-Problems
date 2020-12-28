"""
Example 1: Bohr-Sommerfeld quantization for bound states of the Lennard-Jones Potential

Computational Physics (Python version)
"""

import numpy as np
import os
import sys
from ..display.utils import Display

etol = 1e-6
xtol = 1e-6
maxlat = 1000  # Max number of lattice points
V = np.zeros(maxlat)
x = np.zeros(maxlat)
maxlvl = 10  # Maximum number of quantum levels
igamma = 13
ietol = 38
ixtol = 39
inpts = 40
ingrf = 87


def archon():
    """
    Finds the bound states of the Lennard-Jones potential from the Bohr-Sommerfeld
    quantization rule
    """
    xin = np.empty(maxlvl)
    xout = np.empty(maxlvl)
    Energy = np.empty(maxlvl)
    NLEVEL = maxlvl
    E1 = -1.0               # Begin at well bottom
    F1 = -np.pi/2           # the action is zero there
    # Find the nlevel bound states
    for i in range(NLEVEL-1):
        Energy[i], xin[i], xout[i] = search(i, E1, F1)
        F1 = F1 - np.pi
        print(
            f"{i} \t {Energy[i]:.5e} \t {F1:.5e} \t {xin[i]:.5e} \t {xout[i]:.5e}")


def search(n, E1, f1):
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
    x1, x2 = 0, 0
    # use secant search to find the bound state
    while abs(de) > etol:
        x1, x2, s = action(E2)  # S at new energy
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

    return E2, x1, x2


def action(E):
    """
    Calculates the (action integral)/2 (S) and the classical turning points (x1,x2) for a
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
    potmin = 2**(1.0/6)
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
    npts = 32  # TODO: remove this
    if npts % 2 == 1:
        npts += 1
    h = (x2 - x1) / npts
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
    # TODO: Define gamma and remove this
    gamma = 1.0  # np.sqrt(2.0*mass*length**2*potential/hbar**2)
    S = sum1 * gamma
    return x1, x2, S


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


def init():
    """
    Initializes constants, displays header screen, initializes menu arrays for input parameter
    """
    # Get environment parameters
    description = []
    description.append("Example 1 \n")
    description.append("Bohr-Sommerfeld quantization for bound state \n ")
    description.append("energies of the 6-12 potenial \n")
    nhead = 3

    # text output description
    description.append("energy and classical turning points for each state \n")
    ntext = 1

    # graphics output description
    description.append("phase space (wavenumber vs position) portrait \n")
    description.append("of classical trajectories \n")
    ngraph = 2

    # Call header
    Display.header(description, nhead, ntext, ngraph)


def param():
    pass


def pcheck():
    pass


def prmout(munit, nlines):
    if munit == ounit:  # TODO : define ounit
        Display.clear()
    #
    print(' ')
    print(' Output from example 1: Bohr Sommerfeld Quantization \n')
    print(
        "Energy tolerence = {:.5E} \t position tolerance = {:.5E}".format(etol, xtol))
    print(" number of quadrature points = {:4I}".format(npts))
    print("For gamma = {:.F2} there are {:4I} levels:".format(gamma, nlevel))
    print("(all quantities are expressed in scaled units)")
    #
    if munit != gunit:  # TODO: define gunit
        print('\t Level \t Energy \t xmin \t xmax')
        print("\t ----- \t ----- \t ----- \t -----")

    nlines = 7  # TODO: Is nlines input or returned?


def txtout():
    """
    Writes results for one state to the requested unit
    """

    # if screen is full, clear screen and retype headings
    if(nlines % (trmlin-6) == 0) and (munit == ounit):
        input('to continue...')
        Display.clear()
        # TODO: continue from here


def grfout():
    pass


def main():
    Display.clear()
    init()
    archon()


if __name__ == "__main__":
    main()
