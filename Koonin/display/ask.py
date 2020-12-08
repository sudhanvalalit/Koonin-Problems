from os import system, name
from menu import Menu

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
        if mtype[i] == float:
            mreals[i] = getflt(mreals[i], mlolim[i], mhilim[i], mprmpt[i])

        start += 1
