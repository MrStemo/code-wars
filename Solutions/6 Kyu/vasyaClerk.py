"""
The new "Avengers" movie has just been released!
There are a lot of people at the cinema box office standing in a huge line.
Each of them has a single 100, 50 or 25 dollar bill. An "Avengers" ticket costs 25 dollars.

Vasya is currently working as a clerk. He wants to sell a ticket to every single person in this line.

Can Vasya sell a ticket to every person and give change if he initially has no money and sells the tickets strictly in the order people queue?

Return YES, if Vasya can sell a ticket to every person and give change with the bills he has at hand at that moment. Otherwise return NO.

https://www.codewars.com/kata/555615a77ebc7c2c8a0000b8

"""

import unittest

# Solution #

def tickets(people):
    hundreds = 0
    fifties = 0
    twentyfives = 0

    for i in people:

        if i == 100:
            hundreds += 1
            if fifties > 0 and twentyfives > 0:
                fifties += -1
                twentyfives += -1
            elif twentyfives > 2:
                twentyfives += -3
            else:
                return "NO"

        if i == 50:
            fifties += 1
            if twentyfives > 0:
                twentyfives += -1
            else:
                return "NO"

        if i == 25:
            twentyfives += 1

    return "YES"


# Testing #


class MyTestCase(unittest.TestCase):
    def test(self):
        self.assertEqual(tickets([25, 25, 50]), "YES")
        self.assertEqual(tickets([25, 100]), "NO")


if __name__ == '__main__':
    unittest.main()