"""
Example 1: Bohr-Sommerfeld quantization for bound states of the Lennard-Jones Potential

Computational Physics (Python version)
"""


def search(n, E1, F1, x1, x2):
    """
    finds the n'th bound state
    E1 is passed in as initial guess for the bound state energy and returned as the true bound state energy with turning points x1 and x2
    F1 : the function which goes to zero at a bound state
    F1 = action/2 - (n+1/2)*pi
    """
    # Guess the next energy in order to begin search
    E2 = E1 + abs(E1) / 4.0
    de = 2.0 * ETOL


def Potential(x):
    """
    Evaluates the Lennard-Jones Potential at x.
    If you change the potential, normalize to a minimum of -1 and change the value of potmin in function init to the new equilibrium position (i.e. the X valuee at which the force is zero)
    """
    return 4.0 * (x ** (-12) - x ** (-6))


def main():
    pass


if __name__ == "__main__":
    main()
