"""
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

Python: return a list;
JavaScript: returns an Array;
C#: returns a string[];
PHP: returns an array;
C++: returns a vector<string>;
Haskell: returns a [String];
Ruby: returns an Array;
Have fun!

for example, a tower of 3 floors looks like below

[
  '  *  ',
  ' *** ',
  '*****'
]
and a tower of 6 floors looks like below

[
  '     *     ',
  '    ***    ',
  '   *****   ',
  '  *******  ',
  ' ********* ',
  '***********'
]

https://www.codewars.com/kata/576757b1df89ecf5bd00073b

"""

import unittest

# Solution #


def tower_builder(n_floors):
    # build here
    spaces = n_floors - 1
    tower = []

    for i in range(1, (n_floors) + 1):
        ast = i * 2 - 1
        tower += 'a'
        tower[i - 1] = ' ' * spaces + '*' * ast + ' ' * spaces
        spaces -= 1

    return tower


# Testing #


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(tower_builder(1), ['*', ])
        self.assertEqual(tower_builder(2), [' * ', '***'])
        self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])


if __name__ == '__main__':
    unittest.main()