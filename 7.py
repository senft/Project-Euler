# Correct answer: 104743
from math import sqrt


def is_prime(n):
    for i in xrange(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

primes = [2]

while len(primes) < 10001:
    n = primes[-1] + 1
    while not is_prime(n):
        n += 1
    primes.append(n)
    print len(primes), ':', n
