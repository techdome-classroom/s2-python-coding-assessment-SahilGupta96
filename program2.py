
def value(r):
	if (r == 'I'):
		return 1
	if (r == 'V'):
		return 5
	if (r == 'X'):
		return 10
	if (r == 'L'):
		return 50
	if (r == 'C'):
		return 100
	if (r == 'D'):
		return 500
	if (r == 'M'):
		return 1000
	return -1

def romanToInt( s: str) -> int:
    
	res = 0
	i = 0

	while (i < len(s)):

		# Getting value of symbol s[i]
		s1 = value(s[i])

		if (i + 1 < len(s)):

			# Getting value of symbol s[i + 1]
			s2 = value(s[i + 1])

			# Comparing both values
			if (s1 >= s2):

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s1
				i = i + 1
			else:

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1

	return res
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
        # Remove this test if we assume input will always be valid as per constraints  
        self.assertEqual(self.solution.romanToInt(""), 0)  

if __name__ == '_main_':  
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

