from test_framework import generic_test


def ss_decode_col_id(col):
    result = 0
    for c in col:
        result = result * 26 + ord(c) - 65 + 1
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
