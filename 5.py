x = 20
while True:
    for divisor in xrange(2, 21):
        if x % divisor != 0:
            break
    else:
        print x
        break
    x += 10
