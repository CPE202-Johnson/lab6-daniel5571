import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_sort(self):
        nums = [23, 7, 5, 12, 1]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 9)
        self.assertEqual(nums, [1, 5, 7, 12, 23])

    def test_worst(self):
        nums = [8, 7, 6, 5, 4, 3, 2, 1]        #worst because it is in reverse numerical order
        comps = insertion_sort(nums)
        self.assertEqual(comps, 28)
        self.assertEqual(nums, [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__': 
    unittest.main()
