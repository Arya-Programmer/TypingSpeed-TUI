#  Copyright (C) 2021 Arya K. O.
#
#  Test is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
#  *TypingSpeed-TUI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with *TypingSpeed-TUI. If not, see http://www.gnu.org/licenses/
#
#  Test is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
#
#  *TypingSpeed-TUI is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
#  See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with *TypingSpeed-TUI. If not, see http://www.gnu.org/licenses/
import unittest
import curses
from src.main import TypeTest


class TypeTestTest(unittest.TestCase):
    def test_init_colors(self):
        """
        Test that it initializes the colors
        """
        curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        TypeTest.init_custom_colors()

        print("curses.pair_number():", curses.color_pair(10))
        self.assertEqual(curses.color_pair(10), 167772160, "Color not initialized!")
        self.assertEqual(curses.color_pair(11), 184549376, "Color not initialized!")
        self.assertEqual(curses.color_pair(12), 201326592, "Color not initialized!")

    # noinspection PyTypeChecker
    def test_colorize_user_input(self):
        """
        Test if the color given to user input is right
        """
        class Test:
            current_string = "Hello world"
        result_correct_input = TypeTest.colorize_user_input(Test(), -1, "H")
        result_incorrect_input = TypeTest.colorize_user_input(Test(), -1, "Y")
        more_result = TypeTest.colorize_user_input(Test(), 1, "l")

        self.assertEqual(result_correct_input, (("H", 10),))
        self.assertEqual(result_incorrect_input, (("H", 11),))
        self.assertEqual(more_result, (("l", 10),))


if __name__ == '__main__':
    unittest.main()
