# Copyright (C) 2021 Arya K. O.
#
# Test is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
# *TypingSpeed-TUI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with *TypingSpeed-TUI. If not, see http://www.gnu.org/licenses/

import curses
from time import sleep

from curses import wrapper

curses.initscr()

current_string = "Hello everyone"


def test_typing(window):
    # Clear screen
    window.clear()
    curses.start_color()

    curses.init_pair(10, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(11, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(12, curses.COLOR_WHITE, curses.COLOR_BLACK)

    window.addstr(0, 0, current_string, curses.color_pair(12))
    typed_chars = ()
    for index in range(-1, len(current_string)):
        next_char = current_string[index+1]
        not_typed_chars = current_string[max(index, 0):]

        try:
            print(list(enumerate(typed_chars)))
            print(next_char)
            window.addstr(0, max(index, 0), not_typed_chars, curses.color_pair(12))
            if index >= 0:
                for char_num, (char, color) in enumerate(typed_chars):
                    window.addstr(0, char_num, char, curses.color_pair(color))
        except curses.error as e:
            "pass"

        val = chr(window.getch(0, index+1))
        print(val)
        typed_chars += ((next_char, 10 if str(val) == str(next_char) else 11), )


    window.refresh()
    window.getkey()


wrapper(test_typing)
