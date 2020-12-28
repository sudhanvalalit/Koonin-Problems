from os import system, name


def centerify(text, width=-1):
    lines = text.split("\n")
    width = max(map(len, lines)) if width == -1 else width
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
        for i in range(N + 1):
            if i == nhead + 1:
                print(centerify("\n Text output displays"))
            if i == nhead + ntext + 1:
                print(centerify("Graphics output displays"))
        print(centerify(''.join(description)))
        input("Press the <ENTER> key to begin the program...")
        Display.clear()


def main():
    Display.clear()
    descrip = []
    descrip.append("This text is written for \n")
    descrip.append("display purposes only")
    Display.header(descrip, 1, 0, 0)


if __name__ == "__main__":
    main()
