"""

Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order.
Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321

https://www.codewars.com/kata/5467e4d82edf8bbf40000155

"""


import unittest

# Solution #


def descending_order(num):

    return int("".join(sorted(str(num), reverse=True)))

# Testing #


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(descending_order(0), 0)
        self.assertEqual(descending_order(15), 51)
        self.assertEqual(descending_order(123456789), 987654321)


if __name__ == '__main__':
    unittest.main()