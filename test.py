# Run this file in order to test culour.
# Running this should produce a curses screen, with a string that's saying the truth
import curses
import culour

def test(stdscr):
    # Create a string with all colors
    string = ("default "
              "{black}black{end} "
              "{red}red{end} "
              "{green}green{end} "
              "{yellow}yellow{end} "
              "{blue}blue{end} "
              "{magenta}magenta{end} "
              "{cyan}cyan{end} "
              "{white}white{end} "
              "default").format(black='\033[90m',
                              red='\033[91m',
                              green='\033[92m',
                              yellow='\033[93m',
                              blue='\033[94m',
                              magenta='\033[95m',
                              cyan='\033[96m',
                              white='\033[97m',
                              end='\033[0m')

    # Add the string to the curses window
    culour.addstr(stdscr, 10, 10, string)
    stdscr.getch()

curses.wrapper(test)
