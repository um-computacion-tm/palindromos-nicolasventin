import unittest

from Palindromos import palindrome

class TestPalindrome(unittest.TestCase):
    
    def test_1 (self):
        result = palindrome('aba')
        self.assertEqual(result, True)
    
    def test_2 (self):
        result = palindrome('Neuquen')
        self.assertEqual(result, True)
    
    def test_3 (self):
        result = palindrome('vaca')
        self.assertEqual(result, False)

    def test_4 (self):
        result = palindrome('balab')
        self.assertEqual(result, True)




if __name__ == '__main__':
    unittest.main()