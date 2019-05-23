from test_framework import generic_test


def can_reach_end(A):
    end = len(A) - 1
    i = 0
    furthest_reach = 0

    while i <= furthest_reach and furthest_reach <= end:
        furthest_reach = max(furthest_reach, A[i] + i)
        i += 1
    return furthest_reach >= end


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "advance_by_offsets.py", "advance_by_offsets.tsv", can_reach_end))
