from test_framework import generic_test


def reverse(x):
    result = 0
    secX = abs(x)
    while secX:
        result = result * 10 + (secX % 10)
        secX = secX // 10

    return -result if x < 0 else result
    #if x < 0: return -result
    # else: return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_digits.py",
                                       'reverse_digits.tsv', reverse))
