import sys


def next_natural(num):
    digits = num_to_digits(num)
    n_sum = sum(digits)
    possible = find_sums(len(digits), n_sum)
    print possible
    possible_nums = [digits_to_num(digits) for digits in possible]
    greater_nums = filter(lambda x: x > num, possible_nums)
    if any(greater_nums):
        next_greatest = sorted(greater_nums)[0]
        return next_greatest
    else:
        return -1

def filter_num(num):
    def f(digits):
        return int(''.join(digits))
    return f

def find_sums(digit_count, n_sum):
    if digit_count == 1:
        if n_sum < 10:
            return [[n_sum]]
        else:
            return []
    else:
        sums = []
        for i in range(1, min(n_sum, 10)):
            new_sum = n_sum - i
            if new_sum > 0:
                for new_digits in find_sums(digit_count - 1, new_sum):
                    sums.append([i] + new_digits)
        return sums

def num_to_digits(num):
    return [int(c) for c in str(num)]

def digits_to_num(digits):
    return int(''.join(str(c) for c in digits))


if __name__ == "__main__":
    print next_natural(int(sys.argv[1]))
