"""

A pangram is a sentence that contains every single letter of the alphabet at least once.
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram,
because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not.
Ignore numbers and punctuation.

https://www.codewars.com/kata/545cedaa9943f7fe7b000048

"""


import unittest

# Solution #


def is_pangram(s):

    s = s.lower()

    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in s:
            continue
        else:
            return False
    return True


# Testing #


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)


if __name__ == '__main__':
    unittest.main()