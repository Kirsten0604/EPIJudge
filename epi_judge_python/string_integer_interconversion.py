from test_framework import generic_test
from test_framework.test_failure import TestFailure
import string

def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True

    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    return ('-' if is_negative else '') + ''.join(reversed(s))


def string_to_int(s):
    is_negative = False
    if s[0] == '-':
        s = s[1:]
        is_negative = True

    result = 0
    for c in s:
        result = result * 10 + string.digits.index(c)

    return -result if is_negative else result


def wrapper(x, s):
    if int_to_string(x) != s:
        raise TestFailure("Int to string conversion failed")
    if string_to_int(s) != x:
        raise TestFailure("String to int conversion failed")

# result = int_to_string(314)
# print(result)
# print(type(result))

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_integer_interconversion.py",
                                       'string_integer_interconversion.tsv',
                                       wrapper))
