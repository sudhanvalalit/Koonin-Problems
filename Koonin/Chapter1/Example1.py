"""
Example 1: Bohr-Sommerfeld quantization for bound states of the Lennard-Jones Potential

Computational Physics (Python version)
"""

import numpy as np
import os
import sys
from ..display.utils import Display, selected_choices
from ..display.ask import Ask
from ..display.menu import *

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
# TODO: Correct the value of maxgrf
maxgrf = 10


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
    gamma = 30.0  # np.sqrt(2.0*mass*length**2*potential/hbar**2)
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
    potmin = 2**(1.0/6)
    # Display.Menu(archon)
    ls = [1, 2, 3, 4, 5]
    mtype, mprmpt, mhilim, mlolim, mreals, mints, mstring, mtag = Menu(*ls)
    mints = mints.astype(np.int)
    print(type(mints))
    mtype[12] = Float
    mprmpt[12] = 'Enter gamma = sqrt(2*m*a**2*V/hbar**2) (dimensionless)'
    mtag[12] = 'Gamma (dimensionless)'
    mlolim[12] = 1
    mhilim[12] = 500
    mreals[12] = 50

    mtype[13] = Skip
    mreals[13] = 35

    mtype[37] = Float
    mprmpt[37] = 'Enter tolerance for energy search (scaled units)'
    mtag[37] = 'Energy search tolerance (scaled units)'
    mlolim[37] = 1e-5
    mhilim[37] = 0.01
    mreals[37] = 5e-3
    mtype[38] = Float
    mprmpt[38] = 'Enter tolerance for turning point search (scaled units)'
    mtag[38] = 'Turning point search tolerance (scaled units)'
    mlolim[38] = 1e-5
    mhilim[38] = 0.01
    mreals[38] = 5e-3

    mtype[39] = Num
    mprmpt[39] = 'Enter number of points for action integral'
    mtag[39] = 'Number of quadrature points for action integral'
    mlolim[39] = 20.0
    mhilim[39] = 5e3
    mints[39] = 100

    mtype[40] = Skip
    mreals[40] = 60.0
    mstring[mints[74]] = 'example1.txt'
    mtype[75] = Skip
    mreals[75] = 80.0

    mstring[mints[85]] = 'example.pdf'
    mtype[86] = Num
    mprmpt[86] = 'Enter number of points to be used in graphing'
    mtag[86] = 'Number of graphing points'
    mlolim[86] = 10
    mhilim[86] = maxgrf - 2
    mints[86] = 80

    mtype[87] = Skip
    mreals[87] = 90.0

    data = [mtype, mprmpt, mhilim, mlolim, mreals, mints, mstring, mtag]
    selected_choices(archon, data)


def param():
    Display.clear()
    Ask(1, istop)


def pcheck():
    '''
    Ensure that the number of states is not greater than the size of the data arrays;
    if so prompt for smaller gamma
    '''
    while (nlevel-1) > maxlvl:
        print("Total number of levels (= {:I5}) is larger than maximum allowable (= {:I3})".format(
            nlevel, maxlevel))
        mhilim[igamma] = gamma
        mreals[igamma] = getflt(
            mreals[igamma]/2, mlolim[igamma], mhilim[igamma], 'Enter a smaller gamma')
        gamma = mreals[igamma]
        #
        E = -etol
        x1, x2, S = action(E)
        nlevel = int(S/np.pi + 0.5) + 1


def prmout(munit):
    '''
    outputs parameter summary to the specified unit
    Input variables:
        munit   -   unit number for output 
    Output variables:
        nlines  -   number of lines written so far
    '''
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

    nlines = 7
    return nlines


def txtout(munit, ilevel, E, x1, x2, nlines):
    """
    Writes results for one state to the requested unit
    Input variables:
        munit   -   output unit specifier
        ilevel  -   current level
        E       -   Eigen energy
        x1,x2   -   classical turning points
        nlines  -   number of lines printed so far               
    """

    # if screen is full, clear screen and retype headings
    if(nlines % (trmlin-6) == 0) and (munit == ounit):
        input('to continue...')
        Display.clear()
        print("Level \t Energy \t Xmin \t Xmax")
        print("----- \t ----- \t ----- \t -----")
        print(f"{ilevel:4I} \t {E:.5E} \t {x1:.5E} \t {x2:.5E}")

    # keep track of printed lines only for terminal output
    if munit == ounit:
        nlines += 1


def grfout():
    pass


def main():
    Display.clear()
    init()
    archon()


if __name__ == "__main__":
    main()
