import curses
from time import sleep

from curses import wrapper

curses.initscr()

current_string = "Hello everyone"


def pbar(window):
    # Clear screen
    window.clear()

    for index in range(0, len(current_string)):
        current_char = current_string[index]
        try:
            window.addstr(0, 0, current_string)
        except curses.error as e:
            pass
        val = window.getch(0, index)

    window.refresh()
    window.getkey()


wrapper(pbar)
