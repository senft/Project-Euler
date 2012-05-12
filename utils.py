#!/usr/bin/env python2
# coding: utf-8

from math import sqrt


def memoize(fn):
    stored_results = {}

    def memoized(*args):
        try:
            # try to get the cached result
            return stored_results[args]
        except KeyError:
            # nothing was cached for those args. let's fix that.
            result = stored_results[args] = fn(*args)
            return result

    return memoized


@memoize
def factorize(n):
    factors = [1]
    while n > 1:
        for i in xrange(2, n + 1):
            if is_prime(i) and n % i == 0:
                factors.append(i)
                n = n / i
                break
    return factors


@memoize
def is_prime(n):
    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


@memoize
def fib(n):
    return n if n in [0, 1] else fib(n - 2) + fib(n - 1)
