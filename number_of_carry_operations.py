"""
Number of Carry Operations

Purpose: count the number of carry operations on sump of two integers.
General challenge time: 15'
"""


import unittest


def number_of_carry_operations(num1, num2):
    num1 = str(num1)
    num2 = str(num2)

    max_length = max(len(num1), len(num2))
    num1 = list(num1.zfill(max_length))
    num2 = list(num2.zfill(max_length))

    count = 0

    for i in range(0, max_length):
        i = -(i+1)  # inverse index

        if int(num1[i]) + int(num2[i]) > 9:
            count += 1
            if len(num1) >= -(i-1):
                num1[i-1] = int(num1[i - 1]) + 1
    return count


def terse_solution(num1, num2):
    def digit_sum(n):
        return sum(map(int, str(n)))
    return (digit_sum(num1) + digit_sum(num2) - digit_sum(num1+num2)) / 9


class TestNumberOfCarryOperations(unittest.TestCase):

    def main_assertions(self, f):
        self.assertEqual(f(123, 456), 0)
        self.assertEqual(f(555, 555), 3)
        self.assertEqual(f(900, 11), 0)
        self.assertEqual(f(145, 55), 2)
        self.assertEqual(f(0, 0), 0)
        self.assertEqual(f(1, 99999), 5)
        self.assertEqual(f(999045, 1055), 5)
        self.assertEqual(f(101, 809), 1)
        self.assertEqual(f(189, 209), 1)

    def test_number_of_carry_operations(self):
        f = number_of_carry_operations
        self.main_assertions(f)

    def test_terse_solution(self):
        f = terse_solution
        self.main_assertions(f)


if __name__ == '__main__':
    unittest.main()
