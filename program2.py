class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        prev_value = 0  # Store the value of the previous character

        for char in s:
            current_value = roman_map[char]

            if current_value > prev_value:
                total -= prev_value  # Subtract the previous value if it's smaller
            else:
                total += prev_value

            prev_value = current_value

        total += prev_value  # Add the last character's value

        return total

import unittest

class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)

    def test_example2(self):
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)

    def test_example3(self):
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)

    def test_single_roman_digit(self):
        self.assertEqual(self.solution.romanToInt("X"), 10)

    def test_subtraction_rule(self):
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("IX"), 9)

    def test_large_number(self):
        self.assertEqual(self.solution.romanToInt("MMMCMXCIX"), 3999)

    def test_empty_string(self):
        self.assertEqual(self.solution.romanToInt(""), 0)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


