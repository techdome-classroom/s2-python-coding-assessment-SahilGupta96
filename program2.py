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
        n = len(s)  
        
        # Iterate through the string  
        for i in range(n):  
            # Check if the current value is less than the next value  
            if i < n - 1 and roman_map[s[i]] < roman_map[s[i + 1]]:  
                total -= roman_map[s[i]]  # Subtract if it's a subtraction case  
            else:  
                total += roman_map[s[i]]   # Add otherwise  
                
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
        # Remove this test if we assume input will always be valid as per constraints  
        self.assertEqual(self.solution.romanToInt(""), 0)  

if _name_ == '_main_':  
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

