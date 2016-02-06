# Run this file in order to test culour.
# Running this should produce a curses screen, with a string that's saying the truth
import curses
import culour


class COLORS(object):
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def test(stdscr):
    string = "white{red}red{end}\nwhite{green}green{end}white".format(red=COLORS.RED,
                                                                      green=COLORS.GREEN,
                                                                      end=COLORS.END)
    culour.addstr(stdscr, 10, 50, string)
    stdscr.getch()

curses.wrapper(test)
