"""
Exercise 1.8: Another important test of a working code is to compare
its results with what is expected on the basis of physical intuition. Restore 
the code to use the Lennard-Jones potential and run it for gamma = 50.
Note that, as in the case of the purely parabolic potential discussed in
the previous exercise, the first excited state is roughly three times as high
above the bottom of the well as is the ground state and that the spacings
between the few lowest states are roughly constant. This is because the
Lennard-Jones potential is roughly parabolic about its minimum (see Figure 1.3). 
By calculating the second derivative of V at the minimum, find
the 'spring constant' and show that the frequency of small-amplitude
motion is expected ta be:

..math::
    \frac{\hbar\omega}{V_0} = \frac{6 \times 2^{5/6}}{\gamma} \approx \frac{10.691}{\gamma}

Verify that this is consistent with the numerical results and explore this
agreement for different values of gamma. Can you understand why the higher
energies are more densely spaced than the lower ones by comparing the
Lennard-Jones potential with its parabolic approximation?
"""

import numpy as np


def main():
    pass


if __name__ == "__main__":
    main()
