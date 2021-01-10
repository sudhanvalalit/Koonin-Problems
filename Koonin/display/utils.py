from os import system, name, get_terminal_size


def centerify(text, width=-1):
    lines = text.split("\n")
    width = get_terminal_size().columns  # if width == -1 else width
    return "\n".join(line.center(width) for line in lines)


class Display:
    @staticmethod
    def clear():
        # for windows
        if name == "nt":
            _ = system("cls")
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system("clear")

    @staticmethod
    def header(description, nhead, ntext, ngraph):
        # constant part of the header
        print(
            centerify(
                " Computational Physics \n \n (Python Version) \n \n by Steven E. Koonin and Dawn C. Meredith \n \n Copyright Sudhanva Lalit"
            )
        )
        #
        # Write out chapter dependent section of the header
        N = nhead + ntext + ngraph
        for i in range(N):
            if i == nhead:
                print(centerify("\n Text output displays"))
            if i == nhead + ntext:
                print(centerify("Graphics output displays"))
            print(centerify(description[i]))
        input("Press the <ENTER> key to begin the program...")
        Display.clear()

    @staticmethod
    def Menu(func):
        mprmpt = []
        [mprmpt.append(0) for i in range(100)]
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
        mprmpt[65] = "Make menu choice and press Return \n"
        mprmpt[71] = "Text output parameters"
        mprmpt[72] = "Do you want text output displayed on screen?"
        mprmpt[73] = "Do you want text output sent to a file?"
        mprmpt[74] = "Enter name of file for text output"
        mprmpt[81] = "Graphics output parameters"
        mprmpt[82] = "Do you want graphics sent to the terminal?"
        mprmpt[83] = "Do you want graphics sent to the hardcopy device?"
        mprmpt[84] = "Do you want data for graphing sent to a file?"
        mprmpt[85] = "Enter name of file for graphics data"
        choice = 6
        while choice != 7:
            for i in range(1, 9):
                print("\t", mprmpt[i])
            choice = int(
                input("Make a menu choice [{}]: \n".format(choice)) or choice)
            if choice == 1:
                Display.clear()
                print("\t", mprmpt[11])
                input("You selected 1")

            elif choice == 2:
                print("\t", mprmpt[36])
                input("You selected 2")

            elif choice == 3:
                Display.clear()
                myList1 = [61, 62, 63, 64]
                [print("\t", mprmpt[i]) for i in myList1]
                newChoice = int(input(mprmpt[65]))
                if newChoice == 3:
                    exit
            elif choice == 4:
                print("\t", "Display parameters here")
                input("Choice 4")
            elif choice == 5:
                print("\t CHoice 5")

            elif choice == 6:
                Display.clear()
                func()
                input("Press enter to continue...")

            # TODO: improve to add choices and run the function with the given choices
            Display.clear()


def main():
    Display.clear()
    descrip = []
    descrip.append("This text is written for \n")
    descrip.append("display purposes only")
    Display.header(descrip, 1, 0, 0)


if __name__ == "__main__":
    main()
