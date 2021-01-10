from os import system, name
import numpy as np
"""
MENU: defines menu array variables that are the same for all the programs
"""

#__all__ = ["Menu"]

# Parameters for the values
Float = 0               # Floating point number
Num = 1                 # integer
Boolen = 2              # yes or no user input
Yeskip = 3              # yes or no, skip on YES
Noskip = 4              # yes or no, skip on NO
Skip = 5                # Unconditional skip
Quit = 6                # Abort current ASK call
Title = 7               # print prompt (in ASK or PRTAGS)
Wait = 8                # print prompt and invoke PAUSE
Chstr = 9               # character string
Mtitle = 10             # print MPRMPT() during ASK only
Mchoic = 11             # print prompt, get choice, branch
Pprint = 12             # print out parameters
Clrtrm = 13             # Clear screen


def setup():
    '''
    Allows users to supply i/o parameters for their computing environment
    '''


def Menu(*args):
    mtype, mprmpt, mtag, mstring = [], [], [], []
    # Fill in mtype
    [mtype.append(Mtitle) for i in range(100)]
    myList1 = [0, 10, 35, 60, 70, 80]
    for i in myList1:
        mtype[i] = Clrtrm
    myList2 = [9, 65]
    for i in myList2:
        mtype[i] = Mchoic
    myList3 = [11, 36, 71, 81]
    for i in myList3:
        mtype[i] = Title
    myList4 = [34, 59, 79, 89, 91, 94]
    for i in myList4:
        mtype[i] = Skip
    myList5 = [72, 82, 83]
    for i in myList5:
        mtype[i] = Boolen
    mtype[73], mtype[84] = Noskip, Noskip
    mtype[74], mtype[85] = Chstr, Chstr
    mtype[90], mtype[93] = Pprint, Pprint

    # Fill in mprmpt
    [mprmpt.append(Mtitle) for i in range(100)]
    mprmpt[1] = "Main Menu"
    mprmpt[2] = "1) Change physical parameters"
    mprmpt[3] = "2) Change numerical parameters"
    mprmpt[4] = "3) Change output parameters"
    mprmpt[5] = "4) Display physical and numerical parameters"
    mprmpt[6] = "5) Display output parameters"
    mprmpt[7] = "6) Run Program"
    mprmpt[8] = "7) Stop Program"
    mprmpt[9] = "Make a menu choice"
    mprmpt[11] = "Physical parameters"
    mprmpt[36] = "Numerical parameters"
    mprmpt[61] = "Output Menu"
    mprmpt[62] = "1) Change text output parameters"
    mprmpt[63] = "2) Change graphics output parameters"
    mprmpt[64] = "3) Return to main menu"
    mprmpt[65] = "Make menu choice and press Return"
    mprmpt[71] = "Text output parameters"
    mprmpt[72] = "Do you want text output displayed on screen?"
    mprmpt[73] = "Do you want text output sent to a file?"
    mprmpt[74] = "Enter name of file for text output"
    mprmpt[81] = "Graphics output parameters"
    mprmpt[82] = "Do you want graphics sent to the terminal?"
    mprmpt[83] = "Do you want graphics sent to the hardcopy device?"
    mprmpt[84] = "Do you want data for graphing sent to a file?"
    mprmpt[85] = "Enter name of file for graphics data"

    # MLOLIM
    mlolim = np.zeros(100)
    mlolist1 = [1, 11, 36, 71, 81, 85]
    for i in mlolist1:
        mlolim[i] = 2
    mlolist2 = [9, 65, 74]
    for i in mlolist2:
        mlolim[i] = 1
    mlolim[90] = 11
    mlolim[93] = 71

    # Mhilim
    mhilim = np.zeros(100)
    mhilist1 = [1, 8, 11, 36, 61, 64, 71, 81]
    for i in mhilist1:
        mhilim[i] = 1
    mhilim[9] = 7
    mhilim[65] = 3
    mhilim[74], mhilim[85] = 12, 12
    mhilim[90] = 60
    mhilim[93] = 90

    # mtag
    # Fill in mtag
    [mtag.append(0) for i in range(100)]
    mtag[9] = '11 36 61 91 94 99 99'
    mtag[65] = '71 81 01'
    mtag[72] = "Text output to screen"
    mtag[73] = "Text output to file"
    mtag[74] = "File name for text output"
    mtag[82] = "Graphics output to terminal"
    mtag[83] = "Graphics output to hardcopy device"
    mtag[84] = "Data for graphing sent to file"
    mtag[85] = "File for graphics data"

    # mints
    # Fill in mints
    # These values are taken as input from problems
    txttrm, txtfil, grftrm, grfhrd, grffil = args
    mints = np.zeros(100)
    mints[9] = 6
    mints[65] = 3
    mints[72] = txttrm
    mints[73] = txtfil
    mints[74] = 1
    mints[82] = grftrm
    mints[83] = grfhrd
    mints[84] = grffil
    mints[85] = 2

    # mreals
    mreals = np.zeros(100)
    mreals[9] = -6
    mreals[34] = 1
    mreals[59] = 1
    mreals[73] = 76
    mreals[79] = 61
    mreals[84] = 87
    mreals[89] = 61
    mreals[91] = 1
    mreals[94] = 1

    #
    # Fill in mstrings
    [mstring.append(Mtitle) for i in range(100)]
    mstring[1] = "cmphys.txt"
    mstring[2] = "cmphys.grf"
    return mtype, mprmpt, mhilim, mlolim, mreals, mints, mstring


def main():
    ls = [1, 2, 3, 4, 5]
    # Menu(*ls)


if __name__ == "__main__":
    main()
