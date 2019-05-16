from test_framework import generic_test
import math

def is_palindrome_number(x):
    # result = 0
    # if x <= 0:
    #     # if x < 0: return false
    #     # if x == 0: return true
    #     return x == 0
    #
    # secX = abs(x)
    # while secX:
    #     result = result * 10 + (secX % 10)
    #     secX = secX // 10
    # return result == x

    if x <= 0:
     return x ==0

    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask
        x //= 10
        msd_mask //= 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_number_palindromic.py",
                                       "is_number_palindromic.tsv",
                                       is_palindrome_number))
