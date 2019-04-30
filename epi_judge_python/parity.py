from test_framework import generic_test


def parity(x):
    # result = 0
    # while x:
    #     result += x&1
    #     x >>= 1
    #
    # if result % 2 == 0:
    #     return 0
    # else:
    #     return 1
    # return 0
    result = 0
    while x:
        result ^= 1
        x &= x-1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("parity.py", 'parity.tsv', parity))
