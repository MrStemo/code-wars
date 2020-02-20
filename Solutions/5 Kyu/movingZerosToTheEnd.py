"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]

https://www.codewars.com/kata/52597aa56021e91c93000cb0

"""

import unittest

# Solution #


def move_zeros(array):
    # your code here
    new = []
    zeros = []

    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            else:
                new.append(array[i])
        else:
            new.append(array[i])

    return new + zeros



class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(move_zeros([1,2,0,1,0,1,0,3,0,1]),[ 1, 2, 1, 1, 3, 1, 0, 0, 0, 0 ])
        self.assertEqual(move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                      [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
                      ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]),
            ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 1, None, 2, False, 1, 0]), [1, None, 2, False, 1, 0, 0])
        self.assertEqual(move_zeros(["a", "b"]), ["a", "b"])
        self.assertEqual(move_zeros(["a"]), ["a"])
        self.assertEqual(move_zeros([0, 0]), [0, 0])
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([False]), [False])
        self.assertEqual(move_zeros([]), [])


if __name__ == '__main__':
    unittest.main()
