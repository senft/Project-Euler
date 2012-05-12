#!/usr/bin/env python2
# coding: utf-8


from collections import Counter
from utils import factorize


def triangle(n):
    return (n * (n + 1)) / 2

i = 1
while True:
    current = triangle(i)
    prime_factors = factorize(current)
    count = Counter(prime_factors)
    num_divisors = sum(count.values())

    if num_divisors >= 500:
        print current
        break
    i += 1
