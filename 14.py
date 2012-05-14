#!/usr/bin/env python
# encoding: utf-8


from utils import memoize


MAX = 1000000


@memoize
def len_sequence(n):
    if n < 2:
        return n

    return 1 + len_sequence(n / 2) if n % 2 == 0 else \
            1 + len_sequence(3 * n + 1)


def main():
    max_len, max_start = (0, 0)

    for n in xrange(1, MAX):
        new_len, new_start = len_sequence(n), n
        if new_len > max_len:
            max_start = new_start
            max_len = new_len

    print max_start, max_len

if __name__ == '__main__':
    main()
