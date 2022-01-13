import unittest

import two_sum

class TwoSum(unittest.TestCase):

    def test_true_case(self):
        x = two_sum.two_sum([24, 12, 8, 3, 6], 5, 11)

        self.assertEqual(1, x)

    def test_false_case(self):
        x = two_sum.two_sum([24, 12, 8, 3, 6], 5, 59)

        self.assertEqual(-1, x)
