#!/usr/bin/env python
# encoding: utf-8


from utils import memoize


MAX = 1000000


@memoize
def len_sequence(n):
    if n == 1:
        return 1

    return 1 + len_sequence(n / 2) if n % 2 == 0 else \
            1 + len_sequence(3 * n + 1)


def main():
    print max([(len_sequence(n), n) for n in xrange(1, MAX)])

if __name__ == '__main__':
    main()
