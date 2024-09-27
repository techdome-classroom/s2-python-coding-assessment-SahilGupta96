
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
        

        i = 0
        num = 0
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in roman_map:
                num+=roman_map[s[i:i+2]]
                i+=2
            else:
                #print(i)
                num+=roman_map[s[i]]
                i+=1
        return num
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

