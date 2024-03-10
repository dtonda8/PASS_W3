import unittest
from typing import List
from data_structures.array_list import ArrayList
from Q2 import find_duplicate_negative_number
from ed_utils.decorators import number


def get_array_list(lst: List) -> ArrayList:
    res = ArrayList(len(lst))
    for num in lst:
        res.append(num)
    return res

class Test_Q2(unittest.TestCase):
    @number("2.1")
    def test_examples(self):
        self.assertEqual(find_duplicate_negative_number(get_array_list([-1,-3,-4,-2,-2])), -2)
        self.assertEqual(find_duplicate_negative_number(get_array_list( [-3,-1,-3,-4,-2])), -3)
        self.assertEqual(find_duplicate_negative_number(get_array_list( [-3,-3,-3,-3,-3])), -3)
    
    @number("2.2")
    def test_extra(self):
        self.assertEqual(find_duplicate_negative_number(get_array_list([-2,-3])), -1)
        self.assertEqual(find_duplicate_negative_number(get_array_list([-3])), -1)
        self.assertEqual(find_duplicate_negative_number(get_array_list([-9,-3,-4,-5,-6,-7,-8,-9])), -1)

if __name__ == '__main__':
    unittest.main()