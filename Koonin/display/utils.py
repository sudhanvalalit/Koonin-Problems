
from os import system, name


class display:

    def __init__():
        pass


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def centerify(text, width=-1):
    lines = text.split('\n')
    width = max(map(len, lines)) if width == -1 else width
    return '\n'.join(line.center(width) for line in lines)


def header(description, nhead, ntext, ngraph):
    print("You inserted {} {} {} {}".format(description, nhead, ntext, ngraph))


def main():
    pass


if __name__ == "__main__":
    main()
