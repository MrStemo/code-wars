"""

The goal of this exercise is to convert a string to a new string where each character in the new string is "("
if that character appears only once in the original string, or ")" if that character appears more than once in
the original string. Ignore capitalization when determining if a character is a duplicate.

Examples
"din"      =>  "((("
"recede"   =>  "()()()"
"Success"  =>  ")())())"
"(( @"     =>  "))(("
Notes

Assertion messages may be unclear about what they display in some languages. If you read "...It Should encode XXX",
the "XXX" is the expected result, not the input!

https://www.codewars.com/kata/54b42f9314d9229fd6000d9c

"""


import unittest

# Solution #

def duplicate_encode(word):
    newword = ''
    word = word.lower()
    for i in word:
        if list(word).count(i) > 1:
            newword += ')'
        else:
            newword += '('
    return newword

# Testing #


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(duplicate_encode("din"),"(((")
        self.assertEqual(duplicate_encode("recede"),"()()()")
        self.assertEqual(duplicate_encode("Success"),")())())","should ignore case")
        self.assertEqual(duplicate_encode("(( @"),"))((")


if __name__ == '__main__':
    unittest.main()