from os import system, name
from .menu import *

__all__ = ["Ask"]


def Ask(start, end):
    """
    Input variables:
        start, end - starting and ending menu items to execute
    Local variables:
        i   - current menu item
        ilow, ihigh - integer limits for NUM type
        numskp      - number of blank lines to print
        ichoic      - current menu choice
    Functions:
        charac      - character input
        getflt      - real input
        getint      - integer input
        parse       - determines menu branching
        yesno       - boolean input
    """

    while start < end:
        i = start
        if type(mtype[i]) == float:
            mreals[i] = getflt(mreals[i], mlolim[i], mhilim[i], mprmpt[i])

        start += 1
    # TODO: Continue here


def getflt(x, xmin, xmax, xprmpt):
    """
    Get a  floating point number getflt; make sure it is between xmin and xmax and
    prompt with xprmpt
    If your compiler accepts (FMT=*) to an internal unit, comment out lines 3 and 5
    and uncomment lines 2 and 4 [Not needed in python]
    """
    pass
