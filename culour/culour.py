import os
import curses

COLOR_PAIRS_CACHE = {}


class TerminalColors(object):
    MAGENTA = '[95'
    BLUE = '[94'
    GREEN = '[92'
    YELLOW = '[93'
    RED = '[91'
    END = '[0'


# Translates between the terminal notation of a color, to it's curses color number
TERMINAL_COLOR_TO_CURSES = {
    TerminalColors.RED: curses.COLOR_RED,
    TerminalColors.GREEN: curses.COLOR_GREEN,
    TerminalColors.YELLOW: curses.COLOR_YELLOW,
    TerminalColors.BLUE: curses.COLOR_BLUE,
    TerminalColors.MAGENTA: curses.COLOR_MAGENTA
}


def _get_color(fg, bg):
    key = (fg, bg)
    if key not in COLOR_PAIRS_CACHE:
        # Use the pairs from 101 and after, so there's less chance they'll be overwritten by the user
        pair_num = len(COLOR_PAIRS_CACHE) + 1
        curses.init_pair(pair_num, fg, bg)
        COLOR_PAIRS_CACHE[key] = pair_num

    return COLOR_PAIRS_CACHE[key]


def _color_str_to_color_pair(color):
    if color == TerminalColors.END:
        fg = curses.COLOR_WHITE
    else:
        fg = TERMINAL_COLOR_TO_CURSES[color]
    color_pair = _get_color(fg, curses.COLOR_BLACK)
    return color_pair


def _add_line(y, x, window, line):
    # split but \033 which stands for a color change
    color_split = line.split('\033')

    # Print the first part of the line without color change
    default_color_pair = _get_color(curses.COLOR_WHITE, curses.COLOR_BLACK)
    window.addstr(y, x, color_split[0], curses.color_pair(default_color_pair))
    x += len(color_split[0])

    # Iterate over the rest of the line-parts and print them with their colors
    for substring in color_split[1:]:
        color_str = substring.split('m')[0]
        substring = substring[len(color_str)+1:]
        color_pair = _color_str_to_color_pair(color_str)
        window.addstr(y, x, substring, curses.color_pair(color_pair))
        x += len(substring)


def _inner_addstr(window, string, y=-1, x=-1):
    assert curses.has_colors(), "Curses wasn't configured to support colors. Call curses.start_color()"

    cur_y, cur_x = window.getyx()
    if y == -1:
        y = cur_y
    if x == -1:
        x = cur_x
    for line in string.split(os.linesep):
        _add_line(y, x, window, line)
        # next line
        y += 1


def addstr(*args):
    """
    Adds the color-formatted string to the given window, in the given coordinates
    To add in the current location, call like this:
        addstr(window, string)
    and to set the location to print the string, call with:
        addstr(window, y, x, string)
    Only use color pairs up to 100 when using this function,
    otherwise you will overwrite the pairs used by this function
    """
    if len(args) != 2 and len(args) != 4:
        raise TypeError("addstr requires 2 or 4 arguments")

    if len(args) == 4:
        window = args[0]
        y = args[1]
        x = args[2]
        string = args[3]
    else:
        window = args[0]
        string = args[1]
        y = -1
        x = -1

    return _inner_addstr(window, string, y, x)
