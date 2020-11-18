from os import system, name


def centerify(text, width=-1):
    lines = text.split('\n')
    width = max(map(len, lines)) if width == -1 else width
    return '\n'.join(line.center(width) for line in lines)


class display:

    @staticmethod
    def clear():
        # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')

    @staticmethod
    def header(description, nhead, ntext, ngraph):
        # constant part of the header
        print(centerify(
            " Computational Physics \n \n (Python Version) \n \n by Steven E. Koonin and Dawn C. Meredith \n \n Copyright Sudhanva Lalit"))
        # print description related to example
        N = nhead + ntext + ngraph
        for i in range(N):
            if (i == nhead+1):
                print(centerify("\n Text output displays"))
            if (i == nhead + ntext + 1):
                print(centerify("Graphics output displays"))


def main():
    display.clear()
    display.header("This text", 10, 4, 5)


if __name__ == "__main__":
    main()
