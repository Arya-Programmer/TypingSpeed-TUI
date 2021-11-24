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
import datetime
import math
from essential_generators import DocumentGenerator
from unidecode import unidecode

from curses import wrapper

gen = DocumentGenerator()
curses.initscr()


class TypeTest:

    def __init__(self, window):
        # Clear screen
        self.initial_time = datetime.datetime.now()
        self.window = window
        self.current_string = ""
        self.continue_on_mistake = False

        self.window.clear()
        curses.start_color()
        self.init_custom_colors()

        # START
        self.generate_random_text()
        self.show_random_text()
        self.start_test()

        self.window.refresh()
        self.window.getkey()

    @staticmethod
    def init_custom_colors():
        curses.init_pair(10, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(11, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(12, curses.COLOR_WHITE, curses.COLOR_BLACK)

    @staticmethod
    def remove_non_ascii(text):
        return unidecode(text)

    def show_random_text(self):
        self.window.addstr(0, 0, self.current_string, curses.color_pair(12))

    def generate_random_text(self):
        self.current_string = self.remove_non_ascii(gen.gen_sentence(15, 20).replace("\n", ""))

    def start_test(self):
        typed_chars = ()
        words_typed_num = 0
        index = -1
        while index < len(self.current_string):
            if index + 1 < len(self.current_string):
                user_input = self.get_user_input(index)
                user_input_colored = self.colorize_user_input(index, user_input)

                if index == -1:
                    self.initial_time = datetime.datetime.now()

                if not self.continue_on_mistake and user_input_colored[0][1] == 11:
                    if user_input_colored[0][0] == self.current_string[len(typed_chars)]:
                        typed_chars += user_input_colored
                    continue

                if user_input_colored[0][0] == self.current_string[len(typed_chars)]:
                    typed_chars += user_input_colored

            if typed_chars[-1][0] == " ":
                words_typed_num += 1

            try:
                self.color_typed_texts(typed_chars)
                self.update_wpm(words_typed_num)

            except curses.error as e:
                "pass"

            index += 1

        self.prompt_play_again()

    def get_user_input(self, index):
        next_char_index = index + 1
        return chr(self.window.getch(0, next_char_index))

    def colorize_user_input(self, index, u_input):
        next_char = self.current_string[index + 1]
        return (next_char, 10 if str(u_input) == str(next_char) else 11),

    def color_typed_texts(self, typed_chars):
        for char_num, (char, color) in enumerate(typed_chars):
            self.window.addstr(0, char_num, char, curses.color_pair(color))

    def update_wpm(self, w_num):
        duration = datetime.datetime.now() - self.initial_time
        wpm = w_num / (duration.seconds / 60 if duration.seconds != 0 else 1)
        self.window.addstr(2, 0, f"WPM: {math.ceil(wpm)}", curses.color_pair(10))

    def prompt_play_again(self):
        self.window.clear()
        play_again_string = "Do you want to test your typing speed again? Yes[Y]/No[Any key]"
        self.window.addstr(0, 0, play_again_string)
        play_again = self.get_user_input(len(play_again_string)-1).lower() == "y"

        if play_again:
            self.window.clear()
            self.generate_random_text()
            self.show_random_text()
            self.start_test()


if __name__ == '__main__':
    # test_typing = TypeTest()
    wrapper(TypeTest)
