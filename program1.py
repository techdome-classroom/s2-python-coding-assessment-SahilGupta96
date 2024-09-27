class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s: 
            if c in '([{': 
                stack.append(c) 
            else: 
                if not stack or \
                    (c == ')' and stack[-1] != '(') or \
                    (c == '}' and stack[-1] != '{') or \
                    (c == ']' and stack[-1] != '['):
                    return False 
                stack.pop() 
        return not stack

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
    



  

