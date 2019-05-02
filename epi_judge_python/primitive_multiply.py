from test_framework import generic_test

def add (a,b):
    while b:
        carry = a & b
        a = a ^ b
        b = carry << 1
    return a

def multiply(x, y):
    sum = 0
    while x:
        if x & 1:
            sum = add(sum, y)
        x >>= 1
        y <<= 1
    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("primitive_multiply.py",
                                       'primitive_multiply.tsv', multiply))
