#  Copyright (C) 2021 Arya K. O.
#
#  Test is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
#  *TypingSpeed-TUI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with *TypingSpeed-TUI. If not, see http://www.gnu.org/licenses/
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


class TypeTest:

    def __init__(self, window):
        # Clear screen
        self.window = window
        self.current_string = current_string
        self.window.clear()
        curses.start_color()
        self.init_custom_colors()

        self.window.addstr(0, 0, current_string, curses.color_pair(12))

        self.start_test()

        self.window.refresh()
        self.window.getkey()

    @staticmethod
    def init_custom_colors():
        curses.init_pair(10, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(11, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(12, curses.COLOR_WHITE, curses.COLOR_BLACK)

    def start_test(self):
        typed_chars = ()
        for index in range(-1, len(current_string)):
            if index + 1 < len(current_string):
                user_input = self.get_user_input(index)
                typed_chars += self.colorize_user_input(index, user_input)

            try:
                print(list(enumerate(typed_chars)))
                self.color_typed_texts(typed_chars)

            except curses.error as e:
                "pass"

    def get_user_input(self, index):
        next_char_index = index + 1
        return chr(self.window.getch(0, next_char_index))

    def colorize_user_input(self, index, u_input):
        next_char = self.current_string[index + 1]
        return (next_char, 10 if str(u_input) == str(next_char) else 11),

    def color_typed_texts(self, typed_chars):
        for char_num, (char, color) in enumerate(typed_chars):
            self.window.addstr(0, char_num, char, curses.color_pair(color))

    def update_wmp(self):
        self.window.addstr(2, 0, "WMP: ", curses.color_pair(10))


if __name__ == '__main__':
    # test_typing = TypeTest()
    wrapper(TypeTest)
