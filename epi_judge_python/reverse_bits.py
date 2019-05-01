from test_framework import generic_test


def reverse_bits(x):
    result = 0
    for _ in range(64):
        result <<= 1
        result |= (x & 1)
        x >>= 1

    return result

print(reverse_bits(11))
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_bits.py", "reverse_bits.tsv",
                                       reverse_bits))
