import unittest
from Q1 import valid_parentheses
from ed_utils.decorators import number


class Test_Q1(unittest.TestCase):
    @number("1.1")
    def test_examples(self):
        self.assertTrue(valid_parentheses("()"))
        self.assertTrue(valid_parentheses("()[]{}"))
        self.assertFalse(valid_parentheses("(]"))
    
    @number("1.2")
    def test_extra(self):
        self.assertTrue(valid_parentheses("([]{})"))
        self.assertTrue(valid_parentheses("()[{}"))
        self.assertFalse(valid_parentheses("(()"))

if __name__ == '__main__':
    unittest.main()