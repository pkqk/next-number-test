import sys
import unittest


def next_natural(num):
    digits = num_to_digits(num)
    n_sum = sum(digits)
    possible = find_sums(len(digits), n_sum)
    possible_nums = (digits_to_num(digits) for digits in possible)
    greater_nums = (n for n in possible_nums if n > int(num))
    for n in greater_nums:
        return n
    return -1


def find_sums(digit_count, n_sum):
    if digit_count == 1:
        if n_sum < 10:
            yield [n_sum]
    else:
        for i in range(0, min(n_sum, 10)):
            new_sum = n_sum - i
            if new_sum > 0:
                for new_digits in find_sums(digit_count - 1, new_sum):
                    yield [i] + new_digits


def num_to_digits(num):
    return [int(c) for c in str(num)]


def digits_to_num(digits):
    return int(''.join(str(c) for c in digits))


class TestNumberFinder(unittest.TestCase):

    def test_123(self):
        self.assertEqual(132, next_natural('123'))

    def test_0200(self):
        self.assertEqual(1001, next_natural('0200'))

    def test_09999999999999(self):
        #self.assertEqual(18999999999999, next_natural('09999999999999'))
        self.assertEqual(189999, next_natural('099999'))

    def test_90(self):
        self.assertEqual(-1, next_natural('99'))

    def test_9999(self):
        self.assertEqual(-1, next_natural('9999'))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print next_natural(sys.argv[1])
    else:
        unittest.main()
