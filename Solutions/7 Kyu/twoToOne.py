"""

Take 2 strings s1 and s2 including only letters from ato z.
Return a new sorted string, the longest possible, containing distinct letters,

each taken only once - coming from s1 or s2.
Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

https://www.codewars.com/kata/5656b6906de340bd1b0000ac

"""


import unittest

# Solution #


def longest(s1, s2):
    return ''.join(sorted(set(s1+s2)))

# Testing #


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(longest("aretheyhere", "yestheyarehere"), "aehrsty")
        self.assertEqual(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
        self.assertEqual(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")


if __name__ == '__main__':
    unittest.main()