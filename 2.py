# Correct answer: 4613732

from utils import fib

x = sum = 0
while True:
    x += 1
    current = fib(x)
    if current >= 4000000:
        break
    if current % 2 == 0:
        sum += current
print sum
