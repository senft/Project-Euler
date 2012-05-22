#!/usr/bin/env python
# encoding: utf-8


def main():
    s = str(2 ** 1000)
    sum = 0
    for c in s:
        sum += int(c)

    print sum

if __name__ == '__main__':
    main()
